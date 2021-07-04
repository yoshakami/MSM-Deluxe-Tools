import os
from tkinter import Tk, Label, Button, END, Entry, OptionMenu, StringVar
from tkinter.filedialog import askdirectory
from functools import partial

if ':\\Windows' in os.getcwd():
    os.chdir(os.environ['userprofile'] + '\\Desktop')

with open('C:\\Yosh\\#language.txt', 'r', encoding="utf-8") as txt:
    language = txt.read()
    language = [''] + language.splitlines()

start = int(language[1].split(":")[19])
msm = int(language[1].split(":")[1])
space = " "*20
space25 = " "*25

button_row = []
for j in range(8, 20):
    button_row += [j, j, j]
for j in range(8, 20):
    button_row += [j, j, j, j, j]
for j in range(20, 32):
    button_row += [j, j, j, j, j, j, j, j]

print(f"{language[start + 2]}\n")

button_col = [0, 1, 2] * 12 + [3, 4, 5, 6, 7] * 12 + [0, 1, 2, 3, 4, 5, 6, 7] * 12
button_list = []
a = Tk()
a.title(language[start])
a.minsize(660, 440)
a.config(bg='#bfaaff')
a.iconbitmap('C:\\Yosh\\msm_stuff\\tex.ico')


def encode(file, index):
    colourenc = COLOUR.get()
    colourenc = colourenc.strip(space)
    nmipmap = MIPMAP.get()
    nmipmap = nmipmap.strip(space25)
    out = output.get()
    if out == '':
        out = os.path.splitext(file)
    os.system(f'wimgt encode "{file}" -x {colourenc} --n-mm {nmipmap} -d "{out}.tex0"')

    button_list[index].destroy()
    patched = Label(a, text=language[start + 3], bg='#bfaaff', width=30)
    patched.grid(row=button_row[index], column=button_col[index])


def scan_directory():
    del button_list[:]
    i = 0
    for tkstuff in a.winfo_children():
        if tkstuff not in [text_label, cwd_label, entry_dir, refreshbu, open_explorerbu, title, encoding, mipmaps, output_name, Mipmap, Colour, output, blank]:
            tkstuff.destroy()

    for files in os.listdir('./'):  # display a button for each png found
        try:
            if not os.path.isfile(files):
                continue
            size = os.path.getsize(files)
            if size < 10 or i > 192:
                continue
            with open(files, 'rb') as check_file:
                header = check_file.read(4)
            if header == b'\x89PNG':
                patch = partial(encode, files, i)
                brsarbu = Button(a, text=files, command=patch, activebackground='#a9ff99', width=30)
                brsarbu.grid(row=button_row[i], column=button_col[i])
                button_list.append(brsarbu)
                i += 1

        except PermissionError as error:
            print(error)
            continue

    if i > 36:  # if many png are found, then it puts the window on fullscreen and create a big exit button
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


text_label = Label(a, text=language[msm + 18], bg='#bfaaff', width=30)
text_label.grid(row=0, column=0)

cwd_label = Label(a, text=os.getcwd(), bg='#bfaaff', width=60, anchor='w')
cwd_label.grid(row=0, column=1, columnspan=3)

entry_dir = Entry(a, width=30)
entry_dir.grid(row=1, column=1)

refreshbu = Button(a, text=language[msm + 40], command=change_directory, activebackground='#ff9999', width=30)
refreshbu.grid(row=1, column=2)

open_explorerbu = Button(a, text=language[msm + 19], command=open_explorer, activebackground='#96c7ff', width=15)
open_explorerbu.grid(row=1, column=0)

title = Label(a, text=language[start + 1], font=(None, 15), bg='#bfaaff', height=3)
title.grid(row=2, columnspan=20)

encoding = Label(a, text=language[start + 4], bg='#bfaaff', width=30)
encoding.grid(row=5, column=0)

mipmaps = Label(a, text=language[start + 5], bg='#bfaaff', width=30)
mipmaps.grid(row=5, column=1)

output_name = Label(a, text=language[start + 6], bg='#bfaaff', width=30)
output_name.grid(row=5, column=2)

colour = (
    ' ' * 20 + 'I4' + ' ' * 20, ' ' * 20 + 'I8' + ' ' * 20, ' ' * 20 + 'IA4' + ' ' * 20, ' ' * 20 + 'IA8' + ' ' * 20,
    ' ' * 20 + 'RGB565' + ' ' * 20, ' ' * 20 + 'RGB5A3' + ' ' * 20, ' ' * 20 + 'RGBA8' + ' ' * 20,
    ' ' * 20 + 'CI4' + ' ' * 20, ' ' * 20 + 'CI8' + ' ' * 20, ' ' * 20 + 'CI14x2' + ' ' * 20,
    ' ' * 20 + 'CMPR' + ' ' * 20)
COLOUR = StringVar()
COLOUR.set(colour[10])
Colour = OptionMenu(a, COLOUR, *colour)
Colour["menu"].config(bg="#000000", fg='#ffffff')
Colour.config(width=26)
Colour.grid(row=6, column=0)

mipmap = (' ' * 25 + '0' + ' ' * 25, ' ' * 25 + '1' + ' ' * 25, ' ' * 25 + '2' + ' ' * 25, ' ' * 25 + '3' + ' ' * 25,
          ' ' * 25 + '4' + ' ' * 25, ' ' * 25 + '5' + ' ' * 25, ' ' * 25 + '6' + ' ' * 25, ' ' * 25 + '7' + ' ' * 25,
          ' ' * 25 + '8' + ' ' * 25, ' ' * 25 + '9' + ' ' * 25)
MIPMAP = StringVar()
MIPMAP.set(mipmap[0])
Mipmap = OptionMenu(a, MIPMAP, *mipmap)
Mipmap["menu"].config(bg="#000000", fg='#ffffff')
Mipmap.config(width=26)
Mipmap.grid(row=6, column=1)

output = Entry(a, width=25)
output.grid(row=6, column=2)

blank = Label(a, text="", bg="#bfaaff")
blank.grid(row=7)
scan_directory()
a.mainloop()
