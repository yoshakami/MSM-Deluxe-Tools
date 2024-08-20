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
hashtag = int(language[1].split(":")[3])
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

burow_repack = [burow_extract[i] + 16 for i in range(len(burow_extract))]

extract_list = []
repack_list = []
brres_list = ["Coin.brres", "Coin.brres",
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
              "qpanel_h.brres",  # (question panel, stop panel from st03 and reverse panel from st09)
              "qpanel_s10.brres", # (question panel from Bowser Jr. Boulevard)
              "Marker.brres",  # (contains 47 models for all languages "P1", "P2"... circle on the ground and star shape)
              "score.brres",  # (3D model of figures)
              "Shadow.brres",
              "wipe.brres"]
brres_len = [0, 0, 0,
             11392,
             38528,
             65664,
             90880,
             134400,
             215168,
             251008,
             290304,
             329600,
             393088,
             453632,
             487424,
             575104,
             664448,
             715904,
             767360,
             950912,
             991360,
             1352832,
             1484800,
             1490048,
             0x193F7F]

def scan_directory():
    del repack_list[:]
    del extract_list[:]
    for tkstuff in a.winfo_children():
        if tkstuff not in [text_label, cwd_label, entry_dir, refreshbu, open_explorerbu]:
            tkstuff.destroy()

    def repack(cmn_dir):  # compress cfile
        brres_content = b""
        if not os.path.exists(cmn_dir):
            cmn_dir = input("drag and drop cmn_test_extracted in this window then press enter\n")
        if not os.path.exists(cmn):
            cmn = input("drag and drop cmn_test_DECOMP.bin in this window then press enter\n")
        with open(cmn, "r+b") as file:
            for i in range(3, len(brres_list)):
                if not os.path.exists(cmn_dir + "/" + brres_list[i]):
                    print(f"cannot find file, skipping {brres_list[i]}")
                    continue
                file.seek(brres_len[i])
                if brres_len[i] + os.path.getsize(cmn_dir + "/" + brres_list[i]) > brres_len[i + 1]:
                    print(f"{brres_list[i]}'s file size has changed. skipping")
                    continue
                with open(cmn_dir + "/" + brres_list[i], "rb") as brres:
                    brres_content = brres.read()
                file.write(brres_content)
        print(f"rebuilt file!\npress enter to exit...")
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
            if data.count(b'bres') != 22:
                raise IndexError
            if data[:4] != b'bres':
                os.system(f'{n} "{cmn}" -x')
                cmn = os.path.splitext(cmn)[0] + '_DECOMP.bin'
            for i in range(0, len(data), 16):
                if data[i:i + 4] == b'bres':
                    print(i, brres_count, brres_list[brres_count])
                    brres_count += 1
                    with open(cmn_dir + "/" + brres_list[brres_count], "wb") as brres:
                        brres.write(data[previous:i])
                    previous = i
            with open(cmn_dir + "/" + brres_list[-1], "wb") as brres:
                brres.write(data[previous:i])
            print(brres_count)
        except IndexError:
            return language[cmn + 11]
        return language[hashtag + 16].replace('#', brres_count)
    
    def explorer_repack():
        repack_dir = askdirectory(initialdir=cwd, title="Select a directory to repack")
        repack(repack_dir)

    def explorer_extract():
        file = askopenfilename(initialdir=cwd)
        print(extract(file))

    def extract_file(file, number):
        label_text = extract(file)
        extract_list[number].destroy()
        patched = Label(a, text=label_text, bg='#dfffaa', width=30)
        patched.grid(row=burow_extract[number], column=bucolumn[number])

    def repack_file(brres, num):
        repack(brres)
        repack_list[num].destroy()
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
                if header[:1] in [b'@', b'\x10', b'\x11', b'\x81', b'\x82', b'$', b'(', b'0', b'P', b'b'] and header != b'PK\x03\x04':  # lh @, old lz \x10, lz77 \x11, diff8 \x81, diff16 \x82, huff4 $, huff8 (, runlength 0, lrc P
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

    manual_explorerbu = Button(a, text=language[msm + 19], command=explorer_repack, activebackground='#ffc773', bg='#ffe4bd', width=87)
    manual_explorerbu.grid(row=21, column=0, columnspan=3)

    manual_label = Label(a, text=language[cmn + 7], bg='#dfffaa', width=30)
    manual_label.grid(row=20, column=0)

    manual_entry = Entry(a, width=30)
    manual_entry.grid(row=20, column=1)

    manual_button = Button(a, text=language[cmn + 8], activebackground='#a9ff91', bg='#c9ffba', width=30)
    manual_repack = partial(repack, manual_entry.get())
    manual_button.config(command=manual_repack)
    manual_button.grid(row=20, column=2)

    i = 0
    for dir_to_repack in os.listdir('./'):
        try:
            if os.path.isdir(dir_to_repack):
                cmn_dir = os.listdir(dir_to_repack)
                this_is_a_cmn_dir = True
                for brres in brres_list:
                    if brres not in cmn_dir:
                        this_is_a_cmn_dir = False
                        break
                if not this_is_a_cmn_dir or i >= len(bucolumn):
                    continue
                run_repack_file = partial(repack_file, dir_to_repack, i)
                temp2 = Button(a, text=dir_to_repack, command=run_repack_file, activebackground='#a9ff91', width=30)
                temp2.grid(row=burow_repack[i], column=bucolumn[i])
                repack_list.append(temp2)
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
