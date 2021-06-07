import os
import shutil
from tkinter import Tk, Label, Button, Entry, Checkbutton, OptionMenu, StringVar
from tkinter.filedialog import askdirectory
from functools import partial

if ':\\Windows' in os.getcwd():
    os.chdir(os.environ['userprofile'] + '\\Desktop')

with open('#language.txt', 'r') as txt:
    language = txt.read()
    language = [''] + language.splitlines()

extract_row = []
for j in range(5, 16):
    extract_row += [j, j, j, j]
for j in range(5, 16):
    extract_row += [j, j, j, j]
extract_col = [0, 1, 2, 3] * 11 + [4, 5, 6, 7] * 11

create_row = []
for j in range(17, 32):
    create_row += [j, j, j, j]
for j in range(17, 32):
    create_row += [j, j, j, j]
create_col = [0, 1, 2, 3] * 15 + [4, 5, 6, 7] * 15

extract_list = []
create_list = []
a = Tk()
a.title(language[98])
a.minsize(660, 440)
a.config(bg='#aaffaa')
a.iconbitmap('C:\\Yosh\\isox.ico')


def extract(file, index):
    with open('C:\\Yosh\\a', 'rb') as config1:
        config1.seek(15)
        rm_update = config1.read(1)
    file2 = os.path.splitext(file)[0]
    os.system(f'wit extract "{file}" "{file2}" -o')
    if rm_update == b'1':
        shutil.rmtree(f'{file2}\\UPDATE')
        shutil.move(f'{file2}\\DATA', f'{file2}')
        shutil.rmtree(f'{file2}\\DATA')

    extract_list[index].destroy()
    patched = Label(a, text=language[37], bg='#aaffaa', width=30)
    patched.grid(row=extract_row[index], column=extract_col[index])


def create(name, ref):
    filetype = COMPRESSION.get()
    os.system(f'wit copy "{name}" "{name}.{filetype}" -o')

    create_list[ref].destroy()
    if os.path.exists(f"{name}.{filetype}"):
        patched = Label(a, text=language[37], bg='#aaffaa', width=30)
    else:
        patched = Label(a, text=language[99], bg='#aaffaa', width=30)
    patched.grid(row=create_row[ref], column=create_col[ref])


def scan_directory():  # triggered each time Enter button / Open File Explorer button is pressed (or when you launch the script)
    i = n = 0
    for tkstuff in a.winfo_children():
        if tkstuff not in [text_label, cwd_label, entry_dir, refreshbu, open_explorerbu, cb_rm_update, lextract, lextract2, lcompression, Compression, lcreate]:
            tkstuff.destroy()

    for files in os.listdir('./'):  # display a button for each iso, ciso or wbfs found
        # print(os.listdir('./'))
        size = os.path.getsize(files)
        if not os.path.isfile(files) or size < 4 or i > 88:
            continue
        try:
            with open(files, 'rb') as check_file:
                header = check_file.read(4)
                check_file.seek(24)
                iso = check_file.read(4)
                iso2 = check_file.read(4)

            if header in [b'WBFS', b'CISO'] or iso == b']\x1c\x9e\xa3' or iso2 == b'\xc23\x9f=':
                launch_func = partial(extract, files, i)
                extractbu = Button(a, text=files, command=launch_func, activebackground='#a9ff99', width=30)
                extractbu.grid(row=extract_row[i], column=extract_col[i])
                extract_list.append(extractbu)
                i += 1

        except PermissionError as error:
            print(error)
            continue

    for folder in os.listdir('./'):  # display a button for each folder found
        if os.path.isdir(folder) and n < 120:
            launch_func = partial(create, folder, n)
            createbu = Button(a, text=folder, command=launch_func, activebackground='#a9ff99', width=30)
            createbu.grid(row=create_row[n], column=create_col[n])
            create_list.append(createbu)
            n += 1

    if i > 40 or n > 40:  # creates a big exit button and make the window fullscreen as it was too tiny to display all buttons
        exitbu2 = Button(a, text=language[38], command=a.quit, activebackground='#d9ff8c', bg='#d9ff8c', fg='#ff2222', width=58, height=3, font=100)
        exitbu2.grid(row=0, column=4, rowspan=2, columnspan=3)
        a.attributes('-fullscreen', True)


def change_directory():  # enter button to change directory (take the entry content)
    cwd = entry_dir.get()
    if cwd == '':
        cwd = os.getcwd()
    else:
        cwd_label.configure(text=cwd)
    entry_dir.delete(0, 'end')
    os.chdir(cwd)
    scan_directory()


def open_explorer():  # change directory with C:\Windows\explorer.exe GUI
    new_cwd = askdirectory(initialdir=os.getcwd())
    os.chdir(new_cwd)
    cwd_label.configure(text=new_cwd)
    scan_directory()


def checkbu_rm_update():  # trigerred each time the checkbutton is pressed
    with open('C:\\Yosh\\a', 'r+b') as conf:
        conf.seek(15)
        mode = conf.read(1)
        conf.seek(15)
        if mode == b'1':
            conf.write(b'0')
        else:
            conf.write(b'1')


text_label = Label(a, text=language[29], bg='#aaffaa', width=30)
text_label.grid(row=0, column=0)

cwd_label = Label(a, text=os.getcwd(), bg='#aaffaa', width=60, anchor='w')
cwd_label.grid(row=0, column=1, columnspan=2)

entry_dir = Entry(a, width=30)
entry_dir.grid(row=1, column=1)

refreshbu = Button(a, text=language[40], command=change_directory, activebackground='#ff9999', width=30)
refreshbu.grid(row=1, column=2)

open_explorerbu = Button(a, text=language[30], command=open_explorer, activebackground='#96c7ff', width=15)
open_explorerbu.grid(row=1, column=0)

cb_rm_update = Checkbutton(a, text=language[100], command=checkbu_rm_update, bg="#aaffaa", width=20)
cb_rm_update.grid(row=0, column=3)

lcompression = Label(a, text=f'{language[101]} ->             ', bg='#aaffaa', width=30)
lcompression.grid(row=16, column=1, columnspan=2)

compression = ('iso', 'ciso', 'wbfs')
COMPRESSION = StringVar()
COMPRESSION.set(compression[2])
Compression = OptionMenu(a, COMPRESSION, *compression)
Compression["menu"].config(bg="#000000", fg='#ffffff')
Compression.config(width=7)
Compression.grid(row=16, column=2)

lextract = Label(a, text=language[41], font=500, bg='#aaffaa', height=3)
lextract.grid(row=2, column=0, rowspan=2)

lextract2 = Label(a, text=language[102], font=500, bg='#aaffaa', height=3)
lextract2.grid(row=2, column=1, rowspan=2, columnspan=2)

lcreate = Label(a, text=language[44], font=500, bg='#aaffaa')
lcreate.grid(row=16, column=0)

with open('C:\\Yosh\\a', 'rb') as config:
    config.seek(15)
    remove_update = config.read(1)
if remove_update == b'1':
    Checkbutton.select(cb_rm_update)

scan_directory()
a.mainloop()
