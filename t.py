import os

with open('C:\\Yosh\\#language.txt', 'r', encoding="utf-8") as txt:
    language = txt.read()
    language = [''] + language.splitlines()

start = int(language[1].split(":")[29])
hashtag = int(language[1].split(":")[3])
tex0 = [0]
bres_list = []
add_tex0 = filetype = file = header = 0
colourenc = ['I4', 'I8', 'IA4', 'IA8', 'RGB565', 'RGB5A3', 'RGBA8', 0, 'CI4', 'CI8', 'CI14x2', 0, 0, 0, 'CMPR']
extensions = ['.bin', '.mdl', '.cmp']
bresarc = [b'U\xaa8-', b'bres']


def message():
    print(f"\n\n{language[start]},\n{language[start + 1]}\n{language[start + 2]}\n{language[start + 3]}\n\n{language[start + 4]}\n")


def external():
    print(f'{language[start + 30]}\n\n{language[start + 31]}\n{language[start + 32]}')


for file in os.listdir('./'):
    if not os.path.isfile(file) or os.path.getsize(file) < 10:
        continue
    try:
        with open(file, 'rb') as stuff:
            header = stuff.read(4)

    except PermissionError as error:
        # print(error)
        continue

    if header in bresarc:
        break
if header not in bresarc:  # the for can ends after browsing a complete directory without finding any brres or arc file.
    input(f'{language[start + 5]}.\n{language[start + 6]}.')
    exit()
compress = True
mode = input(f"{language[start + 7]} : {file}\n{language[start + 33]}\n{language[131]}\n{language[start + 34]}\n{language[start + 35]}\n{language[137]} : ")
if mode in ['2', '3']:  # don't compress
    compress = False
while mode in ["1", "2"]:  # that's not the file you want, so type manually the filename
    file = input(f'{language[138]} : ')
    if not os.path.exists(file):
        continue
    with open(file, 'rb') as check:
        if check.read(4) not in bresarc:
            print(f'{language[139]}.')
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
    print(language[140])  # in case it's long

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
        tex_name = input(f'{language[start + 36]} ')  # remember quote is a forbidden character in windows
        tex_name = tex_name.strip('"')  # if you drag and drop it adds quotes and create a name that doesn't exists
        if not os.path.exists(tex_name):  # yes, python considers quotes as part of a file name
            print(f'{tex_name} {language[start + 20]}.\n{language[start + 37]}.')
            continue
        with open(f'{tex_name}', 'r+b') as check_tex0:
            header = check_tex0.read(4)
        if header != b'TEX0':
            print(f"{language[start + 38]}\n{language[start + 39]}")
            continue
        while header != 1:  # while user enters a wrong number
            pos = input(f'{language[start + 23]} : ')
            if pos in ['0', '-0', '']:
                print(language[start + 24])
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
            # data_size = (byte[0] * 16777216) + (byte[1] * 65536) + (byte[2] * 256) + byte[3] - 64  # 4 bytes integer
            data_size = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3] - 64  # 4 bytes integer
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
            input(f'{tex_name}{language[hashtag + 8].split("#")[1]}{dim_tex[0] * 256 + dim_tex[1]}{language[hashtag + 8].split("#")[2]}{dim_tex[2] * 256 + dim_tex[3]}{language[hashtag + 8].split("#")[3]}{file}{language[hashtag + 8].split("#")[4]}{arc_tex_dim[0] * 256 + arc_tex_dim[1]}{language[hashtag + 8].split("#")[5]}{arc_tex_dim[2] * 256 + arc_tex_dim[3]}\n{language[start + 30]}\n\n{language[start + 31]}\n\n{language[start + 32]}\n')
            external()
            continue

        cursor = tex0[pos] + 39  # the 39th byte of a tex0 file is the number of mipmaps +1
        arc.seek(cursor)  # a mipmap is a duplicate of a texture downscaled by 2, used when far away
        arc_mips = arc.read(1)[0] - 1  # to use less RAM, and also looks better visually when far away (not distorted)

        arc.seek(cursor - 4)
        arc_color = arc.read(1)[0]  # the 35th byte of a tex0 file is the colour encoding, see colourenc for full list

        if tex_mips != arc_mips:
            print(file + language[hashtag].split("#")[1] + str(arc_mips) + language[hashtag].split("#")[2] + tex_name + language[hashtag].split("#")[3] + str(tex_mips))
            external()
            continue
        if arc_color != tex_color:
            print(file + language[hashtag + 1].split("#")[1] + colourenc[arc_color] + language[hashtag + 1].split("#")[2] + tex_name + language[hashtag + 1].split("#")[3] + colourenc[tex_color])
            external()
            continue

        next_tex0_pos = arc_tex0_data_pos + data_size
        if pos == -1 or pos == len(tex0) - 1:  # if the texture is the last one, it doesn't have a next
            next_tex0_pos = arc_tex0_data_pos - 64
        arc.seek(next_tex0_pos)
        header = arc.read(4)
        brres = bres_list[-1]  # equals zero if the list is empty or the first brres offset if not empty
        if (brres == 0 or next_tex0_pos < brres) and header != b'TEX0':
            print(language[start + 40])
            print(f'dev info : current file = {file} ; picture name = {tex_name} ; tex0 data size = {data_size}')
            print(f'offset of next tex0 = {next_tex0_pos} ; next brres offset = {brres}')
            input(language[start + 32])
            continue
        arc.seek(arc_tex0_data_pos)
        arc.write(tex)  # custom texture data
        print(language[start + 41])
        add_tex0 = input(f'{language[start + 42]}\n')

if compress:
    with open(file, 'rb') as check_mdl:
        check_mdl.seek(0)
        if check_mdl.read(1) == b'\x00':
            filetype = 2  # .cmp
        while cursor > size - 2222:
            cursor -= 1
            check_mdl.seek(cursor)
            if check_mdl.read(6) == b'body_h':
                filetype = 1  # .mdl
                break
    os.system(f'C:\\Yosh\\n.exe "{file}" -lh -o "{short}{extensions[filetype]}" -A32')
