import os

if ':\\Windows' in os.getcwd():
    os.chdir(os.environ['userprofile'] + '\\Desktop')
    
install_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(install_dir, '#language.txt'), 'r', encoding="utf-8") as txt:
    language = txt.read()
    language = [''] + language.splitlines()

start = int(language[1].split(":")[29])
hashtag = int(language[1].split(":")[3])
tex0 = [0]
name, position, bres_list = [], [], []
add_png = keep = filetype = file = header = 0
colourenc = ['I4', 'I8', 'IA4', 'IA8', 'RGB565', 'RGB5A3', 'RGBA8', 0, 'CI4', 'CI8', 'CI14x2', 0, 0, 0, 'CMPR']
extensions = ['.bin', '.mdl', '.cmp']
bresarc = [b'U\xaa8-', b'bres']

n = os.path.join(install_dir, 'n.exe')

def message():
    print(f"\n\n{language[start]},\n{language[start + 1]}\n{language[start + 2]}\n{language[start + 3]}\n\n{language[start + 4]}\n")


for file in os.listdir('./'):
    if not os.path.isfile(file) or os.path.getsize(file) < 4:
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
mode = input(f"{language[start + 7]} : {file}\n{language[start + 8]}\n{language[start + 9]}\n{language[start + 10]}\n{language[start + 11]}\n{language[start + 12]}\n{language[start + 13]}\n{language[start + 14]}\n{language[start + 15]}")
if mode in ['2', '3', '5', '6']:  # keep encoded textures
    keep = True
if mode in ['4', '5', '6']:  # don't compress
    compress = False
while mode in ["1", "3", "6"]:  # that's not the file you want, so type manually the filename
    file = input(f'{language[start + 16]} : ')
    if not os.path.exists(file):
        continue
    with open(file, 'rb') as check:
        if check.read(4) not in bresarc:
            print(f'{language[start + 17]}.')
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
    print(language[start + 18])  # in case it's long
    for z in range(0, size - 17, 16):
        arc.seek(z)
        header = arc.read(4)
        if header == b'TEX0':
            tex0.append(z)  # list of all the textures offsets
        if header == b'bres':
            bres_list.append(z)  # list of all the brres offsets
    bres_list.append(0)
    bres_list.reverse()  # make 0 the last element of the last if it's empty and the first brres offset if not empty
    cmd_list = []
    while add_png != '1':  # while user enters a wrong name
        picture = input(f'{language[start + 19]} : ')
        if not os.path.exists(f'{picture}.png'):
            print(f'{picture}.png {language[start + 20]}.\n{language[start + 21]}.')
            continue
        with open(f'{picture}.png', 'r+b') as png:
            header = png.read(4)
        if header != b'\x89PNG':
            print(f"{language[start + 22]}.")
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
        name.append(picture)
        position.append(pos)
        print()  # creates a blank line in cmd, else it looks too compressed
        offset = tex0[pos] + 39  # the 39th byte of a tex0 file is the number of mipmaps +1
        arc.seek(offset)  # a mipmap is a duplicate of a texture downscaled by 2, used when far away
        nmipmap = arc.read(1)[0] - 1  # to use less RAM, and also looks better visually when far away (not distorted)
        arc.seek(offset - 4)
        colour = arc.read(1)[0]  # the 35th byte of a tex0 file is the colour encoding, see colourenc for full list
        cmd_list.append(f'wimgt encode "{picture}.png" -x {colourenc[colour]} --n-mm {nmipmap} -o')
        print(language[start + 25])
        add_png = input(f'{language[start + 26]}\n')
        if add_png == '1':
            for command in cmd_list:
                os.system(command)
    # ^ while add_png != 1 ^
    # wimgt will convert all png to encoded texture files called tex0 because their header is tex0

    for i in range(len(name)):  # replace textures in the file by the png given
        tex_name = name[i]
        pos = position[i]
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
        if dim_tex != arc_tex_dim:  # don't replace vanilla texture if the custom one doesn't have the same size
            input(f'{picture}{language[hashtag + 8].split("#")[1]}{dim_tex[0] * 256 + dim_tex[1]}{language[hashtag + 8].split("#")[2]}{dim_tex[2] * 256 + dim_tex[3]}{language[hashtag + 8].split("#")[3]}{file}{language[hashtag + 8].split("#")[4]}{arc_tex_dim[0] * 256 + arc_tex_dim[1]}{language[hashtag + 8].split("#")[5]}{arc_tex_dim[2] * 256 + arc_tex_dim[3]}\n{language[start + 30]}\n\n{language[start + 31]}\n\n{language[start + 32]}\n')
            continue
        next_tex0_pos = arc_tex0_data_pos + data_size
        if pos == -1 or pos == len(tex0) - 1:  # if the texture is the last one, it doesn't have a next
            next_tex0_pos = arc_tex0_data_pos - 64
        arc.seek(next_tex0_pos)
        header = arc.read(4)
        brres = bres_list[-1]  # equals zero if the list is empty or the first brres offset if not empty
        if (brres == 0 or next_tex0_pos < brres) and header != b'TEX0':
            print(language[start + 27])
            print(f'dev info : current file = {file} ; picture name = {picture} ; tex0 data size = {data_size}')
            print(f'offset of next tex0 = {next_tex0_pos} ; next brres offset = {brres}')
            input(language[start + 28])
            continue
        arc.seek(arc_tex0_data_pos)
        arc.write(tex)  # custom texture data

if not keep:
    for instruction in cmd_list:
        if instruction.startswith("del "):
            continue
        texname = instruction.split('wimgt encode ')[1]
        texname = texname.split('.png')[0]
        os.system(f'del "{texname}"')
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
    os.system(f'{n} "{file}" -lh -o "{short}{extensions[filetype]}" -A32')
