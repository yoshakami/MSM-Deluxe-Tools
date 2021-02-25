import os
from functools import partial
from tkinter import Tk, Button, Label, END, Entry
from tkinter.filedialog import askopenfilename, askdirectory

a = Tk()
a.title('Mario Sports Mix Modding mdl/bin/cmp/mot files extract and compress')
a.minsize(660, 440)
a.config(bg='#dfffaa')
a.iconbitmap('C:\\Yosh\\lh.ico')

thrice = [b'U\xaa8-', b'bres', b'\x00 \xaf0']  # arc, brres, and tpl files
twice = thrice[:2]
extensions = ['.mdl', '.bin', '.cmp']  # extensions of compressed files recognized
burow_extract = [6, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10] + [6, 7, 8, 9, 10] * 5 + [11] * 8 + [12] * 8 + [13] * 8 + [14] * 8 + [15] * 8 + [16] * 8 + [17] * 8
bucolumn = [0] + [0, 1, 2] * 5 + [3] * 5 + [4] * 5 + [5] * 5 + [6] * 5 + [7] * 5 + [0, 1, 2, 3, 4, 5, 6, 7] * 7
burow_compress = [burow_extract[i] + 16 for i in range(len(burow_extract))]

button_list = [0]
button_list2 = [0]


def scan_directory():
    for tkstuff in a.winfo_children():
        if tkstuff not in [text_label, cwd_label, entry_dir, refreshbu, exitbu, open_explorerbu]:
            tkstuff.destroy()

    def extract_all():  # extract all lh-compressed files in current directory
        for lh_file in os.listdir('./'):
            if os.path.isfile(lh_file) and os.path.getsize(lh_file) > 4:
                with open(lh_file, 'rb') as file:
                    lh_header = file.read(1)
                if lh_header == b'@':  # all files with lh compression starts with @
                    os.system(f'n "{lh_file}" -x')

        extract_allbu.destroy()

    def extract_type(ext, tkbu):  # ext is either .bin, .mdl, .cmp, or .mot
        for ext_file in os.listdir('./'):
            if os.path.isfile(ext_file) and os.path.getsize(ext_file) > 4:
                with open(ext_file, 'rb') as check_ext_file:
                    mdl_header = check_ext_file.read(1)
                if mdl_header == b'@' and os.path.splitext(ext_file)[1] == ext:
                    os.system(f'n "{ext_file}" -x')
        tkbu.destroy()

    def compress_all():  # compress all files in current directory
        for uncomp_file in os.listdir('./'):
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
        for j in range(3):
            if f"{shortname}{extensions[j]}" != cfile:  # don't delete the file the script will compress!
                os.system(
                    f'del "{shortname}{extensions[j]}"')  # delete the mdl, cmp, or bin file with the same name as the
        if ismodel:  # future compressed file if it exists  ( == overwrite )
            os.system(f'n "{cfile}" -lh -o "{shortname}.mdl"')  # create a compressed file with mdl extension
        elif iscmp:
            os.system(f'n "{cfile}" -lh -o "{shortname}.cmp"')
        else:
            os.system(f'n "{cfile}" -lh -o "{shortname}.bin"')
        manual_entry.delete(0, END)

    def explorer_compress():
        expfile = askopenfilename(initialdir=cwd)
        compressing_file = expfile.replace('/', '\\')
        compress(compressing_file)

    def explorer_extract():
        b = askopenfilename(initialdir=cwd)
        b = b.replace('/', '\\')
        os.system(f'n "{b}" -x')

    def extract_file(file, number):
        os.system(f'n "{file}" -x')
        button_list[number].destroy()

    def compress_file(brres, num):
        compress(brres)
        button_list2[num].destroy()

    file_extract_label = Label(a, text='file extract', font=300, bg='#dfffaa', height=2, width=45)
    file_extract_label.grid(row=2, columnspan=20)
    extract_allbu = Button(a, text='extract all files', activebackground='#ff7373', command=extract_all, width=30)
    extract_allbu.grid(row=4, column=0)

    extract_mdlbu = Button(a, text='extract all mdl', activebackground='#cf7dff', width=30)
    extract_mdl = partial(extract_type, '.mdl', extract_mdlbu)
    extract_mdlbu.config(command=extract_mdl)
    extract_mdlbu.grid(row=4, column=1)

    extract_binbu = Button(a, text='extract all bin', activebackground='#8afff3', width=30)
    extract_bin = partial(extract_type, '.bin', extract_binbu)
    extract_binbu.config(command=extract_bin)
    extract_binbu.grid(row=4, column=2)

    explorer_extractbu = Button(a, text='Open file explorer', activebackground='#96c7ff', command=explorer_extract, width=30)
    explorer_extractbu.grid(row=5, column=0)

    extract_cmpbu = Button(a, text='extract all cmp', activebackground='#ff70ec', width=30)
    extract_cmp = partial(extract_type, '.cmp', extract_cmpbu)
    extract_cmpbu.config(command=extract_cmp)
    extract_cmpbu.grid(row=5, column=1)

    extract_motbu = Button(a, text='extract all mot', activebackground='#ffff7f', width=30)
    extract_mot = partial(extract_type, '.mot', extract_motbu)
    extract_motbu.config(command=extract_mot)
    extract_motbu.grid(row=5, column=2)

    i = 0
    for file_to_extract in os.listdir('./'):
        size = os.path.getsize(file_to_extract)
        if os.path.isfile(file_to_extract) and size > 4 and i < 96:
            with open(file_to_extract, 'rb') as check_xfile:
                header = check_xfile.read(1)
            if header == b'@':
                i += 1
                run_extract_file = partial(extract_file, file_to_extract, i)
                temp = Button(a, text=file_to_extract, command=run_extract_file, activebackground='#a9ff99', width=30)
                temp.grid(row=burow_extract[i], column=bucolumn[i])
                button_list.append(temp)
    file_compress_label = Label(a, text='file compress', font=300, bg='#dfffaa', height=2)
    file_compress_label.grid(row=18, columnspan=20)

    manual_explorerbu = Button(a, text='Open file explorer', command=explorer_compress, activebackground='#ffc773', width=30)
    manual_explorerbu.grid(row=21, column=0)

    manual_label = Label(a, text='Manual Compress ->', bg='#dfffaa', width=30)
    manual_label.grid(row=20, column=0)

    manual_entry = Entry(a, width=30)
    manual_entry.grid(row=20, column=1)

    manual_button = Button(a, text='Compress', activebackground='#a9ff91', width=30)
    manual_compress = partial(compress, manual_entry.get())
    manual_button.config(command=manual_compress)
    manual_button.grid(row=20, column=2)

    compress_all_filesbu = Button(a, text='compress all files', command=compress_all, activebackground='#ff8c8c', width=61)
    compress_all_filesbu.grid(row=21, column=1, columnspan=2)

    i = 0
    for file_to_compress in os.listdir('./'):
        size = os.path.getsize(file_to_compress)
        if os.path.isfile(file_to_compress) and size > 4 and i < 96:
            with open(file_to_compress, 'rb') as check_cfile:
                header4 = check_cfile.read(4)
            if header4 in thrice:
                i += 1
                run_compress_file = partial(compress_file, file_to_compress, i)
                temp2 = Button(a, text=file_to_compress, command=run_compress_file, activebackground='#a9ff91', width=30)
                temp2.grid(row=burow_compress[i], column=bucolumn[i])
                button_list2.append(temp2)


def change_directory():  # enter button to change directory (take the entry content)
    entry_cwd = entry_dir.get()
    if entry_cwd == '':
        entry_cwd = os.getcwd()
    else:
        cwd_label.configure(text=entry_cwd)
    entry_dir.delete(0, END)
    os.chdir(entry_cwd)
    scan_directory()


def open_explorer():  # change directory with C:\Windows\explorer.exe GUI
    new_cwd = askdirectory(initialdir=os.getcwd)
    os.chdir(new_cwd)
    cwd_label.configure(text=new_cwd)
    scan_directory()


cwd = os.getcwd()
text_label = Label(a, text='Current working directory is', bg='#dfffaa', width=30)
text_label.grid(row=0, column=0)
cwd_label = Label(a, text=cwd, bg='#dfffaa', width=30)
cwd_label.grid(row=1, column=0)
entry_dir = Entry(a, width=30)
entry_dir.grid(row=1, column=1)
refreshbu = Button(a, text='Enter', command=change_directory, activebackground='#ff9999', width=30)
refreshbu.grid(row=1, column=2)
exitbu = Button(a, text='Exit', command=a.quit, activebackground='#d9ff8c', width=15)
exitbu.grid(row=0, column=2)
open_explorerbu = Button(a, text='Open file Explorer', command=open_explorer, activebackground='#96c7ff', width=15)
open_explorerbu.grid(row=0, column=1)
scan_directory()
a.mainloop()
