from tkinter import Tk, Label, Button, END, Entry, Checkbutton
from tkinter.filedialog import askdirectory
from functools import partial
from hashlib import sha256
import shutil
import os


if ':\\Windows' in os.getcwd():
    os.chdir(os.environ['userprofile'] + '\\Desktop')

with open('C:\\Yosh\\#language.txt', 'r', encoding="utf-8") as txt:
    language = txt.read()
    language = [''] + language.splitlines()

start = int(language[1].split(":")[11])
hashtag = int(language[1].split(":")[3])
msm = int(language[1].split(":")[1])
button_row = []
for j in range(8, 20):
    button_row += [j, j, j]
for j in range(8, 20):
    button_row += [j, j, j, j]
for j in range(20, 32):
    button_row += [j, j, j, j, j, j, j]

button_col = [0, 1, 2] * 12 + [3, 4, 5, 6] * 12 + [0, 1, 2, 3, 4, 5, 6] * 12
colourenc = ['I4', 'I8', 'IA4', 'IA8', 'RGB565', 'RGB5A3', 'RGBA8', 0, 'CI4', 'CI8', 'CI14x2', 0, 0, 0, 'CMPR']
button_list = []
a = Tk()
a.title(language[start])
a.minsize(660, 440)
a.config(bg='#aaffbf')
a.iconbitmap('C:\\Yosh\\msm_stuff\\dump.ico')
print(f"{language[start + 2]}\n{language[start + 3]}\n")


def dump(file, index):
    y = os.path.getsize(file)
    counter = z = 0
    with open('C:\\Yosh\\a', 'rb') as config3:
        config3.seek(13)
        keeptex = config3.read(1)
        dumpmips = config3.read(1)
    if keeptex == b'0':  # keep tex0 button unchecked
        remtex0 = True
    else:
        remtex0 = False  # keep tex0 button checked
    if dumpmips == b'1':
        dumpmip = True  # dump mipmaps button checked
    else:
        dumpmip = False
    tex0 = True
    folder = './' + os.path.splitext(file)[0]
    if not os.path.exists(folder):
        os.mkdir(folder)
    if not os.path.exists(folder + '/tex0'):
        os.mkdir(folder + '/tex0')
    png_list = []
    size_list = []
    mips_list = []
    color_list = []
    with open(file, 'rb') as model:
        header = model.read(4)
        if header == b'\x00 \xaf0':  # TPL File
            img_header = []
            model.seek(4)
            byte = model.read(4)
            img_count = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3]  # 4 bytes integer
            byte = model.read(4)
            table_offset = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3]  # 4 bytes integer
            for i in range(img_count):
                model.seek(table_offset + (i * 8))
                byte = model.read(4)
                img_header.append((byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3])  # 4 bytes integer
            for i in range(len(img_header)):
                model.seek(img_header[i] + 7)
                tex_color = model.read(1)[0]
                if i == 0:
                    png_list.append(f"{folder}/{file}.png")
                else:
                    png_list.append(f"{folder}/{file}.mm{i}.png")
                size_list.append(img_header[i])
                if len(img_header) == 1:
                    mips_list.append(f"TPL")
                else:
                    mips_list.append(f"TPL{img_count - 1}")
                color_list.append(colourenc[tex_color])
                os.system(f'wimgt decode "{file}" -d "{folder}/{file}.png" -o --strip')

            png_list.append(f"{folder}/{file}.png")
            size_list.append(y)
            mips_list.append("TPL")
            color_list.append(colourenc[tex_color])
            os.system(f'wimgt decode "{file}" -d "{folder}/{file}.png" -o --strip')

        elif header in [b'U\xaa8-', b'bres']:
            tex0 = False
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
                    with open(f'{folder}/tex0/{tex_name}.tex0', 'wb') as tex:
                        tex.write(texture)  # + padding
                    if dumpmip:
                        os.system(f'wimgt decode "{folder}/tex0/{tex_name}.tex0" -d "{folder}/{tex_name}.png" -o --strip')
                    else:
                        os.system(f'wimgt decode "{folder}/tex0/{tex_name}.tex0" --no-mm -d "{folder}/{tex_name}.png" -o --strip')
                    png_list.append(f"{folder}/{tex_name}.png")
                    size_list.append(tex_size)
                    mips_list.append(tex_mips)
                    color_list.append(colourenc[tex_color])
                z += 16
        elif dumpmip:
            os.system(f'wimgt decode "{file}" -o --strip')
        else:
            os.system(f'wimgt decode --no-mm "{file}" -o --strip')
    if remtex0:
        shutil.rmtree(folder + '/tex0')
        print(language[hashtag + 7].replace('#', folder + '/tex0'))
        # for element in os.listdir(folder + '/tex0'):
        #    if os.path.splitext(element)[-1] == '.tex0':
        #        # os.system(f'del ".\\{folder[2:]}\\{element}"')
        #        if os.path.exists(f'{folder}/tex0/{element}'):
        #            os.remove(f'{folder}/tex0/{element}')
        #        print(language[msm + 48].replace('#', element))
    if not tex0:  # if the file isn't a single tex0 but rather an arc, brres, or tpl file
        with open(folder + '/zzzdump.txt', 'w') as zzzdump:
            zzzdump.write('\n'.join([language[start + 7], language[start + 8], language[start + 9]]))
            for i in range(len(png_list)):
                if not os.path.exists(png_list[i]):
                    print(language[hashtag + 9].replace('#', png_list[i]))
                zzzdump.write('\n' + ' '.join([str(size_list[i]), str(mips_list[i]), color_list[i], png_list[i].split('/')[-1]]) + '\n')
                with open(png_list[i], 'rb') as png:
                    zzzdump.write(sha256(png.read()).hexdigest())  # sha256 hash of the png
    button_list[index].destroy()
    dumped = Label(a, text=language[hashtag + 3].replace("#", str(counter)), bg='#aaffbf', width=30)
    dumped.grid(row=button_row[index], column=button_col[index])


def scan_directory():
    del button_list[:]
    i = 0
    for tkstuff in a.winfo_children():
        if tkstuff not in [text_label, cwd_label, entry_dir, refreshbu, open_explorerbu, keep_tex0, dump_mipmaps, T, title]:
            tkstuff.destroy()

    for files in os.listdir('./'):
        try:
            if not os.path.isfile(files):
                continue
            size = os.path.getsize(files)
            if size < 10 or i >= len(button_col):
                continue
            with open(files, 'rb') as check_file:
                header = check_file.read(4)
            if header in [b'bres', b'U\xaa8-', b'TEX0']:
                patch = partial(dump, files, i)
                dumpbu = Button(a, text=files, command=patch, activebackground='#a9ff99', width=30)
                dumpbu.grid(row=button_row[i], column=button_col[i])
                button_list.append(dumpbu)
                i += 1

        except PermissionError as error:
            print(error)
            continue

    if i > 50:  # if many brres, arc, or tex0 are found, then it puts the window on fullscreen and create a big exit button
        exitbu2 = Button(a, text=language[msm + 39], command=a.quit, activebackground='#d9ff8c', bg='#d9ff8c', fg='#ff2222', width=58, height=3, font=100)
        exitbu2.grid(row=0, column=4, rowspan=2, columnspan=3)
        a.attributes('-fullscreen', True)


def change_directory():  # enter button to change directory (take the entry content)
    cwd = entry_dir.get()
    if cwd == '':
        cwd = os.getcwd()
    else:
        cwd_label.configure(text=cwd)
    entry_dir.delete(0, END)
    os.chdir(cwd)
    scan_directory()


def open_explorer():  # change directory with C:\Windows\explorer.exe GUI
    new_cwd = askdirectory(initialdir=os.getcwd())
    os.chdir(new_cwd)
    cwd_label.configure(text=new_cwd)
    scan_directory()


text_label = Label(a, text=language[msm + 18], bg='#aaffbf', width=30)
text_label.grid(row=0, column=0)

cwd_label = Label(a, text=os.getcwd(), bg='#aaffbf', width=60, anchor='w')
cwd_label.grid(row=0, column=1, columnspan=3)

entry_dir = Entry(a, width=30)
entry_dir.grid(row=1, column=1)

refreshbu = Button(a, text=language[msm + 40], command=change_directory, activebackground='#ff9999', width=30)
refreshbu.grid(row=1, column=2)

open_explorerbu = Button(a, text=language[msm + 19], command=open_explorer, activebackground='#96c7ff', width=15)
open_explorerbu.grid(row=1, column=0)


def keep():  # each time the checkbutton keep_tex0 is triggered
    with open('C:\\Yosh\\a', 'r+b') as checcbutton:
        checcbutton.seek(13)
        configg = checcbutton.read(1)
        checcbutton.seek(13)
        if configg == b'1':
            checcbutton.write(b'0')
        else:
            checcbutton.write(b'1')


def mipmaps():  # each time the checkbutton dump_mipmaps is triggered
    with open('C:\\Yosh\\a', 'r+b') as mipmap:
        mipmap.seek(14)
        config2 = mipmap.read(1)
        mipmap.seek(14)
        if config2 == b'1':
            mipmap.write(b'0')
        else:
            mipmap.write(b'1')


keep_tex0 = Checkbutton(a, text=language[start + 4], command=keep, bg="#aaffbf", width=20)
keep_tex0.grid(row=2, column=0)
dump_mipmaps = Checkbutton(a, text=language[start + 5], command=mipmaps, bg="#aaffbf", width=20)
dump_mipmaps.grid(row=2, column=2)
T = Label(a, text=language[start + 6], bg='#aaffbf', width=30)
T.grid(row=2, column=1)
with open('C:\\Yosh\\a', 'rb') as config:
    config.seek(13)
    checkbu = config.read(1)
    mips = config.read(1)
if checkbu == b'1':
    Checkbutton.select(keep_tex0)
if mips == b'1':
    Checkbutton.select(dump_mipmaps)
title = Label(a, text=language[start + 1], font=500, bg='#aaffbf', height=3)
title.grid(row=3, columnspan=9)

scan_directory()
a.mainloop()
