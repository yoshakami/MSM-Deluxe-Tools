import os
import webbrowser
from tkinter import Tk, Label, Button, Canvas, PhotoImage

install_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(install_dir, '#language.txt'), 'r', encoding="utf-8") as txt:
    language = txt.read()
    language = [''] + language.splitlines()

start = int(language[1].split(":")[27])
msm = int(language[1].split(":")[1])
a = Tk()
a.title(language[msm + 2])
a.minsize(680, 440)
a.maxsize(680, 440)
a.config(bg="#bfffaa")
ico = os.path.join('msm_stuff', 'web.ico')
a.iconbitmap(os.path.join(install_dir, ico))
config_file = os.path.join(install_dir, 'a')


def howto():
    webbrowser.open("https://mario-sports-mix-modding-community-com.webnode.fr/how-to/")


def tht():
    webbrowser.open("https://mario-sports-mix-modding-community-com.webnode.fr/tht/")


def brsar():
    webbrowser.open("https://mario-sports-mix-modding-community-com.webnode.fr/brsar/")


def list_fr():
    webbrowser.open("https://mario-sports-mix-modding-community-com.webnode.fr/list/")


def tht_fr():
    webbrowser.open("https://mario-sports-mix-modding-community-com.webnode.fr/texture-hack/")


def list_en():
    webbrowser.open("https://mario-sports-mix-modding-community-com.webnode.fr/list/")


def info():
    webbrowser.open("https://mario-sports-mix-modding-community-com.webnode.fr/info/")


def filesystem():
    webbrowser.open("https://mario-sports-mix-modding-community-com.webnode.fr/filesystem/")


def custom():
    webbrowser.open("https://mario-sports-mix-modding-community-com.webnode.fr/custom/")


def mods():
    webbrowser.open("https://mario-sports-mix-modding-community-com.webnode.fr/mods/")


def mesg():
    webbrowser.open("https://mario-sports-mix-modding-community-com.webnode.fr/filesystem/menu/mesg/")


def tcrf():
    webbrowser.open("https://tcrf.net/Mario_Sports_Mix")


def sheet():
    webbrowser.open("https://docs.google.com/spreadsheets/d/1KUrCDyvDU8aOH_wJfC28MMRUYJZtH8jVQGUln8oSOQg/edit?usp=sharing")


def discord():
    webbrowser.open("https://discord.gg/y3bfyBf")


def yt():
    webbrowser.open("https://www.youtube.com/c/yoshytp")


ltitle = Label(a, text=language[start], font=300, bg="#bfffaa", height=3)
ltitle.grid(row=0, columnspan=3)
lhowto = Button(a, text=language[start + 1], command=howto, activebackground="#ff7f7f", width=30)
lhowto.grid(row=3, column=0)
ltht = Button(a, text=language[start + 2], command=tht, activebackground="#ffa555", width=30)
ltht.grid(row=3, column=1)
lbrsar = Button(a, text=language[start + 3], command=brsar, activebackground="#ffff7f", width=30)
lbrsar.grid(row=3, column=2)
l1 = Label(a, text="", bg="#bfffaa", width=35)
l1.grid(row=4, column=1)
llist_fr = Button(a, text=language[start + 4], command=list_fr, activebackground="#dfff7f", width=30)
llist_fr.grid(row=5, column=0)
ltht_fr = Button(a, text=language[start + 5], command=tht_fr, activebackground="#bfff7f", width=30)
ltht_fr.grid(row=5, column=1)
llist_en = Button(a, text=language[start + 6], command=list_en, activebackground="#7fff7f", width=30)
llist_en.grid(row=5, column=2)
l2 = Label(a, text="", bg="#bfffaa")
l2.grid(row=6)
linfo = Button(a, text=language[start + 7], command=info, activebackground="#7fffbf", width=30)
linfo.grid(row=7, column=0)
lfilesystem = Button(a, text=language[start + 8], command=filesystem, activebackground="#7fffff", width=30)
lfilesystem.grid(row=7, column=1)
lcustom = Button(a, text=language[start + 9], command=custom, activebackground="#7f7fff", width=30)
lcustom.grid(row=7, column=2)
l3 = Label(a, text="", bg="#bfffaa")
l3.grid(row=8, column=1)
lmods = Button(a, text=language[start + 10], command=mods, activebackground="#bf7fff", width=30)
lmods.grid(row=9, column=0)
lmesg = Button(a, text=language[start + 11], command=mesg, activebackground="#ff7fff", width=30)
lmesg.grid(row=9, column=1)
ltcrf = Button(a, text=language[start + 12], command=tcrf, activebackground="#ff7fbf", width=30)
ltcrf.grid(row=9, column=2)
l4 = Label(a, text="", bg="#bfffaa")
l4.grid(row=10, column=1)
lsheet = Button(a, text=language[start + 13], command=sheet, activebackground="#a9ff91", width=100, height=2)
lsheet.grid(row=11, rowspan=2, columnspan=20)
l5 = Label(a, text="", bg="#bfffaa")
l5.grid(row=13)
ldiscord = Button(a, text=language[start + 14], activebackground="#8888ff", command=discord, width=25)
ldiscord.grid(row=14, column=1)
lyt = Button(a, text=language[start + 15], activebackground="#ff7f7f", command=yt, width=25)
lyt.grid(row=15, column=1)
exitbu = Button(a, text=language[msm + 39], activebackground="#a9ff91", command=a.quit, width=25)
exitbu.grid(row=16, column=1)
msm1 = Canvas(a, width=220, height=148, bd=-2, bg="#aecfee")
msm_stuff = os.path.join(install_dir, 'msm_stuff')
msm_msm = PhotoImage(file=os.path.join(install_dir, "msm.png"))
msm1.create_image(110, 74, image=msm_msm)
msm1.grid(row=13, column=0, rowspan=6)
msm2 = Canvas(a, width=216, height=148, bd=-2, bg="#aecfee")
msm_png = PhotoImage(file=os.path.join(install_dir, "msm2.png"))
msm2.create_image(100, 100, image=msm_png)
msm2.grid(row=13, column=2, rowspan=6)

with open(config_file, "rb") as config:
    config.seek(11)
    color = config.read(1)

if color == b"1":
    lhowto.config(bg="#ff7f7f", activebackground="#ff7f7f")
  
    ltht.config(bg="#ffbf66", activebackground="#ffbf66")
  
    lbrsar.config(bg="#ffff7f", activebackground="#ffff7f")
  
    llist_fr.config(bg="#dfff7f", activebackground="#dfff7f")
      
    ltht_fr.config(bg="#bfff7f", activebackground="#bfff7f")
      
    llist_en.config(bg="#7fff7f", activebackground="#7fff7f")
      
    linfo.config(bg="#7fffbf", activebackground="#7fffbf")
      
    lfilesystem.config(bg="#7fffff", activebackground="#7fffff")
      
    lcustom.config(bg="#7f7fff", activebackground="#7f7fff")
      
    lmods.config(bg="#bf7fff", activebackground="#bf7fff")
      
    lmesg.config(bg="#ff7fff", activebackground="#ff7fff")
      
    ltcrf.config(bg="#ff7fbf", activebackground="#ff7fbf")
      
    lsheet.config(bg="#bfff7f", activebackground="#bfff7f")
      
    ldiscord.config(bg="#7f7fff", activebackground="#7f7fff")
      
    lyt.config(bg="#ff7f7f", activebackground="#ff7f7f")

elif color == b"2":
    lhowto.config(bg="#ff9090", activebackground="#ff9090")
  
    ltht.config(bg="#ffbf7f", activebackground="#ffbf7f")
  
    lbrsar.config(bg="#ffff90", activebackground="#ffff90")
  
    llist_fr.config(bg="#dfff90", activebackground="#dfff90")
      
    ltht_fr.config(bg="#bfff90", activebackground="#bfff90")
      
    llist_en.config(bg="#90ff90", activebackground="#90ff90")
      
    linfo.config(bg="#90ffbf", activebackground="#90ffbf")
      
    lfilesystem.config(bg="#90ffff", activebackground="#90ffff")
      
    lcustom.config(bg="#9090ff", activebackground="#9090ff")
      
    lmods.config(bg="#bf90ff", activebackground="#bf90ff")
      
    lmesg.config(bg="#ff90ff", activebackground="#ff90ff")
      
    ltcrf.config(bg="#ff90bf", activebackground="#ff90bf")
      
    lsheet.config(bg="#bfff90", activebackground="#bfff90")
      
    ldiscord.config(bg="#9090ff", activebackground="#9090ff")
      
    lyt.config(bg="#ff9090", activebackground="#ff9090")

elif color == b"3":
    lhowto.config(bg="#ff9999", activebackground="#ff9999")
  
    ltht.config(bg="#ffbf7f", activebackground="#ffbf7f")
  
    lbrsar.config(bg="#ffff99", activebackground="#ffff99")
  
    llist_fr.config(bg="#dfff99", activebackground="#dfff99")
      
    ltht_fr.config(bg="#bfff99", activebackground="#bfff99")
      
    llist_en.config(bg="#99ff99", activebackground="#99ff99")
      
    linfo.config(bg="#99ffbf", activebackground="#99ffbf")
      
    lfilesystem.config(bg="#99ffff", activebackground="#99ffff")
      
    lcustom.config(bg="#7f7fff", activebackground="#7f7fff")
      
    lmods.config(bg="#bf99ff", activebackground="#bf99ff")
      
    lmesg.config(bg="#ff99ff", activebackground="#ff99ff")
      
    ltcrf.config(bg="#ff99bf", activebackground="#ff99bf")
      
    lsheet.config(bg="#bfff99", activebackground="#bfff99")
      
    ldiscord.config(bg="#9999ff", activebackground="#9999ff")
      
    lyt.config(bg="#ff9999", activebackground="#ff9999")

elif color == b"4":
    lhowto.config(bg="#ffaaaa", activebackground="#ffaaaa")
  
    ltht.config(bg="#ffbfaa", activebackground="#ffbfaa")
  
    lbrsar.config(bg="#ffffaa", activebackground="#ffffaa")
  
    llist_fr.config(bg="#dfffaa", activebackground="#dfffaa")
      
    ltht_fr.config(bg="#bfffaa", activebackground="#bfffaa")
      
    llist_en.config(bg="#aaffaa", activebackground="#aaffaa")
      
    linfo.config(bg="#aaffbf", activebackground="#aaffbf")
      
    lfilesystem.config(bg="#aaffff", activebackground="#aaffff")
      
    lcustom.config(bg="#bbbbff", activebackground="#bbbbff")
      
    lmods.config(bg="#bfaaff", activebackground="#bfaaff")
      
    lmesg.config(bg="#ffaaff", activebackground="#ffaaff")
      
    ltcrf.config(bg="#ffaabf", activebackground="#ffaabf")
      
    lsheet.config(bg="#bfffaa", activebackground="#bfffaa")
      
    ldiscord.config(bg="#aaaaff", activebackground="#aaaaff")
      
    lyt.config(bg="#ffaaaa", activebackground="#ffaaaa")

elif color == b"5":
    lhowto.config(bg="#ffbbbb", activebackground="#ffbbbb")
  
    ltht.config(bg="#ffbfaa", activebackground="#ffbfaa")
  
    lbrsar.config(bg="#ffffbb", activebackground="#ffffbb")
  
    llist_fr.config(bg="#dfffbb", activebackground="#dfffbb")
      
    ltht_fr.config(bg="#bfffbb", activebackground="#bfffbb")
      
    llist_en.config(bg="#bbffbb", activebackground="#bbffbb")
      
    linfo.config(bg="#bbffbf", activebackground="#bbffbf")
      
    lfilesystem.config(bg="#bbffff", activebackground="#bbffff")
      
    lcustom.config(bg="#bbbbff", activebackground="#bbbbff")
      
    lmods.config(bg="#bfbbff", activebackground="#bfbbff")
      
    lmesg.config(bg="#ffbbff", activebackground="#ffbbff")
      
    ltcrf.config(bg="#ffbbbf", activebackground="#ffbbbf")
      
    lsheet.config(bg="#bfffbb", activebackground="#bfffbb")
      
    ldiscord.config(bg="#bbbbff", activebackground="#bbbbff")
      
    lyt.config(bg="#ffbbbb", activebackground="#ffbbbb")

a.mainloop()
