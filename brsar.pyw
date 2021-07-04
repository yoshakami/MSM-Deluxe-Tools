import os
from tkinter import Tk, Label, Button, Entry
from tkinter.filedialog import askdirectory
from functools import partial

if ':\\Windows' in os.getcwd():
    os.chdir(os.environ['userprofile'] + '\\Desktop')

with open('C:\\Yosh\\#language.txt', 'r', encoding="utf-8") as txt:
    language = txt.read()
    language = [''] + language.splitlines()

start = int(language[1].split(":")[3])
msm = int(language[1].split(":")[1])
brstm_max_size = b"\x7f\xff\xff\xff"  # above is negative values (so sounds won't play) as it's a signed hex float
button_row = []
for j in range(8, 20):
    button_row += [j, j, j]
for j in range(8, 20):
    button_row += [j, j, j, j, j]
for j in range(20, 32):
    button_row += [j, j, j, j, j, j, j, j]

button_col = [0, 1, 2] * 12 + [3, 4, 5, 6, 7] * 12 + [0, 1, 2, 3, 4, 5, 6, 7] * 12
button_list = []
a = Tk()
a.title(language[start + 13])
a.minsize(660, 440)
a.config(bg='#ffffaa')
a.iconbitmap('C:\\Yosh\\msm_stuff\\brsar.ico')


def patch_brsar(file, index):
    cursor = patched_num = 0
    with open(file, "r+b") as brsar:
        while cursor < 0x400000:
            cursor += 1
            brsar.seek(cursor)
            brstm = brsar.read(6)
            if brstm == b'.brstm':
                cursor_save = cursor
                patched_num += 1
                while brstm != b"\xff\xff\xff\xff":
                    cursor -= 1
                    brsar.seek(cursor)
                    brstm = brsar.read(4)
                cursor -= 8
                brsar.seek(cursor)
                brsar.write(brstm_max_size)
                cursor = cursor_save
    button_list[index].destroy()
    patched = Label(a, text=f'{language[msm + 43].split("#")[0]}{patched_num}{language[msm + 43].split("#")[1]}', bg='#ffffaa', width=30)
    patched.grid(row=button_row[index], column=button_col[index])


def scan_directory():
    i = 0
    for tkstuff in a.winfo_children():
        if tkstuff not in [text_label, cwd_label, entry_dir, refreshbu, open_explorerbu, title]:
            tkstuff.destroy()

    for files in os.listdir('./'):  # display a button for each brsar found
        try:
            if not os.path.isfile(files):
                continue
            size = os.path.getsize(files)
            if size < 10 or i > 192:
                continue
            with open(files, 'rb') as check_file:
                header = check_file.read(4)

        except PermissionError:
            continue

        if header == b'RSAR':
            patch = partial(patch_brsar, files, i)
            brsarbu = Button(a, text=files, command=patch, activebackground='#a9ff99', width=30)
            brsarbu.grid(row=button_row[i], column=button_col[i])
            button_list.append(brsarbu)
            i += 1
    if i > 50:  # creates a big exit button and make the window fullscreen as it was too tiny to display all buttons
        exitbu2 = Button(a, text=language[msm + 40], command=a.quit, activebackground='#d9ff8c', bg='#d9ff8c', fg='#ff2222', width=58, height=3, font=100)
        exitbu2.grid(row=0, column=4, rowspan=2, columnspan=3)
        a.attributes('-fullscreen', True)


def change_directory():  # enter button to change directory (take the entry content)
    cwd = entry_dir.get()
    if cwd == '':
        cwd = os.getcwd()
    else:
        cwd_label.configure(text=cwd)
    entry_dir.delete(0, "end")
    os.chdir(cwd)
    scan_directory()


def open_explorer():  # change directory with C:\Windows\explorer.exe GUI
    new_cwd = askdirectory(initialdir=os.getcwd())
    os.chdir(new_cwd)
    cwd_label.configure(text=new_cwd)
    scan_directory()


text_label = Label(a, text=language[msm + 18], bg='#ffffaa', width=30)
text_label.grid(row=0, column=0)

cwd_label = Label(a, text=os.getcwd(), bg='#ffffaa', width=60, anchor='w')
cwd_label.grid(row=0, column=1, columnspan=2)

entry_dir = Entry(a, width=30)
entry_dir.grid(row=1, column=1)

refreshbu = Button(a, text=language[msm + 19], command=change_directory, activebackground='#ff9999', width=30)
refreshbu.grid(row=1, column=2)

open_explorerbu = Button(a, text=language[msm + 40], command=open_explorer, activebackground='#96c7ff', width=15)
open_explorerbu.grid(row=1, column=0)

title = Label(a, text=language[start + 14], font=500, bg='#ffffaa', height=3)
title.grid(row=2, columnspan=9)
scan_directory()
a.mainloop()
