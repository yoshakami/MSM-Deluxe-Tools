import os, struct, subprocess
from tkinter import Tk, Label, Button, END, Entry
from tkinter.filedialog import askdirectory
from functools import partial

a = Tk()
a.title('Mario Sports Mix Modding Change root bone attributes')
a.minsize(660, 440)
a.config(bg='#bfaaff')
a.iconbitmap('C:\\Yosh\\attrib.ico')


def hex_float(number):
    num = b''
    value = 0
    w = hex(struct.unpack('<I', struct.pack('<f', float(number)))[0])[2:]
    while len(w) < 8:
        value+=1
    w = '0' * value + w
    for octet in range(0, 8, 2):
        num += bytes(chr(int(w[octet:(octet + 2)], 16)), 'latin-1')
    return num


button_row = []
for m in range(7, 99):
    for _ in range(7):
        button_row.append(m)

button_col = [0, 1, 2, 3, 4, 5, 6] * 99
label_list = []


def scan_directory():
    for tkstuff in a.winfo_children():
        if tkstuff not in forstuff:
            tkstuff.destroy()
    button_list = []
    mdl_list = []

    def change_scale(file, offset):
        for y in range(12):
            if not entries[y].get().lstrip('-').replace('.', '', 1).isdigit():
                entries[y].config(bg='#ffaaaa')
                pass
        j = mdl_list[offset]
        done = False

        default_scale = hex_float(entries[0].get()) + hex_float(entries[1].get()) + hex_float(entries[2].get())
        with open(file, "r+b") as mdlo:
            while j < os.path.getsize(file) - 20:
                j += 1
                mdlo.seek(j)
                if mdlo.read(12) == default_scale:
                    mdlo.seek(j)
                    x = b''
                    for u in range(3, 12):
                        x += hex_float(entries[u].get())
                    mdlo.write(x)
                    j = os.path.getsize(file)
                    done = True
        button_list[offset].destroy()
        if done:
            patched = Label(a, text=f"Done! :)", bg='#bfaaff', width=30)
            patched.grid(row=button_row[offset], column=button_col[offset])
        else:
            notpatched = Label(a, text=f"oof! check help", fg='#0050ff', bg='#bfaaff', width=30)
            notpatched.grid(row=button_row[offset], column=button_col[offset])

    mdl = mdln = 0
    for files in os.listdir('./'):
        if mdl > 800:
            break
        size = os.path.getsize(files)
        if os.path.isfile(files) and size > 4:
            with open(files, 'rb') as bfile:
                cursor = 0
                header = bfile.read(4)
                if header == b'MDL0':
                    edit = partial(change_scale, files, mdl)
                    filebu = Button(a, text='MDL0 ' + files, command=edit, activebackground='#a9ff99', width=30,
                                    fg='#0050ff')
                    filebu.grid(row=button_row[mdl], column=button_col[mdl])
                    button_list.append(filebu)
                    mdl_list.append(0)
                    mdln += 1
                    mdl += 1
                elif header in [b'U\xaa8-', b'bres']:
                    new = 0
                    while cursor < size:
                        bfile.seek(cursor)
                        mdl0 = bfile.read(4)
                        if mdl0 == b'MDL0':
                            mdl_list.append(cursor)
                            new += 1
                        cursor += 16
                    if not new:
                        continue
                    out = subprocess.check_output(['wszst', 'list', files, '-R'])
                    first = True
                    filabel = Label(a, text=files, bg='#bfaaff', font=2, fg='#ff2222', width=19)
                    filabel.grid(row=button_row[mdl], column=button_col[mdl])
                    mdl += 1
                    for k in range(len(out) - 17):
                        if out[k:k + 5] == b'brres':
                            if first:
                                first = False
                            else:
                                count = 1
                                while b'\n' not in out[k - count:k]:
                                    count += 1
                                flabel = Label(a, text=str(out[k - count + 1:k + 5])[2:-1] + " ->", bg='#bfaaff',
                                               fg='#2222ff', width=30)
                                flabel.grid(row=button_row[mdl], column=button_col[mdl])
                                mdl += 1
                        elif out[k:k + 15] == b'3DModels(NW4R)/' and out[k + 15:k + 16] != b'\n':
                            z = 0
                            while b'\n' not in out[k + 15:k + z]:
                                z += 1
                            edit = partial(change_scale, files, mdln)
                            filebu = Button(a, text=str(out[k + 15:k + z])[2:-3], command=edit,
                                            activebackground='#a9ff99', width=30)
                            filebu.grid(row=button_row[mdl], column=button_col[mdl])
                            button_list.append(filebu)
                            mdl += 1
                            mdln += 1
    if mdln > 7:
        exitbu2 = Button(a, text='Exit', command=a.quit, activebackground='#d9ff8c', bg='#d9ff8c', fg='#ff2222',
                         width=58, height=3, font=100)
        exitbu2.grid(row=0, column=4, rowspan=2, columnspan=3)
        a.attributes('-fullscreen', True)


def change_directory():
    cwd = entry_dir.get()
    if cwd == '':
        cwd = os.getcwd()
    else:
        forstuff[1].configure(text=cwd)
    entry_dir.delete(0, END)
    os.chdir(cwd)
    scan_directory()


def open_explorer():
    new_cwd = askdirectory(initialdir=os.getcwd())
    os.chdir(new_cwd)
    forstuff[1].configure(text=new_cwd)
    scan_directory()


ltxt = ['Current working directory is', os.getcwd(), 'default scale', 'custom scale', 'custom rotation',
        'custom translation']
forstuff = []
entries = []
entrow = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]
for n in range(6):
    text = Label(a, text=ltxt[n], bg='#bfaaff', width=30)
    text.grid(row=n, column=0)
    forstuff.append(text)
for indice in range(12):
    entree = Entry(a, width=15)
    entree.grid(row=entrow[indice], column=indice % 3 + 1)
    if indice < 6:
        entree.insert(0, '1.0')
    else:
        entree.insert(0, '0.0')
    entries.append(entree)
forstuff += entries

entry_dir = Entry(a, width=30)
entry_dir.grid(row=1, column=1)
refreshbu = Button(a, text='Enter', command=change_directory, activebackground='#ff9999', width=30)
refreshbu.grid(row=1, column=2)
exitbu = Button(a, text='Exit', command=a.quit, activebackground='#d9ff8c', width=15)
exitbu.grid(row=0, column=2)
open_explorerbu = Button(a, text='Open file Explorer', command=open_explorer, activebackground='#96c7ff', width=15)
open_explorerbu.grid(row=0, column=1)
slash_n = Label(a, text='', bg='#bfaaff')
slash_n.grid(row=6)
dot = Label(a, text='USE DOTS\nNO COMA', bg='#bfaaff', font=2, fg='#ff2222')
dot.grid(row=0, column=3, rowspan=2)
forstuff += [entry_dir, refreshbu, exitbu, open_explorerbu, slash_n, dot]
scan_directory()
a.mainloop()
