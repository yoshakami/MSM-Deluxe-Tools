import os
from tkinter import Tk, Label, Button, END, Entry, Checkbutton
from tkinter.filedialog import askdirectory
from functools import partial

button_row = []
for j in range(8, 20):
    button_row += [j, j, j]
for j in range(8, 20):
    button_row += [j, j, j, j, j]
for j in range(20, 32):
    button_row += [j, j, j, j, j, j, j, j]

print("this app display max 192 brres or arc in your current working directory.\nif you don't set an output name, it will by default be the name of the png\n")

button_col = [0, 1, 2] * 12 + [3, 4, 5, 6, 7] * 12 + [0, 1, 2, 3, 4, 5, 6, 7] * 12
button_list = []
a = Tk()
a.title('Mario Sports Mix Modding Deluxe Tool : Textures Dump to png')
a.minsize(660, 440)
a.config(bg='#aaffbf')
a.iconbitmap('C:\\Yosh\\dump.ico')


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
    folder = './' + os.path.splitext(file)[0]
    if not os.path.exists(folder):
        os.mkdir(folder)
    with open(file, 'rb') as model:
        header = model.read(4)
        if header in [b'U\xaa8-', b'bres']:
            while y - 17 > z:
                model.seek(z)
                data = model.read(4)
                if data == b'TEX0':
                    counter += 1
                    byte = model.read(4)
                    tex_size = (byte[0] * 16777216) + (byte[1] * 65536) + (byte[2] * 256) + byte[3] - 64  # 4 bytes integer
                    model.seek(z)
                    texture = model.read(tex_size)
                    with open(f'./{folder}/{counter}.tex0', 'wb') as tex:
                        tex.write(texture)
                    if dumpmip:
                        os.system(f'wimgt decode "{folder}/{counter}.tex0" -d "{folder}/{counter}.png"')
                    else:
                        os.system(f'wimgt decode "{folder}/{counter}.tex0" --no-mm -d "{folder}/{counter}.png"')
                z += 16
        else:
            os.system(f'wimgt decode "{file}"')
    if remtex0:
        for element in os.listdir(folder):
            if os.path.splitext(element)[-1] == '.tex0':
                os.system(f'del ".\\{folder[2:]}\\{element}"')
                print('deleting ', element)
    button_list[index].destroy()
    patched = Label(a, text=f'dumped {counter} textures :)', bg='#aaffbf', width=30)
    patched.grid(row=button_row[index], column=button_col[index])


def scan_directory():
    i = 0
    for tkstuff in a.winfo_children():
        if tkstuff not in [text_label, cwd_label, entry_dir, refreshbu, exitbu, open_explorerbu, keep_tex0, dump_mipmaps, T, title]:
            tkstuff.destroy()

    for files in os.listdir('./'):
        size = os.path.getsize(files)
        if os.path.isfile(files) and size > 4 and i < 192:
            with open(files, 'rb') as check_file:
                header = check_file.read(4)
            if header in [b'bres', b'U\xaa8-', b'TEX0']:
                patch = partial(dump, files, i)
                dumpbu = Button(a, text=files, command=patch, activebackground='#a9ff99', width=30)
                dumpbu.grid(row=button_row[i], column=button_col[i])
                button_list.append(dumpbu)
                i += 1
    if i > 50:  # if many brres, arc, or tex0 are found, then it puts the window on fullscreen and create a big exit button
        exitbu2 = Button(a, text='Exit', command=a.quit, activebackground='#d9ff8c', bg='#d9ff8c', fg='#ff2222', width=58, height=3, font=100)
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


text_label = Label(a, text='Current working directory is', bg='#aaffbf', width=30)
text_label.grid(row=0, column=0)

cwd_label = Label(a, text=os.getcwd(), bg='#aaffbf', width=30)
cwd_label.grid(row=1, column=0)

entry_dir = Entry(a, width=30)
entry_dir.grid(row=1, column=1)

refreshbu = Button(a, text='Enter', command=change_directory, activebackground='#ff9999', width=30)
refreshbu.grid(row=1, column=2)

exitbu = Button(a, text='Exit', command=a.quit, activebackground='#d9ff8c', width=15)
exitbu.grid(row=0, column=2)

open_explorerbu = Button(a, text='Open file Explorer', command=open_explorer, activebackground='#96c7ff', width=15)
open_explorerbu.grid(row=0, column=1)


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


keep_tex0 = Checkbutton(a, text="Keep tex0", command=keep, bg="#aaffbf", width=20)
keep_tex0.grid(row=2, column=0)
dump_mipmaps = Checkbutton(a, text="Dump mipmaps", command=mipmaps, bg="#aaffbf", width=20)
dump_mipmaps.grid(row=2, column=2)
T = Label(a, text='Dumping can take up to 2 minutes', bg='#aaffbf', width=30)
T.grid(row=2, column=1)
with open('C:\\Yosh\\a', 'rb') as config:
    config.seek(13)
    checkbu = config.read(1)
    mips = config.read(1)
if checkbu == b'1':
    Checkbutton.select(keep_tex0)
if mips == b'1':
    Checkbutton.select(dump_mipmaps)
title = Label(a, text='MSM Textures Dump', font=500, bg='#aaffbf', height=3)
title.grid(row=3, columnspan=9)
scan_directory()
a.mainloop()
