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
cmn = int(language[1].split(":")[33])
a = Tk()
a.title(language[start])
a.minsize(660, 440)
a.config(bg='#dfffaa')
ico = os.path.join('msm_stuff', 'lh.ico')
a.iconbitmap(os.path.join(install_dir, ico))
print(language[cmn + 9])
print(language[cmn + 10])
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
brres_list = ["a", "b",
              "md_shootcircle01.brres",
              "Coin.brres",
              "CockpitCoin.brres",  # (same as Coin)
              "StarPiece.brres",  # (coin models from st16)
              "IB00.brres",  # (Minishroom ball transformation)
              "IB01.brres",  # (Banana ball transformation)
              "IB02.brres",  # (Bob-Omb ball transformation)
              "IB03.brres",  # (Green Shell ball transformation)
              "IB04.brres",  # (Red Shell ball transformation)
              "IB07.brres",  # (Star ball transformation)
              "IT01_Toadstool.brres",  # (Minishroom item)
              "IT02_Star.brres",
              "IT04_Banana.brres",
              "IT05_Bomb.brres",
              "IT06_GShell.brres",
              "IT07_RShell.brres",
              "qpanel_h.brres",  # (question pannel, stop pannel from st03 and reverse pannel from st09)
              "qpanel_s10.brres",
              "Marker.brres",  # (contains 47 models for all languages "P1", "P2"... circle on the ground and star shape)
              "score.brres",  # (3D model of figures)
              "Shadow.brres",
              "wipe.brres"]

def scan_directory():
    del compress_list[:]
    del extract_list[:]
    for tkstuff in a.winfo_children():
        if tkstuff not in [text_label, cwd_label, entry_dir, refreshbu, open_explorerbu]:
            tkstuff.destroy()

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

    def extract(cmn):
        try:
            data = b''
            data2 = b''
            cmn_dir = os.path.splitext(cmn)[0].split('_DECOMP')[0] + "_extracted"
            while os.path.exists(cmn_dir):
                cmn_dir += "_new"
            os.makedirs(cmn_dir)
            previous = 0
            brres_count = 0
            with open(cmn, "rb") as bina:
                data = bina.read()
            if data[:4] != b'bres':
                os.system(f'{n} "{cmn}" -x')
                cmn = os.path.splitext(cmn)[0] + '_DECOMP.bin'
            for i in range(0, len(data), 16):
                if data[i:i + 4] == b'bres':
                    print(i)
                    brres_count += 1
                    with open(cmn_dir + "/" + brres_list[brres_count], "wb") as brres:
                        brres.write(data[previous:i])
                    previous = i
            brres_count += 2
            with open(cmn_dir + "/" + brres_list[-1], "wb") as brres:
                brres.write(data[previous:i])
            print(brres_count)
            if brres_count != 22:
                raise IndexError
        except IndexError:
            print("not_cmn_test.bin!")
        print(f"extracted {brres_count - 2} files!\npress enter to exit...")
    
    def explorer_compress():
        compressing_file = askopenfilename(initialdir=cwd)
        compress(compressing_file)

    def explorer_extract():
        file = askopenfilename(initialdir=cwd)
        extract(file)

    def extract_file(file, number):
        extract(file)
        extract_list[number].destroy()
        patched = Label(a, text=language[arc + 1], bg='#dfffaa', width=30)
        patched.grid(row=burow_extract[number], column=bucolumn[number])

    def compress_file(brres, num):
        compress(brres)
        compress_list[num].destroy()
        patched = Label(a, text=language[arc + 1], bg='#dfffaa', width=30)
        patched.grid(row=burow_extract[num], column=bucolumn[num])

    patched = Label(a, text=language[arc + 1], bg='#dfffaa', width=30)
    patched.grid(row=5, column=0)
    file_extract_label = Label(a, text=language[cmn + 5], font=300, bg='#dfffaa', height=2, width=45)
    file_extract_label.grid(row=2, columnspan=20)

    explorer_extractbu = Button(a, text=language[msm + 19], activebackground='#96c7ff', bg='#c4e0ff', command=explorer_extract, width=87)
    explorer_extractbu.grid(row=5, column=0, columnspan=3)

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

    cmn_repack_label = Label(a, text=language[cmn + 6], font=300, bg='#dfffaa', height=2)
    cmn_repack_label.grid(row=18, columnspan=20)

    manual_explorerbu = Button(a, text=language[msm + 19], command=explorer_compress, activebackground='#ffc773', bg='#ffe4bd', width=87)
    manual_explorerbu.grid(row=21, column=0, columnspan=3)

    manual_label = Label(a, text=language[cmn + 7], bg='#dfffaa', width=30)
    manual_label.grid(row=20, column=0)

    manual_entry = Entry(a, width=30)
    manual_entry.grid(row=20, column=1)

    manual_button = Button(a, text=language[cmn + 8], activebackground='#a9ff91', bg='#c9ffba', width=30)
    manual_compress = partial(compress, manual_entry.get())
    manual_button.config(command=manual_compress)
    manual_button.grid(row=20, column=2)

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
