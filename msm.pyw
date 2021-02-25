import os
import sys
from subprocess import Popen
from tkinter import Tk, Button, Label, END, Entry, Canvas, PhotoImage, DISABLED, OptionMenu, StringVar
from tkinter.filedialog import askdirectory

a = Tk()
a.title("Mario Sports Mix Modding App")
a.minsize(680, 495)
a.maxsize(680, 495)
a.config(bg="#aecfee")
a.iconbitmap('C:\\Yosh\\msm.ico')

run = ('Compress files in cwd (c.py)', 'Extract files in cwd (x.py)', 'Fix all textures to version 3 (f.py)',
       'Convert decimal to hex-float (hexf.py)', "CaPiTaLiSe (rEtUrN-tExT.py)", "V a p o r w a v e (vaporwave.py)")
RUN = StringVar()
RUN.set("Instant Run Apps (no UI)")
Run = OptionMenu(a, RUN, *run)
Run["menu"].config(bg="#000000", fg='#ffffff')


def enter():  # "Run Instant App (Enter)" Button
    app = RUN.get()
    if app == 'Compress files in cwd (c.py)':
        Popen((sys.executable.rstrip("w.exe") + ".exe", "C:\\Yosh\\c.py"))
    elif app == 'Extract files in cwd (x.py)':
        Popen((sys.executable.rstrip("w.exe") + ".exe", "C:\\Yosh\\x.py"))
    elif app == 'Fix all textures to version 3 (f.py)':
        Popen((sys.executable.rstrip("w.exe") + ".exe", "C:\\Yosh\\f.py"))
    elif app == 'Convert decimal to hex-float (hexf.py)':
        Popen((sys.executable.rstrip("w.exe") + ".exe", "C:\\Yosh\\hexf.py"))
    elif app == "CaPiTaLiSe (rEtUrN-tExT.py)":
        Popen((sys.executable.rstrip("w.exe") + ".exe", "C:\\Yosh\\rEtUrN-tExT.py"))
    elif app == "V a p o r w a v e (vaporwave.py)":
        Popen((sys.executable.rstrip("w.exe") + ".exe", "C:\\Yosh\\vaporwave.py"))
    cwd = cwd_entry.get()
    if cwd == '':
        cwd = os.getcwd()  # returns current working directory
    else:
        current_cwd.configure(text=cwd)
    cwd_entry.delete(0, END)  # empties the entry and change current working directory if it exists
    os.chdir(cwd)


def change_directory():  # executed when you press "Open FIle Explorer" button
    new_cwd = askdirectory(initialdir=os.getcwd())
    os.chdir(new_cwd)
    current_cwd.configure(text=new_cwd)


def p():
    Popen((sys.executable.rstrip("w.exe") + ".exe", "C:\\Yosh\\p.py"))


def t():
    Popen((sys.executable.rstrip("w.exe") + ".exe", "C:\\Yosh\\t.py"))


def brsar():  # run with the current executable (pythonw.exe full path)
    Popen((sys.executable, "C:\\Yosh\\brsar.pyw"))


def lh():  # run with command line window (else wszst opens too many windows and closes them instantly too frequently)
    Popen((sys.executable.rstrip("w.exe") + ".exe", "C:\\Yosh\\lh.py"))


def web():
    Popen((sys.executable, "C:\\Yosh\\web.pyw"))


def isox():
    Popen((sys.executable, "C:\\Yosh\\isox.pyw"))


def dump():
    Popen((sys.executable.rstrip("w.exe") + ".exe", "C:\\Yosh\\dump.py"))


def iso():
    Popen((sys.executable.rstrip("w.exe") + ".exe", "C:\\Yosh\\iso.py"))


def arc():
    Popen((sys.executable.rstrip("w.exe") + ".exe", "C:\\Yosh\\arc.py"))


def bstick():
    Popen((sys.executable, "C:\\Yosh\\bstick.pyw"))


def tex():
    Popen((sys.executable.rstrip("w.exe") + ".exe", "C:\\Yosh\\tex.py"))


def mappyw():
    Popen((sys.executable, "C:\\Yosh\\map.pyw"))


def png():
    Popen((sys.executable.rstrip("w.exe") + ".exe", "C:\\Yosh\\png.py"))


def trib():
    Popen((sys.executable.rstrip("w.exe") + ".exe", "C:\\Yosh\\trib.py"))


def msmhelp():
    Popen((sys.executable, "C:\\Yosh\\msmhelp.pyw"))


def shortcuts():
    Popen((sys.executable, "C:\\Yosh\\msmshortcuts.pyw"))


ltitle = Label(a, text="Mario Sports Mix Modding App Menu", font=300, bg="#aecfee", height=3)
ltitle.grid(row=0, columnspan=3)
lp = Button(a, text="Png texture replace (CLI no ex)", command=p, width=30)
lp.grid(row=3, column=0)
lt = Button(a, text="Encoded texture replace (CLI)", command=t, width=30)
lt.grid(row=3, column=1)
lbrsar = Button(a, text="Every Game Brsar Patcher", command=brsar, width=30)
lbrsar.grid(row=3, column=2)
l1 = Label(a, text="", bg="#aecfee", width=35)
l1.grid(row=4, column=1)
llh = Button(a, text="MSM files extract and compress", command=lh, width=30)
llh.grid(row=5, column=0)
lweb = Button(a, text="Website", command=web, width=30)
lweb.grid(row=5, column=1)
lisox = Button(a, text="MSM iso/wbfs extract and compress", command=isox, width=30)
lisox.grid(row=5, column=2)
l2 = Label(a, text="", bg="#aecfee")
l2.grid(row=6)
ldump = Button(a, text="Texture dump to png", command=dump, width=30)
ldump.grid(row=7, column=0)
liso = Button(a, text="MSM iso patcher (soon)", state=DISABLED, command=iso, width=30)
liso.grid(row=7, column=1)
larc = Button(a, text="MSM arc extract and compress", command=arc, width=30)
larc.grid(row=7, column=2)
l3 = Label(a, text="", bg="#aecfee")
l3.grid(row=8, column=1)
lbstick = Button(a, text="Change bstick colour", command=bstick, width=30)
lbstick.grid(row=9, column=0)
ltex = Button(a, text="Encode png to tex0", command=tex, width=30)
ltex.grid(row=9, column=1)
lmappyw = Button(a, text="MSM Symbol Map Viewer", command=mappyw, width=30)
lmappyw.grid(row=9, column=2)
l4 = Label(a, text="", bg="#aecfee")
l4.grid(row=10)
lpng = Button(a, text="Png texture replace (CLI ex)", command=png, width=30)
lpng.grid(row=11, column=0)
Run.config(width=30)
Run.grid(row=11, column=1)
ltrib = Button(a, text="Change root bone attributes", command=trib, width=30)
ltrib.grid(row=11, column=2)


def no_color():
    lp.config(activebackground="#ff9999", bg="#f0f0f0")

    lt.config(activebackground="#ffc999", bg="#f0f0f0")

    lbrsar.config(activebackground="#ffff99", bg="#f0f0f0")

    llh.config(activebackground="#dfff99", bg="#f0f0f0")

    lweb.config(activebackground="#bfff99", bg="#f0f0f0")

    lisox.config(activebackground="#99ff99", bg="#f0f0f0")

    ldump.config(activebackground="#99ffbf", bg="#f0f0f0")

    liso.config(activebackground="#99ffff", bg="#f0f0f0")

    larc.config(activebackground="#99d9ff", bg="#f0f0f0")

    lbstick.config(activebackground="#9999ff", bg="#f0f0f0")

    ltex.config(activebackground="#b999ff", bg="#f0f0f0")

    lmappyw.config(activebackground="#d999ff", bg="#f0f0f0")

    lpng.config(activebackground="#ff99ff", bg="#f0f0f0")

    Run.config(bg="#f0f0f0", activebackground="#f0f0f0")

    ltrib.config(activebackground="#ff99b9", bg="#f0f0f0")


def color_bb():
    lp.config(bg="#ffbbbb", activebackground="#ffbbbb")

    lt.config(bg="#ffbfaa", activebackground="#ffbfaa")

    lbrsar.config(bg="#ffffbb", activebackground="#ffffbb")

    llh.config(bg="#dfffbb", activebackground="#dfffbb")

    lweb.config(bg="#bfffbb", activebackground="#bfffbb")

    lisox.config(bg="#bbffbb", activebackground="#bbffbb")

    ldump.config(bg="#bbffbf", activebackground="#bbffbf")

    liso.config(bg="#bbffff", activebackground="#bbffff")

    larc.config(bg="#bbdfff", activebackground="#bbdfff")

    lbstick.config(bg="#bbbbff", activebackground="#bbbbff")

    ltex.config(bg="#cfbbff", activebackground="#cfbbff")

    lmappyw.config(bg="#ebbbff", activebackground="#ebbbff")

    lpng.config(bg="#ffbbff", activebackground="#ffbbff")

    Run.config(bg="#ffbbe4", activebackground="#ffbbe4")

    ltrib.config(bg="#ffbbcc", activebackground="#ffbbcc")


def color_aa():
    lp.config(bg="#ffaaaa", activebackground="#ffaaaa")

    lt.config(bg="#ffbfaa", activebackground="#ffbfaa")

    lbrsar.config(bg="#ffffaa", activebackground="#ffffaa")

    llh.config(bg="#dfffaa", activebackground="#dfffaa")

    lweb.config(bg="#bfffaa", activebackground="#bfffaa")

    lisox.config(bg="#aaffaa", activebackground="#aaffaa")

    ldump.config(bg="#aaffbf", activebackground="#aaffbf")

    liso.config(bg="#aaffff", activebackground="#aaffff")

    larc.config(bg="#aadfff", activebackground="#aadfff")

    lbstick.config(bg="#aaaaff", activebackground="#aaaaff")

    ltex.config(bg="#bfaaff", activebackground="#bfaaff")

    lmappyw.config(bg="#dfaaff", activebackground="#dfaaff")

    lpng.config(bg="#ffaaff", activebackground="#ffaaff")

    Run.config(bg="#ffaadf", activebackground="#ffaadf")

    ltrib.config(bg="#ffaabf", activebackground="#ffaabf")


def color_99():
    lp.config(bg="#ff9999", activebackground="#ff9999")

    lt.config(bg="#ffbf7f", activebackground="#ffbf7f")

    lbrsar.config(bg="#ffff99", activebackground="#ffff99")

    llh.config(bg="#dfff99", activebackground="#dfff99")

    lweb.config(bg="#bfff99", activebackground="#bfff99")

    lisox.config(bg="#99ff99", activebackground="#99ff99")

    ldump.config(bg="#99ffbf", activebackground="#99ffbf")

    liso.config(bg="#99ffff", activebackground="#99ffff")

    larc.config(bg="#99d9ff", activebackground="#99d9ff")

    lbstick.config(bg="#9999ff", activebackground="#9999ff")

    ltex.config(bg="#b999ff", activebackground="#b999ff")

    lmappyw.config(bg="#d999ff", activebackground="#d999ff")

    lpng.config(bg="#ff99ff", activebackground="#ff99ff")

    Run.config(bg="#ff99d9", activebackground="#ff99d9")

    ltrib.config(bg="#ff99b9", activebackground="#ff99b9")


def color_90():
    lp.config(bg="#ff9090", activebackground="#ff9090")

    lt.config(bg="#ffbf7f", activebackground="#ffbf7f")

    lbrsar.config(bg="#ffff90", activebackground="#ffff90")

    llh.config(bg="#dfff90", activebackground="#dfff90")

    lweb.config(bg="#bfff90", activebackground="#bfff90")

    lisox.config(bg="#90ff90", activebackground="#90ff90")

    ldump.config(bg="#90ffbf", activebackground="#90ffbf")

    liso.config(bg="#90ffff", activebackground="#90ffff")

    larc.config(bg="#90d0ff", activebackground="#90d0ff")

    lbstick.config(bg="#9090ff", activebackground="#9090ff")

    ltex.config(bg="#b090ff", activebackground="#b090ff")

    lmappyw.config(bg="#d090ff", activebackground="#d090ff")

    lpng.config(bg="#ff90ff", activebackground="#ff90ff")

    Run.config(bg="#ff90d0", activebackground="#ff90d0")

    ltrib.config(bg="#ff90b0", activebackground="#ff90b0")


def color_7f():
    lp.config(bg="#ff7f7f", activebackground="#ff7f7f")

    lt.config(bg="#ffbf66", activebackground="#ffbf66")

    lbrsar.config(bg="#ffff7f", activebackground="#ffff7f")

    llh.config(bg="#dfff7f", activebackground="#dfff7f")

    lweb.config(bg="#bfff7f", activebackground="#bfff7f")

    lisox.config(bg="#7fff7f", activebackground="#7fff7f")

    ldump.config(bg="#7fffbf", activebackground="#7fffbf")

    liso.config(bg="#7fffff", activebackground="#7fffff")

    larc.config(bg="#7fccff", activebackground="#7fccff")

    lbstick.config(bg="#7f7fff", activebackground="#7f7fff")

    ltex.config(bg="#aa7fff", activebackground="#aa7fff")

    lmappyw.config(bg="#cc7fff", activebackground="#cc7fff")

    lpng.config(bg="#ff7fff", activebackground="#ff7fff")

    Run.config(bg="#ff7fc4", activebackground="#ff7fc4")

    ltrib.config(bg="#ff7faa", activebackground="#ff7faa")


def change_config():  # change colour when "config" button is pressed
    with open("C:\\Yosh\\a", "r+b") as config:
        config.seek(11)
        colour = config.read(1)
        config.seek(11)
        if colour == b"1":
            config.write(b"2")
            color_90()
        elif colour == b"2":
            config.write(b"3")
            color_99()
        elif colour == b"3":
            config.write(b"4")
            color_aa()
        elif colour == b"4":
            config.write(b"5")
            color_bb()
        elif colour == b"5":
            config.write(b"0")
            no_color()
        else:
            config.write(b"1")
            color_7f()


with open("C:\\Yosh\\a", "rb") as conf:  # change colour after reading config file
    conf.seek(11)
    color = conf.read(1)
if color == b"1":
    color_7f()
elif color == b"2":
    color_90()
elif color == b"3":
    color_99()
elif color == b"4":
    color_aa()
elif color == b"5":
    color_bb()
else:
    no_color()
l5 = Label(a, text="", bg="#aecfee")
l5.grid(row=12)
lcwd = Label(a, text="Current working directory is", bg="#aecfee")
lcwd.grid(row=13, column=0)
current_cwd = Label(a, text=os.getcwd(), bg="#aecfee", width=29)
current_cwd.grid(row=14, column=0)
cwd_entry = Entry(a, width=30)
cwd_entry.grid(row=14, column=1)
me = Label(a, text="Made by Yosh", bg="#aecfee")
me.grid(row=13, column=1)
dirbutton = Button(a, text='Open file Explorer', command=change_directory, activebackground='#96c7ff', width=30)
dirbutton.grid(row=13, column=2)
lenter = Button(a, text="Run Instant App (Enter)", command=enter, activebackground="#a9ff91")
lenter.grid(row=14, column=2)
l6 = Label(a, text="", bg="#aecfee")
l6.grid(row=15)
lhelp = Button(a, text="Help", activebackground="#a9ff91", command=msmhelp, width=25)
lhelp.grid(row=16, column=1)
lshortcuts = Button(a, text="Shortcuts", activebackground="#a9ff91", command=shortcuts, width=25)
lshortcuts.grid(row=17, column=1)
lconfig = Button(a, text="Config", activebackground="#ff9999", command=change_config, width=25)
lconfig.grid(row=18, column=1)
msm1 = Canvas(a, width=216, height=148, bg="#aecfee")
msm_msm = PhotoImage(file="C:\\Yosh\\msm.png")
msm1.create_image(110, 90, image=msm_msm)
msm1.grid(row=15, column=0, rowspan=6)
msm2 = Canvas(a, width=216, height=148, bg="#aecfee")
msm_png = PhotoImage(file="C:\\Yosh\\png.png")
msm2.create_image(100, 100, image=msm_png)
msm2.grid(row=15, column=2, rowspan=6)
a.mainloop()
