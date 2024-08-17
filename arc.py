import os
from tkinter import Tk, Label, Button, END, Entry, OptionMenu, StringVar
from tkinter.filedialog import askdirectory, askopenfilename
from functools import partial
install_dir = os.path.dirname(os.path.abspath(__file__))
if ':\\Windows' in os.getcwd():  # prevents the tool to run on system32 if launched from start menu
    os.chdir(os.environ['userprofile'] + '\\Desktop')

with open(os.path.join(install_dir, '#language.txt'), 'r', encoding="utf-8") as txt:
    language = txt.read()
    language = [''] + language.splitlines()

start = int(language[1].split(":")[7])
msm = int(language[1].split(":")[1])
extract_row = []
for j in range(6, 18):
    extract_row += [j, j, j, j]
for j in range(6, 18):
    extract_row += [j, j, j]
extract_col = [0, 1, 2, 3] * 12 + [4, 5, 6] * 12

create_row = []
for j in range(20, 32):
    create_row += [j, j, j, j]
for j in range(20, 32):
    create_row += [j, j, j]
create_col = [0, 1, 2, 3] * 12 + [4, 5, 6] * 12

extract_list = []
create_list = []
a = Tk()
a.title(language[start])
a.minsize(880, 440)
a.config(bg='#aacfff')
ico = os.path.join('msm_stuff', 'arc.ico')
a.iconbitmap(os.path.join(install_dir, ico))


def extract_all():
    for stuff in os.listdir('./'):
        os.system(f'wszst x "{stuff}" -o')
    extract_allbu.destroy()
    patched = Label(a, text=language[start + 1], bg='#aacfff', width=30)
    patched.grid(row=1, column=3)


def explorer_extract():
    binary_file = askopenfilename(initialdir=os.getcwd(), title='select a file to extract')  # explorer.exe file selection GUI
    os.system(f'wszst x "{binary_file}" -o')


def explorer_create():  # triggered by the "Open File Explorer" button
    directory = askdirectory(initialdir=os.getcwd(), title='select a folder to pack')  # explorer.exe folder selection GUI
    comp = COMPRESSION.get()  # get the compression the user has set in the option menu
    arch = ARCHIVE.get()  # get the archive file type the user has set in the option menu
    destfile = os.path.splitext(directory)[0]
    if comp == ' ' and arch == 'u8':
        os.system(f'wszst c "{directory}" -d "{destfile}.arc" --u8 --no-compress -o')

    elif comp == 'bz' and arch == 'wu8':
        os.system(f'wszst c "{directory}" -d "{destfile}.wbz" --wbz -o')

    elif comp == 'yaz0' and arch == 'u8':
        os.system(f'wszst c "{directory}" -d "{destfile}.szs" --szs -o')

    elif comp == ' ':
        os.system(f'wszst c "{directory}" -d "{destfile}.{arch}" --{arch} --no-compress -o')

    else:
        os.system(f'wszst c "{directory}" -d "{destfile}.{arch}" --{arch} --{comp} -o')


def scan_directory():  # triggered each time Enter button / Open File Explorer button is pressed (or when you launch the script)
    def create(name, ref):
        compr = COMPRESSION.get()
        archi = ARCHIVE.get()
        name2 = os.path.splitext(name)[0]
        if compr == ' ' and archi == 'u8':
            os.system(f'wszst c "{name}" -d "{name2}.arc" --u8 --no-compress -o')

        elif compr == 'bz' and archi == 'wu8':
            os.system(f'wszst c "{name}" -d "{name2}.wbz" --wbz -o')

        elif compr == 'yaz0' and archi == 'u8':
            os.system(f'wszst c "{name}" -d "{name2}.szs" --szs -o')

        elif compr == ' ':
            os.system(f'wszst c "{name}" -d "{name2}.{archi}" --{archi} --no-compress -o')

        else:
            os.system(f'wszst c "{name}" -d "{name2}.{archi}" --{archi} --{compr} -o')

        create_list[ref].destroy()
        if os.path.exists(f"{name2}.{archi}") or os.path.exists(f"{name2}.arc") or os.path.exists(f"{name2}.wbz") or os.path.exists(f"{name2}.szs"):
            patched = Label(a, text=language[start + 1], bg='#aacfff', width=30)
        else:
            patched = Label(a, text='oof! check folder permissions', bg='#aacfff', width=30)
        patched.grid(row=create_row[ref], column=create_col[ref])

    def extract(file, index):
        os.system(f'wszst x "{file}" -o')
        extract_list[index].destroy()
        patched = Label(a, text=language[start + 1], bg='#aacfff', width=30)
        patched.grid(row=extract_row[index], column=extract_col[index])

    i = n = 0
    del create_list[:]
    del extract_list[:]
    for tkstuff in a.winfo_children():
        if tkstuff not in [text_label, open_explorerbu, brawlcrate, cwd_label, entry_dir, refreshbu, lextract, lextract2, extract_allbu, expextract, lcreate, larchive, lcompression, Compression, Archive, expcreate, lfiletypes]:
            tkstuff.destroy()

    for files in os.listdir('./'):  # display a button for each yaz0, yaz1, pack, breff, breft, arc or brres found
        try:
            if not os.path.isfile(files):
                continue
            size = os.path.getsize(files)
            if size < 5 or i >= len(extract_col):
                continue
            with open(files, 'rb') as check_file:
                header = check_file.read(4)
            if header in [b'Yaz0', b'Yaz1', b'PACK', b'REFF', b'REFT', b'U\xaa8-', b'bres']:
                launch_func = partial(extract, files, i)
                extractbu = Button(a, text=files, command=launch_func, activebackground='#a9ff99', width=30)
                extractbu.grid(row=extract_row[i], column=extract_col[i])
                extract_list.append(extractbu)
                i += 1

        except PermissionError as error:
            print(error)
            continue

    for folder in os.listdir('./'):  # display a button for each folder found
        if os.path.isdir(folder) and n < len(create_col):
            launch_func = partial(create, folder, n)
            createbu = Button(a, text=folder, command=launch_func, activebackground='#a9ff99', width=30)
            createbu.grid(row=create_row[n], column=create_col[n])
            create_list.append(createbu)
            n += 1

    if i > 40 or n > 40:  # creates a big exit button and make the window fullscreen as it was too tiny to display all buttons
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


text_label = Label(a, text=language[msm + 18], bg='#aacfff', width=30)
text_label.grid(row=0, column=0)

open_explorerbu = Button(a, text=language[msm + 19], command=open_explorer, activebackground='#96c7ff', width=15)
open_explorerbu.grid(row=1, column=0)

brawlcrate = Label(a, text=language[start + 2]+'\n'+language[start + 3], bg='#aacfff', width=30)
brawlcrate.grid(row=0, column=3, rowspan=2)

cwd_label = Label(a, text=os.getcwd(), bg='#aacfff', width=60)
cwd_label.grid(row=0, column=1, columnspan=2)

entry_dir = Entry(a, width=30)
entry_dir.grid(row=1, column=1)

refreshbu = Button(a, text=language[msm + 40], command=change_directory, activebackground='#ff9999', width=30)
refreshbu.grid(row=1, column=2)

lextract = Label(a, text=language[start + 4], font=500, bg='#aacfff', height=3)
lextract.grid(row=2, column=0, rowspan=2)

lextract2 = Label(a, text=language[start + 5], font=500, bg='#aacfff', height=3)
lextract2.grid(row=2, column=1, rowspan=2, columnspan=2)

extract_allbu = Button(a, text=language[start + 6], command=extract_all, activebackground='#ff9999', width=20)
extract_allbu.grid(row=2, column=3)

expextract = Button(a, text=language[msm + 19], command=explorer_extract, activebackground='#99ffee', width=20)
expextract.grid(row=3, column=3)

lcreate = Label(a, text=f'{language[start + 7]}           ', font=500, bg='#aacfff')
lcreate.grid(row=16, column=0)

larchive = Label(a, text=f'  {language[start + 8]}  ->', bg='#aacfff')
larchive.grid(row=16, column=0, columnspan=2)

lcompression = Label(a, text=f'              {language[start + 9]}  ->', bg='#aacfff')
lcompression.grid(row=16, column=1, columnspan=2)

archive = ('u8', 'wu8', 'pack', 'brres', 'breff', 'breft')
ARCHIVE = StringVar()
ARCHIVE.set(archive[0])
Archive = OptionMenu(a, ARCHIVE, *archive)
Archive["menu"].config(bg="#000000", fg="#ffffff")
Archive.grid(row=16, column=1)

compression = (' ', 'yaz0', 'yaz1', 'bz')
COMPRESSION = StringVar()
COMPRESSION.set(compression[0])
Compression = OptionMenu(a, COMPRESSION, *compression)
Compression["menu"].config(bg="#000000", fg='#ffffff')
Compression.grid(row=16, column=2)

expcreate = Button(a, text=language[msm + 19], command=explorer_create, activebackground='#99ffee', width=20)
expcreate.grid(row=17, column=0, sticky='w')

lfiletypes = Label(a, text=f'{language[start + 10]} -> u8 = arc | u8 + yaz0 = szs | wu8 + bz = wbz', bg='#aacfff', width=54)
lfiletypes.grid(row=17, column=1, columnspan=2)

scan_directory()
a.mainloop()
