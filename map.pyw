import os
from tkinter import Tk, Label, Button
from tkinter.filedialog import askdirectory

if ':\\Windows' in os.getcwd():
    os.chdir(os.environ['userprofile'] + '\\Desktop')

with open('C:\\Yosh\\#language.txt', 'r', encoding="utf-8") as txt:
    language = txt.read()
    language = [''] + language.splitlines()

start = int(language[1].split(":")[17])
msm = int(language[1].split(":")[1])
a = Tk()
a.title(language[start])
a.minsize(439, 222)
a.config(bg='#dfaaff')
a.iconbitmap('C:\\Yosh\\msm_stuff\\map.ico')


def pal():
    os.system('"C:\\Yosh\\MSM PAL Symbol Map.txt"')


def ntscu():
    os.system('"C:\\Yosh\\MSM NTSC-U Symbol Map.txt"')


def japan():
    os.system('"C:\\Yosh\\MSM NTSC-J Symbol Map.txt"')


def map_help():
    os.system('"C:\\Yosh\\Symbol Map Help.txt"')


def save_no_filter():
    path = askdirectory(initialdir=os.getcwd())
    os.system(f'xcopy "C:\\Yosh\\MSM_PAL.txt" "{path}" /i /y /q')
    os.system(f'xcopy "C:\\Yosh\\MSM_NTSC-U.txt" "{path}" /i /y /q')
    os.system(f'xcopy "C:\\Yosh\\MSM_NTSC-J.txt" "{path}" /i /y /q')


def save_demangled():
    path = askdirectory(initialdir=os.getcwd())
    os.system(f'xcopy "C:\\Yosh\\MSM PAL Symbol Map.txt" "{path}" /i /y /q')
    os.system(f'xcopy "C:\\Yosh\\MSM NTSC-U Symbol Map.txt" "{path}" /i /y /q')
    os.system(f'xcopy "C:\\Yosh\\MSM NTSC-J Symbol Map.txt" "{path}" /i /y /q')
    os.system(f'xcopy "C:\\Yosh\\Symbol Map Help.txt" "{path}" /i /y /q')


title = Label(a, text=language[start + 1], bg='#dfaaff', font=300, height=3)
title.grid(row=0, columnspan=20)
helptxt = Button(a, text=language[start + 2], command=map_help, activebackground='#a9ff97', bg='#7fffbf', width=30)
helptxt.grid(row=3, column=0)
save_all = Button(a, text=language[start + 3], command=save_demangled, activebackground='#a9ff97', bg='#7fff7f', width=30)
save_all.grid(row=3, column=1)
view_pal = Button(a, text=language[start + 4], command=pal, activebackground='#a9ff97', bg='#ffa555', width=30)
view_pal.grid(row=4, column=0)
view_ntscu = Button(a, text=language[start + 5], command=ntscu, activebackground='#a9ff97', bg='#8888ff', width=30)
view_ntscu.grid(row=4, column=1)
view_ntscj = Button(a, text=language[start + 6], command=japan, activebackground='#a9ff97', bg='#ffff7f', width=30)
view_ntscj.grid(row=5, column=0)
save_no_filterbu = Button(a, text=language[start + 7], command=save_no_filter, activebackground='#a9ff97', bg='#ff7fbf', width=30)
save_no_filterbu.grid(row=5, column=1)
empty = Label(a, text='', bg='#dfaaff')
empty.grid(row=6)
exitbu = Button(a, text=language[msm + 39], command=a.quit, activebackground='#d9ff8c', width=15)
exitbu.grid(row=7, columnspan=2)
a.mainloop()
