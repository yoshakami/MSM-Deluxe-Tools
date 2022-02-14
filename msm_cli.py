from PIL import Image, UnidentifiedImageError
from hashlib import sha256
import subprocess
import shutil
import struct
import sys
import os

print(sys.argv)
argv = sys.argv
done = []
colourenc = ['I4', 'I8', 'IA4', 'IA8', 'RGB565', 'RGB5A3', 'RGBA8', 0, 'CI4', 'CI8', 'CI14X2', 0, 0, 0, 'CMPR']
hexl = ["0", "1", "2", "3", "4", "5", '6', '7', '8', '9', 'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F']  # hex letters
arg = ''
help_text = """
available commands :
pack -w -k [file_DECOMP.bin] (-k means "keep encoded folder") (-w means to force wszst arc rebuilding method, by default it's choosing automatically the correct method)
dump -m -k [file_DECOMP.bin] (-m means "dump mipmaps")
bstick [#RRGGBB colour] -f [file_DECOMP.bin] (-f means "fix colour")
brsar [file]
trib [file_DECOMP.bin]
tex [cmpr|rgb5a3|i4|i8|ai4|ai8|rgb565] [number of mipmaps : 0 to 9] [file.png]
extract [file] (alias x)
compress [file_DECOMP.bin] (alias c)
png [file] (convert to png using PIL library)
[file] (automatically patch a brsar/dump a brres/pack if it has already been dumped before/encode to cmpr with 0 mipmaps if it's a png/convert to png if it's a [dds|jpeg|jfif|webp|ico|gif|)
please note that all command will overwrite the output file
"""

def compress(param):  # using lh algorithm (lz77 + huffman)
    j = 2
    if param[1] == 'exe':
        j += 1
        if len(param) < 4:  # msm_cli.py exe c
            return 'please enter a file path'
        for i in range(j + 1, len(param)):
            param[j] += ' ' + param[i]
    output = ''
    for cfile in param[j:]:
        ismodel = iscmp = False
        try:
            with open(cfile, 'rb') as mdl_check:
                mdl_check.seek(0)
                if mdl_check.read(1) == b'\x00':
                    iscmp = True
                if not iscmp:  # if it's not a cmp, check whether it is a mdl or else a bin.
                    if b'\x00\x00\x06body_h\x00\x00' in mdl_check.read():
                        ismodel = True

        except PermissionError as error:  # can't open file
            print(error)
            return

        if '_' in cfile:
            shortname = cfile.rsplit('_', 1)[0]  # if there is a _ in the file name, everything after is just the extension
        elif '.' in cfile:
            shortname = os.path.splitext(cfile)[0]  # if there is a . in the file name
        else:
            shortname = cfile  # else compressed file name will be the file name + its right extension
        if ismodel:
            os.system(f'n "{cfile}" -lh -o "{shortname}.mdl" -A32')  # create a compressed file with mdl extension
            output += f'{shortname}.mdl\n'
        elif iscmp:
            os.system(f'n "{cfile}" -lh -o "{shortname}.cmp" -A32')
            output += f'{shortname}.cmp\n'
        else:
            os.system(f'n "{cfile}" -lh -o "{shortname}.bin" -A32')
            output += f'{shortname}.bin\n'
    return ''


def extract(param):  # extracts a wii-compressed file
    j = 2
    if param[1] == 'exe':
        j += 1
        if len(param) < 4:  # msm_cli.py exe png
            return 'please enter a file path'
        for i in range(j + 1, len(param)):
            param[j] += ' ' + param[i]
    for file in param[j:]:
        try:
            subprocess.run(['n', file, '-x'])  # extracts the file
        except subprocess.CalledProcessError:  # out == b"ERR: Can't extract this file.\r\n":
            # print(f"ERR: Can't extract {file}")
            return ''
    return ''


def hex_float(number):
    number = number.replace(',', '.')  # replaces coma with dots
    num = b''
    w = hex(struct.unpack('<I', struct.pack('<f', float(number)))[0])[2:]
    # add zeros to always make the value length to 8
    # w = '0' * (8-len(w)) + w
    w = w.zfill(8)
    for octet in range(0, 8, 2):  # transform for example "3f800000" to b'\x3f\x80\x00\x00'
        num += bytes(chr(int(w[octet:(octet + 2)], 16)), 'latin-1')
    return num


def dump(param):
    if len(param) == 2:
        return 'please enter a file path'
    file = param[2]
    if param[1] == 'exe':
        if len(param) < 4:
            return 'please enter a file path'
        j = 3
        if param[j].lower() in ['-k', '-m']:
            j += 1
        if param[j].lower() in ['-k', '-m']:
            j += 1
        for i in range(j + 1, len(param)):
            if param[i].lower() in ['-k', '-m']:
                continue
            param[j] += ' ' + param[i]
        file = param[j]
    dumpmip = False
    remtex0 = True
    for option in param:
        if option == '-k':
            remtex0 = False
        elif option == '-m':
            dumpmip = True
    y = os.path.getsize(file)
    counter = k = filepath = 0
    tex0 = True
    folder = os.path.splitext(file)[0]
    if not os.path.exists(folder):
        os.mkdir(folder)
    if not os.path.exists(folder + '/tex0'):
        os.mkdir(folder + '/tex0')
    png_list = []
    size_list = []
    mips_list = []
    color_list = []
    offset_list = []
    tpl_name_list = []
    with open(file, 'rb') as model:
        fil = os.path.splitext(file)[0]
        header = model.read(4)
        if header == b'\x00 \xaf0':  # TPL File
            tex0 = False
            tpl_name_list = [file]
            tpl_start_offset_list = [0]
            tpl_size_list = [y]
            filepath = file
        elif header in [b'U\xaa8-', b'bres']:
            tex0 = False  # it's not only a single tex0 file
            if header in [b'U\xaa8-']:  # brres files doesn't have tpl in them
                # uh, what I'm doing here is getting all the names, offset, and sizes of every TPL file in the archive
                # and what's funny, is that I have no clue of where the name string pool starts,
                # that's why I written a workaround based on the bytes values to get that string pool table start offset
                tpl_name_list = []
                tpl_index_list = []
                tpl_start_offset_list = []
                tpl_size_list = []

                byte = model.read(4)
                filesystem_offset = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3]  # 4 bytes integer
                byte = model.read(4)
                string_pool_table_end_offset = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3] + filesystem_offset
                z = string_pool_table_end_offset - 1
                model.seek(z)
                while 0x1F < k < 0x7F or k == 0:
                    model.seek(z)
                    k = model.read(1)[0]
                    z -= 1
                k = 0
                z += 1
                while not (0x1F < k < 0x7F):
                    z += 1
                    model.seek(z)
                    k = model.read(1)[0]
                string_pool_table_start_offset = z  # + 12 - ((z - filesystem_offset) % 12)
                model.seek(string_pool_table_start_offset)
                string_pool_table = model.read(string_pool_table_end_offset - string_pool_table_start_offset).split(b'\x00')
                for i in range(len(string_pool_table)):
                    if b'.tpl' in string_pool_table[i]:
                        tpl_name_list.append(str(string_pool_table[i])[2:-1])
                        tpl_index_list.append(i)
                for tpl_offset in tpl_index_list:
                    model.seek(filesystem_offset + (12 * tpl_offset) + 4)
                    byte = model.read(4)
                    tpl_start_offset_list.append((byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3])  # 4 bytes integer
                    byte = model.read(4)
                    tpl_size_list.append((byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3])  # 4 bytes integer
                for i in range(len(tpl_start_offset_list)):
                    model.seek(tpl_start_offset_list[i])
                    with open(f"{folder}/tex0/{tpl_name_list[i]}", 'wb') as tpl_file:
                        tpl_file.write(model.read(tpl_size_list[i]))
            # once it's done dealing with TPL files, it can now care about TEX0 files
            z = 0
            while y - 17 > z:
                model.seek(z)
                data = model.read(4)
                if data == b'TEX0':
                    counter += 1
                    byte = model.read(4)
                    model.seek(z + 20)
                    pointer = model.read(4)
                    # print(f'pointer = {pointer}')
                    # tex_size = (byte[0] * 16777216) + (byte[1] * 65536) + (byte[2] * 256) + byte[3] - 64  # 4 bytes integer
                    tex_size = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3]  # 4 bytes integer WITH the 64 bytes header
                    tex_name_offset = (pointer[0] << 24) + (pointer[1] << 16) + (pointer[2] << 8) + pointer[3]  # 4 bytes integer
                    # print(tex_name_offset)
                    model.seek(z + tex_name_offset - 1)
                    name_length = model.read(1)[0]
                    tex_name = str(model.read(name_length))[2:-1]  # removes b' '
                    model.seek(z + 39)
                    tex_mips = model.read(1)[0] - 1
                    model.seek(z + 35)
                    tex_color = model.read(1)[0]
                    model.seek(z)
                    texture = model.read(tex_size)
                    for character in ['\\', '/', ':', '*', '?', '"', '<', '>', '|']:
                        tex_name = tex_name.replace(character, ';')  # forbidden characters by windows
                    if os.path.exists(f'{folder}/tex0/{tex_name}.tex0') and f"{folder}/{tex_name}.png" in png_list:
                        num = 0
                        tex_name += '-0'
                        while os.path.exists(f'{folder}/tex0/{tex_name}.tex0'):
                            tex_name = tex_name[:-len(str(num))]
                            num += 1
                            tex_name += str(num)
                    # padding = b'\x00' * 3 + bytes(chr(len(tex_name)), 'latin_1') + bytes(tex_name, 'latin_1')
                    # i = 11
                    # k = 4 + len(tex_name)
                    # if len(tex_name) > i:
                    #    if k % 16 == 0:
                    #        k = 0
                    # padding += b'\x00' * (16 - k)
                    with open(f'{folder}/tex0/{tex_name}.tex0', 'wb') as tex1:
                        tex1.write(texture)  # + padding
                    if dumpmip:
                        subprocess.run(['wimgt', 'decode', f"{folder}/tex0/{tex_name}.tex0", '-d', f"{folder}/{tex_name}.png", '-o', '--strip'], stdout=subprocess.DEVNULL)
                    else:
                        subprocess.run(['wimgt', 'decode', f"{folder}/tex0/{tex_name}.tex0", '--no-mm', '-d', f"{folder}/{tex_name}.png", '-o', '--strip'], stdout=subprocess.DEVNULL)
                    png_list.append(f"{folder}/{tex_name}.png")
                    size_list.append(tex_size)
                    mips_list.append(tex_mips)
                    color_list.append(colourenc[tex_color])
                    offset_list.append(z)
                z += 16
        elif dumpmip:  # dumps a single tex0 (converts it to png with its mipmaps)
            os.system(f'wimgt decode "{file}" -o --strip')
        else:
            os.system(f'wimgt decode --no-mm "{file}" -o --strip')
    if len(tpl_name_list) > 1:
        for n in range(len(tpl_name_list)):
            if filepath != file:
                filepath = f"{folder}/tex0/{tpl_name_list[n]}"
                fil = os.path.splitext(tpl_name_list[n])[0]
            with open(filepath, 'rb') as tpl_file:
                img_header = []
                tpl_file.seek(4)
                byte = tpl_file.read(4)
                img_count = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3]  # 4 bytes integer
                byte = tpl_file.read(4)
                table_offset = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3]  # 4 bytes integer
                for i in range(img_count):
                    tpl_file.seek(table_offset + (i * 8))
                    byte = tpl_file.read(4)
                    img_header.append((byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3])  # 4 bytes integer
                for i in range(len(img_header)):
                    tpl_file.seek(img_header[i] + 7)
                    tex_color = tpl_file.read(1)[0]
                    byte = tpl_file.read(4)
                    offset_list.append(tpl_start_offset_list[n] + (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3])
                    size_list.append(tpl_size_list[n])
                    if i == 0:
                        png_list.append(f"{folder}/{fil}.png")
                    else:
                        png_list.append(f"{folder}/{fil}.mm{i}.png")
                    mips_list.append(f"TPL{i}")
                    color_list.append(colourenc[tex_color])
            subprocess.run(['wimgt', 'decode', f"{filepath}", '-d', f"{folder}/{fil}.png", '-o', '--strip'], stdout=subprocess.DEVNULL)
            counter += img_count
    if remtex0:
        shutil.rmtree(folder + '/tex0')
        print(f"deleting {folder}/tex0...")
    if not tex0:  # if the file isn't a single tex0 but rather an arc, brres, or tpl file
        if counter > 0:
            with open(folder + '/zzzdump.txt', 'w') as zzzdump:
                zzzdump.write("""Auto-Gerated file by MSM Dump Texture App. Don't delete it else you can't use the Pack Texture app.
It contains all tex0 data size, number of mipmaps, colour encoding, offset in file, dumped png names, and sha256 hashes (used to know which png has been edited)
Also, you may already know that you can't resize any png. else they won't fit inside the brres/arc data.""")
                for i in range(len(png_list)):
                    if not os.path.exists(png_list[i]):
                        print(f"{png_list[i]} no longer exists...............")
                    zzzdump.write('\n' + ' '.join([str(size_list[i]), str(mips_list[i]), color_list[i], str(offset_list[i]), png_list[i].split('/')[-1]]) + '\n')
                    with open(png_list[i], 'rb') as png1:
                        zzzdump.write(sha256(png1.read()).hexdigest())  # sha256 hash of the png
    return f"dumped {counter} textures"


def tex(param):
    if len(param) == 2:
        return 'please enter a png picture path'
    file = param[2]
    if param[1] == 'exe':
        if len(param) < 4:
            return 'please enter a file path'
        j = 3
        if param[j].upper() in colourenc:
            j += 1
        if param[j].isdigit():
            j += 1
        for i in range(j + 1, len(param)):
            param[j] += ' ' + param[i]
        file = param[j]
    colour = 'CMPR'
    nmipmap = '0'
    for i in range (len(param)):
        if param[i].isdigit():
            nmipmap = param[i]
        elif param[i].upper() in colourenc:
            colour = param[i]
    # if colour.upper() not in colourenc:
    #    return "unrecognized colour encoding, choose one in this list \n```py\n['I4', 'I8', 'IA4', 'IA8', 'RGB565', 'RGB5A3', 'RGBA8', 'CI4', 'CI8', 'CI14x2', 'CMPR']```"
    # if not nmipmap.isdigit():
    #    return "invalid number of mipmaps"
    out = f"{os.path.splitext(file)[0]}.tex0"
    os.system(f'wimgt encode "{file}" -x {colour} --n-mm {nmipmap} -d "{out}" -o')
    return ''


def brsar(param):
    if len(param) == 2:
        return 'please enter a file path'
    file = param[2]
    if param[1] == 'exe':
        if len(param) < 4:  # msm_cli.py exe brsar
            return 'please enter a file path'
        j = 3
        for i in range(j + 1, len(param)):
            param[j] += ' ' + param[i]
        file = param[j]
    cursor = patched_num = 0
    with open(file, "r+b") as brsar0:
        while cursor < 0x400000:
            cursor += 1
            brsar0.seek(cursor)
            brstm = brsar0.read(6)
            if brstm == b'.brstm':
                cursor_save = cursor
                patched_num += 1
                while brstm != b"\xff\xff\xff\xff":
                    cursor -= 1
                    brsar0.seek(cursor)
                    brstm = brsar0.read(4)
                cursor -= 8
                brsar0.seek(cursor)
                brsar0.write(b"\x7f\xff\xff\xff")  # above is negative values (so sounds won't play) as it's a signed hex float
                cursor = cursor_save
    return f"patched {patched_num} brstm"


def change_scale(file, default_scale=('1', '1', '1'), custom_scale=(), custom_rotation=(), custom_translation=(), mdl=0, interval=16):
    for setting in [default_scale, custom_scale, custom_rotation, custom_translation]:
        for i in range(len(setting)):
            if not setting[i].lstrip('-').replace('.', '', 1).isdigit() or not setting[i].lstrip('-').replace(',', '', 1).isdigit():
                return setting
    size = os.path.getsize(file)
    j = -1
    mdl_count = 0
    with open(file, "rb") as mdlo:
        for i in range(0, size - 20, interval):
            if mdlo.read(4) == b'MDL0':
                if mdl_count == mdl:
                    j = i
                    break
                mdl_count += 1
    if j == -1:
        return 'no mdl0 found'
    done1 = False
    root_scale = hex_float(default_scale[0]) + hex_float(default_scale[1]) + hex_float(default_scale[2])
    with open(file, "r+b") as mdlo:
        while j < size - 20:
            j += 4
            mdlo.seek(j)
            if mdlo.read(12) == root_scale:
                mdlo.seek(j)
                for setting in [custom_scale, custom_rotation, custom_translation]:
                    x = b''
                    if setting:
                        for z in range(3):
                            x += hex_float(setting[z])
                        mdlo.write(x)
                    j += 12
                    mdlo.seek(j)

                done1 = True
                break
    if done1:
        return file
    else:
        return 'invalid default scale'


def trib(arg2):
    if len(arg2) == 2:
        return 'please enter a file path'
    setting = ['d', 's', 'r', 't', 'm', 'i']
    func_setting = [('1', '1', '1'), (), (), (), 0, 16]
    j = 0
    skip = 0
    if arg2[1] == 'exe':
        if len(arg2) < 4:
            return 'please enter a file path'
        j = 1
    for i in range(j + 2, len(arg2)):
        no_setting = True
        j += 1
        if skip > 0:
            skip -= 1
            continue
        print(arg2[i])
        for k in range(len(setting)):
            if arg2[i].lower() == setting[k]:
                no_setting = False
                if len(arg2[i]) > 1:
                    param = (arg2[i][1:], arg2[i + 1], arg2[i + 2])
                    skip = 2
                else:
                    param = (arg2[i + 1], arg2[i + 2], arg2[i + 3])
                    skip = 3
                if k > 3:  # m and i have only 1 parameter
                    if len(arg2) > i:
                        if arg2[i + 1].isdigit():
                            param = arg2[i + 1]
                            skip = 1
                    else:
                        param = int(arg2[i][1:])
                func_setting[k] = param
                continue
        if no_setting:
            j += 1
            break
    for i in range(j + 1, len(arg2)):
        arg2[j] += ' ' + arg2[i]
    file = arg2[j]
    out = change_scale(file, default_scale=func_setting[0], custom_scale=func_setting[1], custom_rotation=func_setting[2], custom_translation=func_setting[3], mdl=func_setting[4], interval=func_setting[5])
    if out in ['invalid default scale', 'no mdl0 found']:
        return out
    else:
        for i in range(len(func_setting)):
            if out == func_setting[i]:
                return f'invalid parameters after {setting[i]}'
    return 'successfully replaced the root bone attributes of the mdl0'


def tpl_wszst(file, color, name):
    fil = os.path.splitext(file)[0]
    nam = os.path.splitext(name)[0]
    if not os.path.exists(f'{fil}/encoded/{fil}.d'):
        os.system(f'wszst x "{file}" -d "{fil}/encoded/{fil}.d"')
    png_name = os.path.splitext(nam)[0]
    if os.path.exists(f"{fil}/encoded/{fil}.d/arc/timg/"):
        os.system(f'wimgt encode "{fil}/{name}" -x TPL.{color} -d "{fil}/encoded/{fil}.d/arc/timg/{png_name}.tpl" -o')
    elif os.path.exists(f"{fil}/encoded/{fil}.d/timg/"):
        os.system(f'wimgt encode "{fil}/{name}" -x TPL.{color} -d "{fil}/encoded/{fil}.d/timg/{png_name}.tpl" -o')
    else:  # strap
        os.system(f'wimgt encode "{fil}/{name}" -x TPL.{color} -d "{fil}/encoded/{fil}.d/{png_name}.tpl" -o')
    return


# this function will seek to the start offset of the edited texture inside the file given then will encode and write it.
def tpl_multi(file: str, mip: int, color: str, offset: int, name: str):  # assuming file is the name of a tpl file
    nam = os.path.splitext(name)[0]
    fil = os.path.splitext(file)[0]
    encoded = fil + '/encoded'
    os.system(f'wimgt encode "{fil}/{name}" -x {color} --n-mm 0 -d "{encoded}/{nam}-{mip}.tex0" -o')
    with open(file, 'r+b') as new_tpl:
        with open(f"{encoded}/{nam}-{mip}.tex0", "rb") as tex0:
            tex0.seek(4)
            byte = tex0.read(4)
            data_size = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3] - 64  # 4 bytes integer minus SIXTY FOUR
            tex0.seek(64)  # jump over the tex0 header
            tex_data = tex0.read(data_size)
        new_tpl.seek(offset)  # yea, offset is the texture start offset inside a tpl (which can be inside an arc file)
        new_tpl.write(tex_data)


def pack(param):
    if len(param) == 2:
        return 'please enter a file path'
    file = param[2]
    if param[1] == 'exe':
        if len(param) < 4:
            return 'please enter a file path'
        j = 3
        while param[j] in ['-k', '-w']:
            j += 1
        for i in range(j+1, len(param)):
            if param[i] in ['-k', '-w']:
                continue
            param[j] += ' ' + param[i]
        file = param[j]
    fil = os.path.splitext(file)[0]
    # print(fil + '\\zzzdump.txt')
    if not os.path.exists(fil + '\\zzzdump.txt'):
        return 'you need to use "dump" on this file before using this command'
    edited = []
    index_edited = []
    size_list = []
    offset_list = []
    counter = clock = num = wszst = keep_encoded = 0
    for option in param:
        if option == '-k':
            keep_encoded = True
        elif option == '-w':
            wzszt = True
    if os.path.splitext(file)[-1] != ".tpl":  # or METHOD.get() == method[2]:
        wszst = True
    # compare the current hashes with these written in zzzdump.txt and establish a list of edited pictures
    # encode these png to tex0
    encoded = fil + '/encoded'
    if not os.path.exists(encoded):
        os.mkdir(encoded)
    with open(fil + '\\zzzdump.txt', 'r') as zzzdump:
        text = zzzdump.read().splitlines()[3:]  # the first three lines are explaining the purpose of this file
        for line in text:
            if clock:  # one line on two, there's a sha256, then size + mipmaps + color + name
                clock = False
                with open(f"{fil}/{name}", 'rb') as png1:
                    if line != sha256(png1.read()).hexdigest():
                        if mip[:3] == "TPL":
                            counter += 1
                            if wszst:
                                tpl_wszst(file, color, name)
                            else:
                                tpl_multi(file, int(mip[3:]), color, int(offset), name)
                            continue
                        nam = os.path.splitext(name)[0]
                        counter += 1
                        index_edited.append(num)
                        size_list.append(int(size))
                        offset_list.append(int(offset))
                        edited.append(f'{nam}.tex0')
                        os.system(f'wimgt encode "{fil}/{name}" -x {color} --n-mm {mip} -d "{encoded}/{nam}.tex0" -o')
                num += 1
            else:
                clock = True
                size = line.split(' ', 4)[0]
                mip = line.split(' ', 4)[1]
                color = line.split(' ', 4)[2]
                offset = line.split(' ', 4)[3]
                name = line.split(' ', 4)[4]
    # now just replace them inside the file
    if os.path.exists(f'{fil}/encoded/{fil}.d'):
        os.system(f'wszst c "{fil}/encoded/{fil}.d" -d "{file}" -o')

    with open(file, 'r+b') as u8:  # works with arc and brres, so it's just a basic u8 archive format I would say
        for i in range(len(offset_list)):
            u8.seek(offset_list[i] + 4)
            byte = u8.read(4)
            data_size = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3] - 64  # 4 bytes integer WITH THAT MINUS SIXTY FOUR
            if data_size + 64 != size_list[i]:  # will not replace data if it's not the vanilla data size
                print(f"Sizes don't fit. I won't replace {edited[i]}\n{data_size + 64} != {size_list[i]}")
                continue
            with open(f'{encoded}/{edited[i]}', 'rb') as texture:
                texture.seek(64)
                tex0 = texture.read(data_size)
            u8.seek(offset_list[i] + 64)
            u8.write(tex0)
    if not keep_encoded:
        shutil.rmtree(encoded)
    return f"replaced {counter} textures"


# bstick
# with open(file, 'r+b') as binary:
#    header = binary.read(4)
#    if header in [b'bres', b'MDL0']:
#        if b'\x00\x00\x06bstick\x00\x00' in binary.read():  # the mdl0 name must be inside the file

def ishex(text):
    if len(text) != 6:
        return False
    for digit in text:
        if digit not in hexl:
            return False
    return True


def rgvb(param):
    fix = False
    hex_colour = ''
    for option in param:
        if option == '-f':
            fix = True
        elif option[0] == '#':
            hex_colour = option
        elif ishex(option):
            hex_colour = '#' + option
    if not hex_colour:
        print('hex colour unrecognized')
        return
    r = hex_colour[1:3]
    num = int(r, 16)
    temp = num - 128
    if temp < 0:
        temp = 0
    r8 = bytes(chr(temp), 'latin-1')
    r = bytes(chr(num), 'latin-1')

    g = hex_colour[3:4]
    temp = int(g, 16) - 8
    if temp < 0:
        temp = 0
    w = bytes(chr(temp), 'latin-1')
    g = bytes(chr(int(g, 16)), 'latin-1')

    v = hex_colour[4:5]
    temp = int(v, 16) - 7
    if temp < 0:
        temp = 0
    u = bytes(chr(temp * 16), 'latin-1')
    v = bytes(chr(int(v, 16) * 16), 'latin-1')

    b = hex_colour[5:7]
    num = int(b, 16)
    temp = num - 128
    if temp < 0:
        temp = 0
    b8 = bytes(chr(temp), 'latin-1')
    b = bytes(chr(num), 'latin-1')
    if fix:  # r = r8  #g = w  #v = u  #b = b8 #{r7}{fa}{fb}{b7}
        return r8 + w + u + b8
    return r + g + v + b  # "#{r7}{fa}{fb}{b7}"


def bstick(param):  # changes the color in the brres or mdl0 given in argument
    if len(param) == 2:
        return 'please enter a file path'
    j = 2
    while (param[j][0] == '#' and ishex(param[j][1:])) or ishex(param[j]) or param[j] == '-f' or param[j] == 'bstick':
        j += 1
    file1 = param[j]
    if param[1] == 'exe':
        if len(param) < 4:
            return 'please enter a file path'
        for i in range(j+1, len(param)):
            if (param[j][0] == '#' and ishex(param[j][1:])) or ishex(param[j]) or param[j] == '-f' or param[j] == 'bstick':
                continue
            param[j] += ' ' + param[i]
        file1 = param[j]
    colour = rgvb(param)
    # print(colour)
    with open(file1, "r+b") as file:
        y = os.path.getsize(file1)
        cursor = 0
        r = colour[:1]
        gvb = colour[1:4]
        while y - 49 > cursor:
            cursor = cursor + 16
            file.seek(cursor)
            data = file.read(34)
            if data == b'a\xf3?\x00\x00a@\x00\x00\x17a\xfe\x00\xff\xe3aA\x004\xa0aB\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00a\xe2':
                data = file.read(7)
                if data == b'\x00\x00\x00a\xe3\x00\x00':
                    continue
                file.seek(cursor + 36)
                file.write(r)
                file.seek(cursor + 39)
                file.write(gvb)
                file.seek(cursor + 44)
                file.write(gvb)
                file.seek(cursor + 49)
                file.write(gvb)
                return 'successfully applied color in the file'
    return 'no bstick found'


def png(param):
    if len(param) == 2:
        return 'please enter a file path'
    j = 2
    file = param[j]
    if param[1] == 'exe':
        j += 1
        if len(param) < 4:  # msm_cli.py exe png
            return 'please enter a file path'
        for i in range(j + 1, len(param)):
            param[j] += ' ' + param[i]
        file = param[j]

    try:
        pic = Image.open(file)
        pic.save(os.path.splitext(file)[0] + ".png")
        pic.close()
        return 'converted to ' + os.path.splitext(file.split('\\')[-1])[0]+ ".png"
    except UnidentifiedImageError:
        return f"can't convert {file}"


def print_help(param):
    return help_text

command = 'pack', 'dump', 'bstick', 'brsar', 'trib', 'tex', 'png', 'x', 'extract', 'c', 'compress', 'help'
command_func = pack, dump, bstick, brsar, trib, tex, png, extract, extract, compress, compress, print_help


def parse(arg1):
    for i in range(len(command)):
        if command[i] == arg1:
            print(command_func[i](argv))
            done.append(True)
            break
    if not done:
        if len(argv) == 1:
            print('your command is not in the list')
            return
        j = 1
        file = argv[j]
        if file == 'exe':
            j += 1
            if len(argv) < 3:  # msm_cli.py exe
                print('your command is not in the list')
                return
            for i in range(j + 1, len(argv)):
                argv[j] += ' ' + argv[i]
            file = argv[j]
        if os.path.exists(file):
            with open(file, 'rb') as binary:
                d = binary.read(25)
            if d[:4] == b"RSAR":
                brsar([0, 0, file])
            elif d[:6] == b'\x00\x00\x01\x00\x01\x00' and d[17:22] == b'\x00\x16\x00\x00\x00':  # ico
                png([0, 0, file])
            elif d[:2] == b'BM' or d[:3] == b'\xff\xd8\xff' or d[:4] in [b'MM\x00*', b'II*\x00', b'GIF8', b'DDS ']:  # bmp, jpeg, tiff, gif, or dds
                png([0, 0, file])
            elif d[:2] == b'\x00\x00' and d[3:12] == b'\x00\x00\x00\x00\x00\x00\x00\x00\x00' and (d[2:3] in [b'\x02', b'\n']) and d[16:17] in [b'\x18', b'\x20']:  # tga
                png([0, 0, file])  # d[2] = b'\n' if the tga file is compressed
            elif d[:4] == b'\x89PNG':
                tex([0, 0, file])
            elif d[:4] == b'bres' and os.path.exists(os.path.splitext(file)[0] + '/zzzdump.txt'):
                pack([0, 0, file])
            elif d[:4] == b'bres':
                dump([0, 0, file])
    done.clear()


if len(argv) > 1:
    arg = argv[1].lower()
    if argv[1] == 'exe':
        arg = argv[2].lower()
    parse(arg)
    input("press enter to continue...\n")
# print(help_text)
while True:
    arg = input("enter a command : ")
    argv.clear()
    argv.append('0')
    argv.append('exe')
    for parameter in arg.split(' '):
        parameter = parameter.replace('"', '')  # to avoid args with "
        argv.append(parameter)
    arg = argv[2].lower()
    parse(arg)
