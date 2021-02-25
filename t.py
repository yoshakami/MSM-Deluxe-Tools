import os

tex0 = [0]
bres_list = []
add_tex0 = filetype = file = header = 0
colourenc = ['I4', 'I8', 'IA4', 'IA8', 'RGB565', 'RGB5A3', 'RGBA8', 0, 'CI4', 'CI8', 'CI14x2', 0, 0, 0, 'CMPR']
extensions = ['.bin', '.mdl', '.cmp']
bresarc = [b'U\xaa8-', b'bres']


def message():
    print("\n\na number was intended or there are less textures than your number,\ncount the texture position in BrawlCrate\nBrawlCrate doesn't only edit the texture data as this app does, but rebuild the whole brres when saving\nthat can damage the file (like destroy bind skin in Mario Sports Mix)\n\nthe number can be negative if you start counting by the bottom\n")


def external():
    print('Did you opened external folder ???\n\nNote also that all textures are counted for all brres in an arc or brres file.\npress enter to go try again...')


for file in os.listdir('./'):
    if not os.path.isfile(file) or os.path.getsize(file) < 4:
        continue
    with open(file, 'rb') as stuff:
        header = stuff.read(4)
    if header in bresarc:
        break
if header not in bresarc:  # the for can ends after browsing a complete directory without finding any brres or arc file.
    input('no brres or arc file found.\npress enter to exit.')
    exit()
compress = True
mode = input(f"replacing in {file}\npress enter to continue (compress at the end) or\n- type 1 if that's not the file you want\n- type 2 if that's not the file you want + don't compress\n- type 3 if you don't want to compress your file when the program ends\nYour choice : ")
if mode in ['2', '3']:  # don't compress
    compress = False
while mode in ["1", "2"]:  # that's not the file you want, so type manually the filename
    file = input('file name with extension : ')
    if not os.path.exists(file):
        continue
    with open(file, 'rb') as check:
        if check.read(4) not in bresarc:
            print('this file is not a brres or an arc file.')
        else:
            mode = '0'
with open(file, 'r+b') as arc:  # though arc could have been named brres as it's the same process for both files
    size = cursor = os.path.getsize(file)
    if '_' in file:
        short = file.rsplit('_', 1)[0]
    elif '.' in file:
        short = os.path.splitext(file)[0]
    else:
        short = file  # short has high probabilities to be the name used in the filesystem of the game
    print('Spotting all texture offsets in the file, please wait...')  # in case it's long

    for z in range(0, size - 17, 16):
        arc.seek(z)
        header = arc.read(4)
        if header == b'TEX0':
            tex0.append(z)  # list of all the textures offsets
        if header == b'bres':
            bres_list.append(z)  # list of all the brres offsets
    bres_list.append(0)
    bres_list.reverse()  # make 0 the last element of the last if it's empty and the first brres offset if not empty

    while add_tex0 != '1':  # while user enters a wrong name
        tex_name = input('texture name with extension : ')  # remember quote is a forbidden character in windows
        tex_name = tex_name.strip('"')  # if you drag and drop it adds quotes and create a name that doesn't exists
        if not os.path.exists(tex_name):  # yes, python considers quotes as part of a file name
            print(f'{tex_name} was not found in the current working directory.\na texture is intended.')
            continue
        with open(f'{tex_name}', 'r+b') as check_tex0:
            header = check_tex0.read(4)
        if header != b'TEX0':
            print("You didn't used a tex0 on this app that only works with already encoded textures.\ntry again")
            continue
        while header != 1:  # while user enters a wrong number
            pos = input('texture position : ')
            if pos in ['0', '-0', '']:
                print("Error: the number can't be 0 (it can be -1 or -2 and more if you start counting by the bottom)")
            elif pos.lstrip('-').isdigit():
                if int(pos.lstrip('-')) > len(tex0):  # if position entered is greater than the max number of tex0 found
                    message()
                    continue
                header = 1  # position entered is valid
                pos = int(pos)
            else:
                message()
        print()  # creates a blank line in cmd, else it looks too compressed
        with open(tex_name, 'rb') as texture:
            if texture.read(4) != b'TEX0':
                continue
            byte = texture.read(4)
            data_size = (byte[0] * 16777216) + (byte[1] * 65536) + (byte[2] * 256) + byte[3] - 64  # 4 bytes integer
            texture.seek(64)  # the header of a tex0 is 64 bytes long
            tex = texture.read(data_size)  # custom texture data

            texture.seek(28)  # the 28th byte of a tex0 file is the offset of dimensions
            dim_tex = texture.read(4)  # 2 bytes integer for width then height

            arc_tex0_data_pos = tex0[pos] + 64
            arc.seek(arc_tex0_data_pos - 36)
            arc_tex_dim = arc.read(4)

            texture.seek(39)
            tex_mips = texture.read(1)[0] - 1

            texture.seek(35)
            tex_color = texture.read(1)[0]

        if dim_tex != arc_tex_dim:  # don't replace vanilla texture if the custom one doesn't have the same size
            input(f'{tex_name} is {dim_tex[0] * 256 + dim_tex[1]}x{dim_tex[2] * 256 + dim_tex[3]} while {file} texture is {arc_tex_dim[0] * 256 + arc_tex_dim[1]}x{arc_tex_dim[2] * 256 + arc_tex_dim[3]}')
            external()
            continue

        cursor = tex0[pos] + 39  # the 39th byte of a tex0 file is the number of mipmaps +1
        arc.seek(cursor)  # a mipmap is a duplicate of a texture downscaled by 2, used when far away
        arc_mips = arc.read(1)[0] - 1  # to use less RAM, and also looks better visually when far away (not distorted)

        arc.seek(cursor - 4)
        arc_color = arc.read(1)[0]  # the 35th byte of a tex0 file is the colour encoding, see colourenc for full list

        if tex_mips != arc_mips:
            print(f'{file} texture has {arc_mips} mipmaps while {tex_name} has {tex_mips}')
            external()
            continue
        if arc_color != tex_color:
            print(f'{file} texture is in {colourenc[arc_color]} colourenc while {tex_name} is in {colourenc[tex_color]}')
            external()
            continue

        next_tex0_pos = arc_tex0_data_pos + data_size
        if pos == -1 or pos == len(tex0) - 1:  # if the texture is the last one, it doesn't have a next
            next_tex0_pos = arc_tex0_data_pos - 64
        arc.seek(next_tex0_pos)
        header = arc.read(4)
        brres = bres_list[-1]  # equals zero if the list is empty or the first brres offset if not empty
        if (brres == 0 or next_tex0_pos < brres) and header != b'TEX0':
            print('replacing texture will override next header, this happens when you use twice the same png.')
            print(f'dev info : current file = {file} ; picture name = {tex_name} ; tex0 data size = {data_size}')
            print(f'offset of next tex0 = {next_tex0_pos} ; next brres offset = {brres}')
            input('this texture will not be replaced, press enter to replace all other textures...')
            continue
        arc.seek(arc_tex0_data_pos)
        arc.write(tex)  # custom texture data

if compress:
    with open(file, 'rb') as check_mdl:
        check_mdl.seek(4)
        if check_mdl.read(1) == b'\x00':
            filetype = 2  # .cmp
        while cursor > size - 2222:
            cursor -= 1
            check_mdl.seek(cursor)
            if check_mdl.read(6) == b'body_h':
                filetype = 1  # .mdl
                break
    os.system(f'n "{file}" -lh -o "{short}{extensions[filetype]}"')
