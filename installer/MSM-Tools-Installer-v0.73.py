import os, shutil
try:
    import pyperclip
    from PIL import Image
except:
    os.system('pip install Pillow')
    os.system('pip install pyperclip')
from tkinter import Tk, Label, Button
from zipfile import ZipFile
from PIL import Image
if not os.path.exists('Common.zip'):
    input("Common.zip isn't in the same directory as this script,\nhow the heck do you want to use the tools without any script!?\npress enter to exit...")
    exit()
if not os.path.exists('jpg.zip'):
    input("hey dude ! you're missing jpg.zip, put it in the same directory as this script\nthe installer will not work without those images that I've spend an enormous amount of time to do.\npress enter to exit...")
    exit()
Cpath = Dpath = Epath = True
if os.path.exists('C:\\Yosh'):  # don't add the folder to path if it already exists
    Cpath = False
if os.path.exists('D:\\Yosh'):
    Dpath = False
if os.path.exists('E:\\Yosh'):
    Epath = False
    
import sys
root = sys.argv[0]
root = os.path.splitext(root)[0]
a = Tk()
a.title("Mario Sports Mix Modding App Installer v"+root.rsplit('v', 1)[-1])
a.minsize(680, 495)
a.maxsize(680, 495)
a.config(bg="#aecfee")

w = a.winfo_screenwidth()
h = a.winfo_screenheight()
print(f"Welcome to the console!\nHere you can see what's happening behind the installer\nthe buttons are just here to separate actions to let them finish\nWhen you'll click on 'I agree', it will resize 18 jpg to your screen dimensions ({w}x{h})\n\nDuring the installation, it will extract zips and move its content to your directory installation path\nit'll also delete useless data (except the installer as it can't delete itself lol)")
jpg = ['msma.jpg', 'msmb.jpg', 'r.jpg', 'r2.jpg', 'r3.jpg', 'r4.jpg', 'r5.jpg', 'r6.jpg', 'r7.jpg', 'r8.jpg', 'r9.jpg',
     'ra.jpg', 'rb.jpg', 'rc.jpg', 'rd.jpg', 're.jpg', 'rf.jpg', 'rm.jpg']
png = ['how-to-run-msm.png', 'MSM Shortcuts.png', 'm.png', 'm2.png', 'm3.png', 'm4.png', 'm5.png', 'm6.png', 'm7.png',
     'm8.png', 'm9.png', 'ma.png', 'mb.png', 'mc.png', 'md.png', 'me.png', 'mf.png', 'mm.png']
delete = ['jpg.zip', 'Common.zip', 'MSM-tools-installer.bat',
      "run-this-if-installer-doesn't-open.bat"]
with ZipFile('jpg.zip', 'r') as zipObj:
    zipObj.extractall()  # extracts jpg.zip (its content is in the jpg list)


def bat_code():
    return '''@echo off

:: BatchGotAdmin
:-------------------------------------
REM	 --> Check for permissions
	IF "%PROCESSOR_ARCHITECTURE%" EQU "amd64" (
>nul 2>&1 "%SYSTEMROOT%\\SysWOW64\\cacls.exe" "%SYSTEMROOT%\\SysWOW64\\config\\system"
) ELSE (
>nul 2>&1 "%SYSTEMROOT%\\system32\\cacls.exe" "%SYSTEMROOT%\\system32\\config\\system"
)

REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
	echo Requesting administrative privileges...
	goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
	echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\\getadmin.vbs"
	set params= %*
	echo UAC.ShellExecute "cmd.exe", "/c ""%~s0"" %params:"=""%", "", "runas", 1 >> "%temp%\\getadmin.vbs"

	"%temp%\\getadmin.vbs"
	del "%temp%\\getadmin.vbs"
	exit /B

:gotAdmin
	pushd "%CD%"
	CD /D "%~dp0"
:--------------------------------------	   
	setx path "%path%;'''


def step4_local():
    for el in png:
        os.system(f'xcopy "{el}" Yosh /i /y /q')
    for el in png:
        os.system(f'del "{el}"')
    for el in delete:
        os.system(f'del "{el}"')
    with open('./Yosh/lh.py', 'rb') as default_file:
        default_file.seek(0x132)
        path = default_file.read(10)
        print(path)
    for filee in os.listdir('./Yosh/'):
        if os.path.splitext(filee)[-1] in ['.pyw', '.py']:
            with open(f'./Yosh/{filee}', 'r+b') as filoc:
                content = filoc.read()
                ignore = []
                for i in range(len(content) - 9):
                    filoc.seek(i)
                    if filoc.read(10) != path:
                        continue
                    ignore.append(i)
                    ignore.append(i + 10)
            if ignore != []:
                with open(f'./Yosh/{filee}', 'wb') as py:
                    i = 0
                    py.write(content[:ignore[0]])
                    for index in ignore:
                        if i == 1:
                            i = 2
                            offset = index
                        elif i == 2:
                            i = 1
                            py.write(content[offset:index])
                        else:
                            i = 1
                    py.write(content[index:])
        if os.path.splitext(filee)[-1] == '.bat':
            os.system(f'del ".\\Yosh\\{filee}"')
    a.quit()


def step4_c():
    os.system(f'xcopy Yosh C:\\Yosh /i /y /q /s')
    for el in png:
        os.system(f'xcopy "{el}" C:\\Yosh /i /y /q')

    if Cpath:
        with open('MSM-tools-installer.bat', 'w') as bat:
            bat.write(bat_code() + 'C:\\Yosh" /M')
        os.system('MSM-tools-installer.bat')
    shutil.rmtree('Yosh')
    for el in png:
        os.system(f'del "{el}"')
    for el in delete:
        os.system(f'del "{el}"')
    a.quit()


def step4_d():
    for element in os.listdir('./Yosh/'):
        if os.path.splitext(element)[-1] not in ['.bat', '.pyw', '.py']:
            continue
        with open(f'./Yosh/{element}', 'r+b') as file:
            data = file.read()
            for i in range(len(data) - 9):
                file.seek(i)
                if file.read(3) != b'C:\\':
                    continue
                file.seek(i)      # by default everything in common.zip is for C:\\Yosh
                file.write(b'D')  # this changes it to D:\\Yosh
    os.system(f'xcopy Yosh D:\\Yosh /i /y /q /s')
    for el in png:
        os.system(f'xcopy "{el}" D:\\Yosh /i /y /q')

    if Dpath:
        with open('MSM-tools-installer.bat', 'w') as bat:
            bat.write(bat_code() + 'D:\\Yosh" /M')
        os.system('MSM-tools-installer.bat')
    shutil.rmtree('Yosh')
    for el in png:
        os.system(f'del "{el}"')
    for el in delete:
        os.system(f'del "{el}"')
    a.quit()


def step4_e():
    for element in os.listdir('./Yosh/'):
        if os.path.splitext(element)[-1] not in ['.bat', '.pyw', '.py']:
            continue
        for i in range(len(element) - 9):
            with open(f'./Yosh/{element}', 'r+b') as file:
                file.seek(i)
                if file.read(8) != b'C:\\Yosh':
                    continue
                file.seek(i)      # by default everything in common.zip is for C:\\Yosh
                file.write(b'E')  # this changes it to E:\\Yosh
    os.system(f'xcopy Yosh E:\\Yosh /i /y /q /s')
    for el in png:
        os.system(f'xcopy "{el}" E:\\Yosh /i /y /q')

    if Epath:
        with open('MSM-tools-installer.bat', 'w') as bat:
            bat.write(bat_code() + 'E:\\Yosh" /M')
        os.system('MSM-tools-installer.bat')
    shutil.rmtree('Yosh')
    for el in png:
        os.system(f'del "{el}"')
    for el in delete:
        os.system(f'del "{el}"')
    a.quit()


def step3_c():
    for everything in a.winfo_children():
        everything.destroy()
    os.system('how-to-run-msm.png')  # tutorial on how to run the main menu script
    for element in jpg:
        os.system(f'del "{element}"')  # delete all jpg from jpg.zip
    with ZipFile('Common.zip', 'r') as zipcommon:
        zipcommon.extractall()  # extracts common.zip
    title3 = Label(a, text="Click on this button to finish installation :) click yes to cmd admin perm.\n\nonce it's done you can delete the installer and enjoy the tools :D\n", bg="#aecfee", font=100)
    title3.grid(row=0)
    button3 = Button(a, text="Finish installation", command=step4_c, activebackground="#a9ff91", width=30)
    button3.grid(row=3)


def step3_d():
    for everything in a.winfo_children():
        everything.destroy()
    os.system('how-to-run-msm.png')
    for element in jpg:
        os.system(f'del "{element}"')
    with ZipFile('Common.zip', 'r') as zipcommon:
        zipcommon.extractall()
    title3 = Label(a, text="Click on this button to finish installation :) click yes to cmd admin perm.\n\nonce it's done you can delete the installer and enjoy the tools :D\n", bg="#aecfee", font=100)
    title3.grid(row=0)
    button3 = Button(a, text="Finish installation", command=step4_d, activebackground="#a9ff91", width=30)
    button3.grid(row=3)


def step3_e():
    for everything in a.winfo_children():
        everything.destroy()
    os.system('how-to-run-msm.png')
    for element in jpg:
        os.system(f'del "{element}"')
    with ZipFile('Common.zip', 'r') as zipcommon:
        zipcommon.extractall()
    title3 = Label(a, text="Click on this button to finish installation :) click yes to cmd admin perm.\n\nonce it's done you can delete the installer and enjoy the tools :D\n", bg="#aecfee", font=100)
    title3.grid(row=0)
    button3 = Button(a, text="Finish installation", command=step4_e, activebackground="#a9ff91", width=30)
    button3.grid(row=3)


def step3_local():
    for everything in a.winfo_children():
        everything.destroy()
    os.system('how-to-run-msm.png')
    for element in jpg:
        os.system(f'del "{element}"')
    with ZipFile('Common.zip', 'r') as zipcommon:
        zipcommon.extractall()
    for o in a.winfo_children():
        o.destroy()
    title3 = Label(a, text="Click on this button to finish installation :)\nonce it's done you can delete the installer and enjoy the tools :D\n", bg="#aecfee", font=100)
    title3.grid(row=0)
    button3 = Button(a, text="Finish installation", command=step4_local, activebackground="#a9ff91", width=30)
    button3.grid(row=3)


def step2():
    for everything in a.winfo_children():
        everything.destroy()
    for i in range(len(jpg)):  # resize all jpg to your screen dimension and convert them to png
        pic = Image.open(jpg[i])
        new_pic = pic.resize((w, h))
        new_pic.save(png[i])
        pic.close()
    title2 = Label(a, text="Please Choose your installation directory", font=300, bg="#aecfee", height=3)
    title2.grid(row=0, columnspan=10)
    note2 = Label(a, text="Note: 'Local' is only intended to be used with a public computer (not your personal)\nor if you don't have Windows, as you have to double click the programs to run them.\n", bg="#aecfee")
    note2.grid(row=3, columnspan=3)
    path_c2 = Button(a, text="C:\\Yosh", command=step3_c, bg="#a9ff91", activebackground="#a9ff91", width=30)
    path_c2.grid(row=6, column=0)
    path_d2 = Button(a, text="D:\\Yosh", command=step3_d, bg="#a9ff91", activebackground="#a9ff91", width=30)
    path_d2.grid(row=6, column=1)
    path_e2 = Button(a, text="E:\\Yosh", command=step3_e, bg="#a9ff91", activebackground="#a9ff91", width=30)
    path_e2.grid(row=6, column=2)
    path_local2 = Button(a, text="Local (movable directory)\\Yosh", command=step3_local, bg="#ff9999", activebackground="#ff7f7f", width=30)
    path_local2.grid(row=7, column=1)


title = Label(a, text="Welcome to Mario Sports Mix Modding App Installer !", font=300, bg="#aecfee", height=3, width=60)
title.grid(row=0)
desc = Label(a, text="a free set of Scripts developped by Yosh in Python", font=300, bg="#aecfee", height=3)
desc.grid(row=3)
info = Label(a, text="if you've paid for this software you have been scammed", font=300, bg="#aecfee", height=3)
info.grid(row=6)
empty = Label(a, text="", font=300, bg="#aecfee", height=3)
empty.grid(row=9, column=0)
joke = Label(a, text="Terms of Agreement", font=300, bg="#aecfee", height=3)
joke.grid(row=10)
launch_step2 = Button(a, text="I agree", command=step2, activebackground="#a9ff91", width=30)
launch_step2.grid(row=13)
backend = Label(a, text="(the app will freeze 1 minute as it's resizing all jpg to your screen dimensions)", bg="#aecfee")
backend.grid(row=16)
a.mainloop()
