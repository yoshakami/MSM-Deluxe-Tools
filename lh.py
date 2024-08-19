import os
from functools import partial
from tkinter import Tk, Button, Label, Entry
from tkinter.filedialog import askopenfilename, askdirectory

if ':\\Windows' in os.getcwd():
    os.chdir(os.environ['userprofile'] + '\\Desktop')

install_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(install_dir, '#language.txt'), 'r', encoding="utf-8") as txt:
    language = txt.read()
    language = [''] + language.splitlines()
    
n = os.path.join(install_dir, 'n.exe')

arc = int(language[1].split(":")[7])
start = int(language[1].split(":")[15])
msm = int(language[1].split(":")[1])
a = Tk()
a.title(language[start])
a.minsize(660, 440)
a.config(bg='#dfffaa')
ico = os.path.join('msm_stuff', 'lh.ico')
a.iconbitmap(os.path.join(install_dir, ico))

thrice = [b'U\xaa8-', b'bres', b'\x00 \xaf0', b'\x00\x00\x00\x00']  # arc, brres, tpl and rso files
twice = thrice[:2]
extensions = ['.mdl', '.bin', '.cmp']  # extensions of compressed files recognized
# burow_extract = [6, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10] + [6, 7, 8, 9, 10] * 5 + [11] * 8 + [12] * 8 + [13] * 8 + [14] * 8 + [15] * 8 + [16] * 8 + [17] * 8
# bucolumn = [0] + [0, 1, 2] * 5 + [3] * 5 + [4] * 5 + [5] * 5 + [6] * 5 + [7] * 5 + [0, 1, 2, 3, 4, 5, 6, 7] * 7
burow_extract = []
for j in range(6, 11):
    burow_extract += [j, j, j]
for j in range(6, 11):
    burow_extract += [j, j, j, j]
for j in range(11, 18):
    burow_extract += [j, j, j, j, j, j, j]

bucolumn = [0, 1, 2] * 5 + [3, 4, 5, 6] * 5 + [0, 1, 2, 3, 4, 5, 6] * 7

burow_compress = [burow_extract[i] + 16 for i in range(len(burow_extract))]

extract_list = []
compress_list = []

def scan_directory():
    del compress_list[:]
    del extract_list[:]
    for tkstuff in a.winfo_children():
        if tkstuff not in [text_label, cwd_label, entry_dir, refreshbu, open_explorerbu]:
            tkstuff.destroy()

    def extract_all():  # extract all lh-compressed files in current directory
        for lh_file in os.listdir('./'):
            if os.path.isfile(lh_file) and os.path.getsize(lh_file) > 4:
                with open(lh_file, 'rb') as file:
                    lh_header = file.read(1)
                if lh_header in [b'@', b'\x10', b'\x11', b'\x81', b'\x82', b'$', b'(', b'0', b'P']:  # lh @, old lz \x10, lz77 \x11, diff8 \x81, diff16 \x82, huff4 $, huff8 (, runlength 0, lrc P
                    os.system(f'{n} "{lh_file}" -x')
        extract_allbu.destroy()

    def extract_type(ext, tkbu):  # ext is either .bin, .mdl, .cmp, or .mot
        for ext_file in os.listdir('./'):
            if os.path.isfile(ext_file) and os.path.getsize(ext_file) > 4:
                with open(ext_file, 'rb') as check_ext_file:
                    mdl_header = check_ext_file.read(1)
                if mdl_header == b'@' and os.path.splitext(ext_file)[1] == ext:
                    os.system(f'{n} "{ext_file}" -x')
        tkbu.destroy()

    def compress_all():  # compress all files in current directory
        for uncomp_file in os.listdir('./'):
            if not os.path.isfile(uncomp_file):
                continue
            with open(uncomp_file, 'rb') as uncomp_check:
                if uncomp_check.read(4) not in thrice:
                    continue
            compress(uncomp_file)
        compress_all_filesbu.destroy()

    def compress(cfile):  # compress cfile
        ismodel = iscmp = False
        csize = cursor = os.path.getsize(cfile)
        if csize > 8 and os.path.isfile(cfile):
            if csize < 2222:  # if the size is very little, don't trigger the while, it's definitely not a mdl file
                cursor = -3333
            cursor -= 8  # cursor = csize - 8
            with open(cfile, 'rb') as cfile_check:
                if cfile_check.read(4) not in thrice:
                    return
                cfile_check.seek(0)
                if cfile_check.read(1) == b'\x00':
                    iscmp = True
                if not iscmp:  # if it's not a cmp, check whether it is a mdl or else a bin.
                    while cursor > csize - 2222:
                        cursor -= 1
                        cfile_check.seek(cursor)
                        data = cfile_check.read(7)
                        if data == b'\x06body_h':  # all mdl does have this text before their end (a mdl0 named body_h)
                            ismodel = True
                            break
        if '_' in cfile:
            shortname = cfile.rsplit('_', 1)[0]  # if there is a _ in the file name, everything after is just the extension
        elif '.' in cfile:
            shortname = os.path.splitext(cfile)[0]  # if there is a . in the file name
        else:
            shortname = cfile  # else compressed file name will be the file name + its right extension
        if ismodel:  # future compressed file if it exists  ( == overwrite )
            os.system(f'{n} "{cfile}" -lh -o "{shortname}.mdl" -A32')  # create a compressed file with mdl extension
        elif iscmp:
            os.system(f'{n} "{cfile}" -lh -o "{shortname}.cmp" -A32')
        else:
            os.system(f'{n} "{cfile}" -lh -o "{shortname}.bin" -A32')
        manual_entry.delete(0, 'end')

    def explorer_compress():
        compressing_file = askopenfilename(initialdir=cwd)
        compress(compressing_file)

    def explorer_extract():
        b = askopenfilename(initialdir=cwd)
        os.system(f'{n} "{b}" -x')

    def extract_file(file, number):
        os.system(f'{n} "{file}" -x')
        extract_list[number].destroy()
        patched = Label(a, text=language[arc + 1], bg='#dfffaa', width=30)
        patched.grid(row=burow_extract[number], column=bucolumn[number])

    def compress_file(brres, num):
        compress(brres)
        compress_list[num].destroy()
        patched = Label(a, text=language[arc + 1], bg='#dfffaa', width=30)
        patched.grid(row=burow_extract[num], column=bucolumn[num])

    patched = Label(a, text=language[arc + 1], bg='#dfffaa', width=30)
    patched.grid(row=4, column=0)
    patched = Label(a, text=language[arc + 1], bg='#dfffaa', width=30)
    patched.grid(row=4, column=1)
    patched = Label(a, text=language[arc + 1], bg='#dfffaa', width=30)
    patched.grid(row=4, column=2)
    patched = Label(a, text=language[arc + 1], bg='#dfffaa', width=30)
    patched.grid(row=5, column=0)
    patched = Label(a, text=language[arc + 1], bg='#dfffaa', width=30)
    patched.grid(row=5, column=1)
    patched = Label(a, text=language[arc + 1], bg='#dfffaa', width=30)
    patched.grid(row=5, column=2)
    file_extract_label = Label(a, text=language[start + 1], font=300, bg='#dfffaa', height=2, width=45)
    file_extract_label.grid(row=2, columnspan=20)
    extract_allbu = Button(a, text=language[start + 2], activebackground='#ff7373', bg='#ffb8b8', command=extract_all, width=30)
    extract_allbu.grid(row=4, column=0)

    extract_mdlbu = Button(a, text=language[start + 3], activebackground='#cf7dff', bg='#e2b0ff', width=30)
    extract_mdl = partial(extract_type, '.mdl', extract_mdlbu)
    extract_mdlbu.config(command=extract_mdl)
    extract_mdlbu.grid(row=4, column=1)

    extract_binbu = Button(a, text=language[start + 4], activebackground='#8afff3', bg='#bffff8', width=30)
    extract_bin = partial(extract_type, '.bin', extract_binbu)
    extract_binbu.config(command=extract_bin)
    extract_binbu.grid(row=4, column=2)

    explorer_extractbu = Button(a, text=language[msm + 19], activebackground='#96c7ff', bg='#c4e0ff', command=explorer_extract, width=30)
    explorer_extractbu.grid(row=5, column=0)

    extract_cmpbu = Button(a, text=language[start + 5], activebackground='#ff70ec', bg='#ffbdf6', width=30)
    extract_cmp = partial(extract_type, '.cmp', extract_cmpbu)
    extract_cmpbu.config(command=extract_cmp)
    extract_cmpbu.grid(row=5, column=1)

    extract_motbu = Button(a, text=language[start + 6], activebackground='#ffff7f', bg='#ffffc2', width=30)
    extract_mot = partial(extract_type, '.mot', extract_motbu)
    extract_motbu.config(command=extract_mot)
    extract_motbu.grid(row=5, column=2)

    p = 0
    for file_to_extract in os.listdir('./'):
        try:
            if os.path.isfile(file_to_extract):
                size = os.path.getsize(file_to_extract)
                if size < 5 or p >= len(bucolumn):
                    continue
                with open(file_to_extract, 'rb') as check_xfile:
                    header = check_xfile.read(4)
                if header[:1] in [b'@', b'\x10', b'\x11', b'\x81', b'\x82', b'$', b'(', b'0', b'P'] and header != b'PK\x03\x04':  # lh @, old lz \x10, lz77 \x11, diff8 \x81, diff16 \x82, huff4 $, huff8 (, runlength 0, lrc P
                    run_extract_file = partial(extract_file, file_to_extract, p)
                    temp = Button(a, text=file_to_extract, command=run_extract_file, activebackground='#a9ff99', width=30)
                    temp.grid(row=burow_extract[p], column=bucolumn[p])
                    extract_list.append(temp)
                    # print(file_to_extract, p)
                    p += 1

        except PermissionError as error:
            print(error)
            continue

    file_compress_label = Label(a, text=language[start + 7], font=300, bg='#dfffaa', height=2)
    file_compress_label.grid(row=18, columnspan=20)

    manual_explorerbu = Button(a, text=language[msm + 19], command=explorer_compress, activebackground='#ffc773', bg='#ffe4bd', width=30)
    manual_explorerbu.grid(row=21, column=0)

    manual_label = Label(a, text=f'{language[start + 8]} ->', bg='#dfffaa', width=30)
    manual_label.grid(row=20, column=0)

    manual_entry = Entry(a, width=30)
    manual_entry.grid(row=20, column=1)

    manual_button = Button(a, text=language[start + 9], activebackground='#a9ff91', bg='#c9ffba', width=30)
    manual_compress = partial(compress, manual_entry.get())
    manual_button.config(command=manual_compress)
    manual_button.grid(row=20, column=2)
    patched = Label(a, text=language[arc + 1], bg='#dfffaa', width=61)
    patched.grid(row=21, column=1, columnspan=2)
    compress_all_filesbu = Button(a, text=language[start + 10], command=compress_all, activebackground='#ff8c8c', bg='#ffc7c7', width=61)
    compress_all_filesbu.grid(row=21, column=1, columnspan=2)

    i = 0
    for file_to_compress in os.listdir('./'):
        try:
            if os.path.isfile(file_to_compress):
                size = os.path.getsize(file_to_compress)
                if size < 5 or i >= len(bucolumn):
                    continue
                with open(file_to_compress, 'rb') as check_cfile:
                    header4 = check_cfile.read(4)
                if header4 in thrice:
                    run_compress_file = partial(compress_file, file_to_compress, i)
                    temp2 = Button(a, text=file_to_compress, command=run_compress_file, activebackground='#a9ff91', width=30)
                    temp2.grid(row=burow_compress[i], column=bucolumn[i])
                    compress_list.append(temp2)
                    i += 1

        except PermissionError as error:
            print(error)
            continue
    if i > 50 or p > 50:  # creates a big exit button and make the window fullscreen as it was too tiny to display all buttons
        exitbu2 = Button(a, text=language[msm + 40], command=a.quit, activebackground='#d9ff8c', bg='#d9ff8c', fg='#ff2222', width=58, height=3, font=100)
        exitbu2.grid(row=0, column=4, rowspan=2, columnspan=3)
        a.attributes('-fullscreen', True)


def change_directory():  # enter button to change directory (take the entry content)
    entry_cwd = entry_dir.get()
    if entry_cwd == '':
        entry_cwd = os.getcwd()
    else:
        cwd_label.configure(text=entry_cwd)
    entry_dir.delete(0, 'end')
    os.chdir(entry_cwd)
    scan_directory()


def open_explorer():  # change directory with C:\Windows\explorer.exe GUI
    new_cwd = askdirectory(initialdir=os.getcwd)
    os.chdir(new_cwd)
    cwd_label.configure(text=new_cwd)
    scan_directory()


cwd = os.getcwd()
text_label = Label(a, text=language[msm + 18], bg='#dfffaa', width=30)
text_label.grid(row=0, column=0)
cwd_label = Label(a, text=cwd, bg='#dfffaa', width=60, anchor='w')
cwd_label.grid(row=0, column=1, columnspan=2)
entry_dir = Entry(a, width=30)
entry_dir.grid(row=1, column=1)
refreshbu = Button(a, text=language[msm + 40], command=change_directory, activebackground='#ff9999', width=30)
refreshbu.grid(row=1, column=2)
open_explorerbu = Button(a, text=language[msm + 19], command=open_explorer, activebackground='#96c7ff', width=15)
open_explorerbu.grid(row=1, column=0)
scan_directory()
a.mainloop()
