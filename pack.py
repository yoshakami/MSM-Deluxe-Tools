import shutil
from tkinter import Tk, Label, Button, END, Entry, Checkbutton, StringVar, OptionMenu
from tkinter.filedialog import askdirectory
from functools import partial
from hashlib import sha256
import os

if ':\\Windows' in os.getcwd():
    os.chdir(os.environ['userprofile'] + '\\Desktop')

with open('C:\\Yosh\\#language.txt', 'r', encoding="utf-8") as txt:
    language = txt.read()
    language = [''] + language.splitlines()

start = int(language[1].split(":")[19])
msm = int(language[1].split(":")[1])
hashtag = int(language[1].split(":")[3])
dump = int(language[1].split(":")[11])
isox = int(language[1].split(":")[13])
button_row = []
for j in range(8, 20):
    button_row += [j, j, j]
for j in range(8, 20):
    button_row += [j, j, j, j]
for j in range(20, 32):
    button_row += [j, j, j, j, j, j, j]

button_col = [0, 1, 2] * 12 + [3, 4, 5, 6] * 12 + [0, 1, 2, 3, 4, 5, 6] * 12
button_list = []
a = Tk()
a.title(language[start])
a.minsize(660, 440)
a.config(bg='#ffaaaa')
a.iconbitmap('C:\\Yosh\\msm_stuff\\pack.ico')
print(f"{language[dump + 2]}\n{language[start + 2]}\n{language[start + 3]}\n{language[start + 4]}\n")


def tpl_wszst(file, color, name):
    fil = os.path.splitext(file)[0]
    nam = os.path.splitext(name)[0]
    if not os.path.exists(f'{fil}/encoded/{fil}.d'):
        os.system(f'wszst x "{file}" -d "{fil}/encoded/{fil}.d"')
    png_name = os.path.splitext(nam)[0]
    os.system(f'wimgt encode "{fil}/{name}" -x TPL.{color} -d "{fil}/encoded/{fil}.d/{png_name}.tpl" -o')
    return


# this function will seek to the start offset of the edited texture inside the file given then will encode and write it.
def tpl_multi(file: str, mip: int, color: str, offset: int, name: str):  # assuming file is the name of a tpl file
    nam = os.path.splitext(name)[0]
    fil = os.path.splitext(file)[0]
    encoded = fil + '/encoded'
    os.system(f'wimgt encode "./{fil}/{name}" -x {color} --n-mm 0 -d "./{encoded}/{nam}-{mip}.tex0" -o')
    with open(file, 'r+b') as new_tpl:
        with open(f"./{encoded}/{nam}-{mip}.tex0", "rb") as tex0:
            tex0.seek(4)
            byte = tex0.read(4)
            data_size = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3] - 64  # 4 bytes integer minus SIXTY FOUR
            tex0.seek(64)  # jump over the tex0 header
            tex_data = tex0.read(data_size)
            new_tpl.seek(offset)  # yea, offset is the texture start offset inside a tpl (which can be inside an arc file)
            new_tpl.write(tex_data)


def pack(file, index):
    fil = os.path.splitext(file)[0]
    with open('C:\\Yosh\\a', 'r+b') as checcbutton:
        checcbutton.seek(16)
        keep_encoded = checcbutton.read(1)
    edited = []
    index_edited = []
    size_list = []
    offset_list = []
    counter = clock = num = wszst = 0
    if os.path.splitext(file)[-1] != ".tpl" or METHOD.get() == method[2]:
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
                with open(f"./{fil}/{name}", 'rb') as png:
                    if line != sha256(png.read()).hexdigest():
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
                        os.system(f'wimgt encode "./{fil}/{name}" -x {color} --n-mm {mip} -d "./{encoded}/{nam}.tex0" -o')
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
            u8.seek(offset_list[i])
            byte = u8.read(4)
            data_size = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3] - 64  # 4 bytes integer WITH THAT MINUS SIXTY FOUR
            if data_size + 64 != size_list[i]:  # will not replace data if it's not the vanilla data size
                print(language[51].replace('#', name) + '\n')
                continue
            with open(f'./{encoded}/{edited[i]}', 'rb') as texture:
                texture.seek(64)
                tex = texture.read(data_size)
            u8.seek(offset_list[i] + 64)
            u8.write(tex)
    if keep_encoded == b'0':
        shutil.rmtree(encoded)
    button_list[index].destroy()
    patched = Label(a, text=language[hashtag + 4].replace("#", str(counter)), bg='#ffaaaa', width=30)
    patched.grid(row=button_row[index], column=button_col[index])


def scan_directory():
    del button_list[:]
    i = 0
    for tkstuff in a.winfo_children():
        if tkstuff not in [text_label, cwd_label, entry_dir, refreshbu, open_explorerbu, T, title, keep_tex0, Method]:
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
            if header in [b'bres', b'U\xaa8-', b'\x00 \xaf0'] and os.path.exists(os.path.splitext(files)[0] + '\\zzzdump.txt'):
                patch = partial(pack, files, i)
                packbu = Button(a, text=files, command=patch, activebackground='#a9ff99', width=30)
                packbu.grid(row=button_row[i], column=button_col[i])
                button_list.append(packbu)
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


def keep():  # each time the checkbutton keep_tex0 is triggered
    with open('C:\\Yosh\\a', 'r+b') as checcbutton:
        checcbutton.seek(16)
        configg = checcbutton.read(1)
        checcbutton.seek(16)
        if configg == b'1':
            checcbutton.write(b'0')
        else:
            checcbutton.write(b'1')


text_label = Label(a, text=language[msm + 18], bg='#ffaaaa', width=30)
text_label.grid(row=0, column=0)

cwd_label = Label(a, text=os.getcwd(), bg='#ffaaaa', width=60, anchor='w')
cwd_label.grid(row=0, column=1, columnspan=3)

entry_dir = Entry(a, width=30)
entry_dir.grid(row=1, column=1)

refreshbu = Button(a, text=language[msm + 40], command=change_directory, activebackground='#ff9999', width=30)
refreshbu.grid(row=1, column=2)

open_explorerbu = Button(a, text=language[msm + 19], command=open_explorer, activebackground='#96c7ff', width=15)
open_explorerbu.grid(row=1, column=0)

T = Label(a, text=language[isox + 5].replace('5', '2'), bg='#ffaaaa', width=40)
T.grid(row=2, column=1, columnspan=2)

title = Label(a, text=language[start + 1], font=(None, 15), bg='#ffaaaa', height=3)
title.grid(row=3, columnspan=9)

method = (' '*70 + language[start + 7] + ' '*(80-len(language[start + 7])), ' '*70+language[start + 8]+' '*(80-len(language[start + 8])), ' '*70+language[start + 9]+' '*(80-len(language[start + 9])))
METHOD = StringVar()
METHOD.set(language[start + 6])
Method = OptionMenu(a, METHOD, *method)
Method["menu"].config(bg="#000000", fg='#ffffff')
Method.config(width=80)
Method.grid(row=4, columnspan=3)

keep_tex0 = Checkbutton(a, text=language[start + 5], command=keep, bg="#ffaaaa", width=25)
keep_tex0.grid(row=2, column=0)

with open('C:\\Yosh\\a', 'rb') as config:
    config.seek(16)
    checkbu = config.read(1)
if checkbu == b'1':
    Checkbutton.select(keep_tex0)

scan_directory()
a.mainloop()
