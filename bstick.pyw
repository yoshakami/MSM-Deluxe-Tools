# coding: latin-1
# ^ else every byte above 0x7f will be encoded in utf-8 (oof)
import os
import webbrowser
from functools import partial
from subprocess import Popen
from tkinter import Tk, Canvas, PhotoImage, Label, Button, Entry, Checkbutton
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askdirectory
from PIL import Image

if ':\\Windows' in os.getcwd():
    os.chdir(os.environ['userprofile'] + '\\Desktop')

with open('C:\\Yosh\\#language.txt', 'r', encoding="utf-8") as txt:
    language = txt.read()
    language = [''] + language.splitlines()

start = int(language[1].split(":")[7])
msm = int(language[1].split(":")[1])
a = Tk()
a.title(language[start])
a.minsize(660, 440)
a.config(bg='#aaaaff')
a.iconbitmap('C:\\Yosh\\msm_stuff\\bstick.ico')

button_row = []
for j in range(12, 26):
    button_row += [j, j, j]
button_col = [0, 1, 2] * 14
button_list = []


def fill_bytes_rgvb():
    with open('C:\\Yosh\\a', 'r+b') as ca:
        hex_colour = str(ca.read(7))[2:9]

        r = hex_colour[1:3]
        num = int(r, 16)
        temp = num - 128
        if temp < 0:
            temp = 0
        r8 = bytes(chr(temp), 'latin-1')
        r7 = bytes(hex(temp)[2:], 'latin-1')
        if len(r7) < 2:
            r7 = b'0' + r7
        r = bytes(chr(num), 'latin-1')

        g = hex_colour[3:4]
        temp = int(g, 16) - 8
        if temp < 0:
            temp = 0
        fa = bytes(str(temp), 'latin-1')
        w = bytes(chr(temp), 'latin-1')
        g = bytes(chr(int(g, 16)), 'latin-1')

        v = hex_colour[4:5]
        temp = int(v, 16) - 7
        if temp < 0:
            temp = 0
        fb = bytes(str(int(v, 16)), 'latin-1')
        u = bytes(chr(temp * 16), 'latin-1')
        v = bytes(chr(int(v, 16) * 16), 'latin-1')

        b = hex_colour[5:7]
        num = int(b, 16)
        temp = num - 128
        if temp < 0:
            temp = 0
        b8 = bytes(chr(temp), 'latin-1')
        b7 = bytes(hex(temp)[2:], 'latin-1')
        if len(b7) < 2:
            b7 = b'0' + b7
        b = bytes(chr(num), 'latin-1')
        ca.seek(12)
        cd = ca.read(1)
        if cd == b'1':
            r = r8
            g = w
            v = u
            b = b8
            hex_colour = f'#{r7}{fa}{fb}{b7}'
            ca.seek(1)
            ca.write(r7)
            ca.write(fa)
            ca.write(fb)
            ca.write(b7)
        ca.seek(7)
        ca.write(r)
        ca.write(g)
        ca.write(v)
        ca.write(b)
    colourbu.configure(text=hex_colour)


def change_file(name, index):  # changes the color in the brres or mdl0 given in argument
    with open(name, "r+b") as h:
        y = os.path.getsize(name)
        cursor = 0
        with open('C:\\Yosh\\a', 'r+b') as conf:
            conf.seek(7)
            r = conf.read(1)
            g = conf.read(3)
        while y - 49 > cursor:
            cursor = cursor + 16
            h.seek(cursor)
            data = h.read(34)
            if data == b'a\xf3?\x00\x00a@\x00\x00\x17a\xfe\x00\xff\xe3aA\x004\xa0aB\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00a\xe2':
                data = h.read(7)
                if data == b'\x00\x00\x00a\xe3\x00\x00':
                    continue
                h.seek(cursor + 36)
                h.write(r)
                h.seek(cursor + 39)
                h.write(g)
                h.seek(cursor + 44)
                h.write(g)
                h.seek(cursor + 49)
                h.write(g)
                break
    button_list[index].destroy()
    patched = Label(a, text=language[start + 1], bg='#aaaaff')
    patched.grid(row=button_row[index], column=button_col[index])


def scan_directory():
    do_not_delete = [entry_dir, text_label, cwd_label, refreshbu, open_explorerbu, title, lcolour,
                     colour_entry, colourbu, google_colorbu, preview, lred, lorange, lyellow, lchartreuse,
                     llight_green, lgreen, lgreen_cyan, lblue_cyan, lblue, lpurple, lfushia, lred_fushia,
                     empty, fix_colourcb, previewbu, lrestart, lwin,
                     lpreview1, lpreview2, lpreview3, lpreview4, lpreview5, lpreview6, lpreview7]
    for o in a.winfo_children():
        if o not in do_not_delete:
            o.destroy()

    i = -1
    for file in os.listdir('./'):
        if not os.path.isfile(file):
            continue
        size = cursor = os.path.getsize(file)
        if size < 2222:
            continue
        cursor -= 7
        try:
            with open(file, 'r+b') as binary:
                header = binary.read(4)
                if header in [b'bres', b'MDL0']:
                    while cursor > size - 2222:
                        cursor -= 1
                        binary.seek(cursor)
                        r = binary.read(7)
                        if r == b'\x06bstick':
                            i += 1
                            change_color = partial(change_file, file, i)
                            filebu = Button(a, text=file, command=change_color, activebackground='#a9ff91', width=30)
                            filebu.grid(row=button_row[i], column=button_col[i])
                            button_list.append(filebu)

        except PermissionError:
            continue


def change_bmp():
    with open('C:\\Yosh\\a', 'r+b') as conf:
        hex_colour = str(conf.read(7))[2:9]

    rt = hex_colour[1:3]
    temp = int(rt, 16) + 128
    if temp > 255:
        temp = 255
    r = bytes(chr(temp), 'latin-1')
    temp = int(199 + (temp - 128) * 39 / 127)
    if temp > 238:
        temp = 238
    rb = bytes(chr(temp), 'latin-1')

    gt = hex_colour[3:5]
    temp = int(gt, 16) + 128
    if temp > 255:
        temp = 255
    g = bytes(chr(temp), 'latin-1')
    temp = int(199 + (temp - 128) * 39 / 127)
    if temp > 238:
        temp = 238
    gb = bytes(chr(temp), 'latin-1')

    bt = hex_colour[5:7]
    temp = int(bt, 16) + 128
    if temp > 255:
        temp = 255
    b = bytes(chr(temp), 'latin-1')
    temp = int(199 + (temp - 128) * 39 / 127)
    if temp > 238:
        temp = 238
    bb = bytes(chr(temp), 'latin-1')

    colourbu.configure(text=hex_colour)
    with open('C:\\Yosh\\msm_stuff\\bstick.bmp', 'r+b') as bmp:
        ab = 397
        ae = b'\x00'
        bmp.seek(695)
        af = bmp.read(3)
        while ab < 195397:
            ab = ab + 3
            bmp.seek(ab)
            ac = bmp.read(3)
            bmp.seek(ab)
            if ac == b'\xfa\xe6\xe6':
                continue
            elif ae in ac:
                ab = ab - 2
                continue
            elif ac == af:
                bmp.write(b)
                bmp.write(g)
                bmp.write(r)
            else:
                bmp.write(bb)
                bmp.write(gb)
                bmp.write(rb)
    bstick_image = Image.open('C:\\Yosh\\msm_stuff\\bstick.bmp')
    bstick_image.save('C:\\Yosh\\msm_stuff\\bstick.png')
    bstick_image.close()
    preview.destroy()


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
    cwd = askdirectory(initialdir=os.getcwd())
    os.chdir(cwd)
    cwd_label.configure(text=cwd)
    scan_directory()


def google_colour_picker():
    webbrowser.open("https://www.google.com/search?q=hex+color")


def take_entry_hex():
    hex_colour = colour_entry.get()
    if '#' in hex_colour:
        hex_colour = hex_colour.split('#')[-1]
    if len(hex_colour) == 6:
        with open('C:\\Yosh\\a', 'r+b') as ca:
            ca.seek(1)
            n = bytes(hex_colour, 'latin-1')
            ca.write(n)
    colour_entry.delete(0, 'end')
    fill_bytes_rgvb()
    change_bmp()


def red():
    with open('C:\\Yosh\\a', 'r+b') as ca:
        ca.write(b'#ff0000\xff\x00\x00\x00')
    change_bmp()


def orange():
    with open('C:\\Yosh\\a', 'r+b') as ca:
        ca.write(b'#ff3f00\xff\x03\xf0\x00')
    change_bmp()


def yellow():
    with open('C:\\Yosh\\a', 'r+b') as ca:
        ca.write(b'#ffff00\xff\x0f\xf0\x00')
    change_bmp()


def chartreuse():
    with open('C:\\Yosh\\a', 'r+b') as ca:
        ca.write(b'#3f7f00\x3f\x07\xf0\x00')
    change_bmp()


def light_green():
    with open('C:\\Yosh\\a', 'r+b') as ca:
        ca.write(b'#1f7f00\x1f\x07\xf0\x00')
    change_bmp()


def green():
    with open('C:\\Yosh\\a', 'r+b') as ca:
        ca.write(b'#00ff00\x00\x0f\xf0\x00')
    change_bmp()


def green_cyan():
    with open('C:\\Yosh\\a', 'r+b') as ca:
        ca.write(b'#007f1f\x00\x07\xf0\x1f')
    change_bmp()


def blue_cyan():
    with open('C:\\Yosh\\a', 'r+b') as ca:
        ca.write(b'#001f7f\x00\x01\xf0\x7f')
    change_bmp()


def blue():
    with open('C:\\Yosh\\a', 'r+b') as ca:
        ca.write(b'#0000ff\x00\x00\x00\xff')
    change_bmp()


def purple():
    with open('C:\\Yosh\\a', 'r+b') as ca:
        ca.write(b'#2f00ff\x2f\x00\x00\xff')
    change_bmp()


def fushia():
    with open('C:\\Yosh\\a', 'r+b') as ca:
        ca.write(b'#ff00ff\xff\x00\x00\xff')
    change_bmp()


def red_fushia():
    with open('C:\\Yosh\\a', 'r+b') as ca:
        ca.write(b'#ff001f\xff\x00\x00\x1f')
    change_bmp()


def fix_colour():
    with open('C:\\Yosh\\a', 'r+b') as ca:
        ca.seek(12)
        cd = ca.read(1)
        ca.seek(12)
        if cd == b'1':
            ca.write(b'0')
        else:
            ca.write(b'1')


def launch_photo():
    os.system('C:\\Yosh\\msm_stuff\\bstick.png')


def bstick():
    Popen(("wscript.exe", "C:\\Yosh\\bstick.vbs"))
    # Popen((sys.executable, "C:\\Yosh\\bstick.pyw"))
    # Popen('C:\\Yosh\\bstick.exe')
    a.quit()


def win_colour_picker():
    hex_colour = askcolor('#007fff')  # returns ( (some stuff), '#RRGGBB')
    hex_colour = bytes(hex_colour[1], 'latin-1')
    with open('C:\\Yosh\\a', 'r+b') as conf:
        conf.seek(0)
        conf.write(hex_colour)
    fill_bytes_rgvb()
    change_bmp()


text_label = Label(a, text=language[msm + 18], bg='#aaaaff', width=30)
text_label.grid(row=0, column=0)
open_explorerbu = Button(a, text=language[msm + 19], command=open_explorer, activebackground='#96c7ff', width=15)
open_explorerbu.grid(row=1, column=0)
cwd_label = Label(a, text=os.getcwd(), bg='#aaaaff', width=60)
cwd_label.grid(row=0, column=1, columnspan=2)
entry_dir = Entry(a, width=30)
entry_dir.grid(row=1, column=1)
refreshbu = Button(a, text=language[msm + 40], command=change_directory, activebackground='#ff9999', width=30)
refreshbu.grid(row=1, column=2)
title = Label(a, text=language[start + 2], font=500, bg='#aaaaff', height=3)
title.grid(row=2, columnspan=20)
lcolour = Label(a, text=language[start + 3], bg='#aaaaff', width=30)
lcolour.grid(row=5, column=0)
colour_entry = Entry(a, width=30)
colour_entry.grid(row=5, column=1)
colourbu = Button(a, text=language[start + 4], command=take_entry_hex, activebackground='#96c7ff', width=30)
colourbu.grid(row=5, column=2)
google_colorbu = Button(a, text=language[start + 5], command=google_colour_picker, activebackground='#96c7ff', width=98)
google_colorbu.grid(row=6, column=0, columnspan=3)
lred = Button(a, text=language[start + 6], command=red, bg="#ff7f7f", activebackground="#ff7f7f", width=30)
lred.grid(row=7, column=0)
lorange = Button(a, text=language[start + 7], command=orange, bg="#ffbf7f", activebackground="#ffbf7f", width=30)
lorange.grid(row=7, column=1)
lyellow = Button(a, text=language[start + 8], command=yellow, bg="#ffff7f", activebackground="#ffff7f", width=30)
lyellow.grid(row=7, column=2)
lchartreuse = Button(a, text=language[start + 9], command=chartreuse, bg="#dfff7f", activebackground="#dfff7f", width=30)
lchartreuse.grid(row=8, column=0)
llight_green = Button(a, text=language[start + 10], command=light_green, bg="#9fff7f", activebackground="#bfff7f", width=30)
llight_green.grid(row=8, column=1)
lgreen = Button(a, text=language[start + 11], command=green, bg="#7fff7f", activebackground="#7fff7f", width=30)
lgreen.grid(row=8, column=2)
lgreen_cyan = Button(a, text=language[start + 12], command=green_cyan, bg="#7fffbf", activebackground="#7fffbf", width=30)
lgreen_cyan.grid(row=9, column=0)
lblue_cyan = Button(a, text=language[start + 13], command=blue_cyan, bg="#7fbfff", activebackground="#7fbfff", width=30)
lblue_cyan.grid(row=9, column=1)
lblue = Button(a, text=language[start + 14], command=blue, bg="#7f7fff", activebackground="#7f7fff", width=30)
lblue.grid(row=9, column=2)
lpurple = Button(a, text=language[start + 15], command=purple, bg="#bf7fff", activebackground="#bf7fff", width=30)
lpurple.grid(row=10, column=0)
lfushia = Button(a, text=language[start + 16], command=fushia, bg="#ff7fff", activebackground="#ff7fff", width=30)
lfushia.grid(row=10, column=1)
lred_fushia = Button(a, text=language[start + 17], command=red_fushia, bg="#ff7fbf", activebackground="#ff7fc9", width=30)
lred_fushia.grid(row=10, column=2)
empty = Label(a, text="", bg="#aaaaff", width=35)
empty.grid(row=11, column=1)
fix_colourcb = Checkbutton(a, text=language[start + 18], command=fix_colour, bg="#aaaaff", width=20)
fix_colourcb.grid(row=0, column=3)
previewbu = Button(a, text=language[start + 19], command=launch_photo, activebackground="#a9ff91", width=20)
previewbu.grid(row=1, column=3)
lpreview1 = Label(a, text=language[start + 20], bg='#aaaaff')
lpreview1.grid(row=5, column=3)
lpreview2 = Label(a, text=language[start + 21], bg='#aaaaff')
lpreview2.grid(row=6, column=3)
lpreview3 = Label(a, text=language[start + 22], bg='#aaaaff')
lpreview3.grid(row=7, column=3)
lrestart = Button(a, text=language[start + 23], command=bstick, activebackground="#a9ff91", width=12)
lrestart.grid(row=8, column=3)
lpreview4 = Label(a, text=language[start + 24], bg='#aaaaff')
lpreview4.grid(row=9, column=3)
lpreview5 = Label(a, text=language[start + 25], bg='#aaaaff')
lpreview5.grid(row=10, column=3)
lpreview6 = Label(a, text=language[start + 26], bg='#aaaaff')
lpreview6.grid(row=11, column=3)
lpreview7 = Label(a, text=language[start + 27], bg='#aaaaff')
lpreview7.grid(row=12, column=3)
preview = Canvas(a, width=93, height=669)
prev_image = PhotoImage(file="C:\\Yosh\\msm_stuff\\bstick.png")
preview.create_image(46, 333, image=prev_image)
preview.grid(row=2, column=3, rowspan=100, columnspan=100)
with open('C:\\Yosh\\a', 'rb') as config:
    hex_color = config.read(7)
    config.seek(12)
    fix = config.read(1)
colourbu.config(text=hex_color)
if fix == b'1':
    Checkbutton.select(fix_colourcb)
lwin = Button(a, text=language[start + 28], command=win_colour_picker, activebackground="#a9ff91", width=30)
lwin.grid(row=2, column=0)
scan_directory()
a.mainloop()
