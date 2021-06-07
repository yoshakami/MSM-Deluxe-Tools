from tkinter import Tk, Label, Button, OptionMenu, StringVar, Checkbutton, DISABLED
from subprocess import check_output
from functools import partial
from zipfile import ZipFile
import shutil
import string
import sys
import os

try:
    import pyperclip
    from PIL import Image
    import win10toast
except ModuleNotFoundError:
    os.system('python -m pip install --upgrade pip')
    os.system('pip install Pillow')
    os.system('pip install pyperclip')
    os.system('pip install win10toast')
try:
    from PIL import Image
except ModuleNotFoundError:
    print('pip.exe not found. this file is included with python >= 3.7 (or you can manually install "pyperclip", "win10toast", and "Pillow" Modules)')
    os.system('pause')

exe = True
if not os.path.exists('Common.zip'):
    input("Common.zip isn't in the same directory as this script,\nhow the heck do you want to use the tools without any script!?\npress enter to exit...")
    exit()
if not os.path.exists('exe.zip'):
    input("exe.zip isn't in the same directory as this script,\nI guess you don't want to use them then.\npress enter to continue...")
    exe = False
if not os.path.exists('jpg.zip'):
    input("hey dude ! you're missing jpg.zip, put it in the same directory as this script\nthe installer will not work without those images that I've spend an enormous amount of time to do.\npress enter to exit...")
    exit()

root = sys.argv[0]
root = os.path.splitext(root)[0]
a = Tk()
a.title("Mario Sports Mix Modding App Installer v" + root.rsplit('v', 1)[-1])
a.minsize(660, 495)
a.maxsize(660, 495)
a.config(bg="#aecfee")

w = a.winfo_screenwidth()
h = a.winfo_screenheight()
print(f"Welcome to the console!\nHere you can see what's happening behind the installer\nthe buttons are just here to separate actions to let them finish")
print("When you'll click on 'I agree', it will resize 18 jpg to your screen dimensions ({w}x{h})\n")
print("During the installation, it will extract zips and move its content to your directory installation path\nit'll also delete useless data (except the installer as it can't delete itself lol)")
print("the installer will add the installation directory to PATH, so scripts will be able to be launched from everywhere !\n")
jpg = ['msma.jpg', 'msmb.jpg', 'r.png', 'r2.png', 'r3.png', 'r4.png', 'r5.png', 'r6.png', 'r7.png', 'r8.png', 'r9.png',
       'ra.png', 'rb.png', 'rc.png', 'rd.png', 're.png', 'rf.png', 'rm.png']
png = ['how-to-run-msm.png', 'MSM Shortcuts.png', 'm.png', 'm2.png', 'm3.png', 'm4.png', 'm5.png', 'm6.png', 'm7.png',
       'm8.png', 'm9.png', 'ma.png', 'mb.png', 'mc.png', 'md.png', 'me.png', 'mf.png', 'mm.png']
delete = []
#delete = ['jpg.zip', 'Common.zip', 'exe.zip', 'MSM-tools-installer.bat']
apps = ['arc.py', 'brsar.pyw', 'bstick.pyw', 'c.pyw', 'dec.py', 'dump.py', 'hexf.py', 'int.py', 'iso.py', 'isox.py', 'lh.py',
        'map.pyw', 'msm.pyw', 'msmhelp.pyw', 'msmshortcuts.pyw', 'p.py', 'pack.pyw', 'png.py', 'rEtUrN-tExT.py',
        't.py', 'tex.py', 'tex3.pyw', 'thp.pyw', 'trib.py', 'vaporwave.py', 'web.pyw', 'x.pyw']
run = ('use exe (might get windows defender angry)', 'use bat (a wild black window open for half a second each time you launch an app)', "other OS than Windows (you won't be able to compress or decompress files)")
with ZipFile('jpg.zip', 'r') as zipObj:
    zipObj.extractall()  # extracts jpg.zip (its content is in the jpg list)

with ZipFile('Common.zip', 'r') as zipcommon:
    zipcommon.extractall()


def bat_code():  # this func just requests admin perm + the beginning of my command to add the tools to %PATH%
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
	setx path '''


def vbs(inst_path):  # this func will create all shortcuts to apps adding a custom icon + create all launchers
    inst_path += "\\Yosh\\"
    for script in apps:
        show = 1
        app = os.path.splitext(script)[0]
        python = sys.executable
        if script[-1] == 'w':
            python = python.rstrip('.exe') + "w.exe"
            show = 0
        with open(f'{app}.vbs', 'w') as vbs_file:
            vbs_file.write(f'''Set objShell = WScript.CreateObject("WScript.Shell")
lnkfile = "{inst_path}{app}.lnk"
Set obj = objShell.CreateShortcut(lnkfile)
obj.TargetPath = "{python}"
obj.Arguments = "{inst_path}{script}"
obj.Description = "Mario Sports Mix App"
obj.HotKey = ""
obj.IconLocation = "{inst_path}{app}.ico"
obj.WindowStyle = "{show}"
obj.WorkingDirectory = ""
obj.Save''')
        os.system(f'{app}.vbs')
    for script in apps:
        show = 1
        app = os.path.splitext(script)[0]
        try:
            os.remove(f'{app}.vbs')
        except:
            pass
        if script[-1] == 'w':
            show = 0
        with open(f"{inst_path}{app}.vbs", 'w') as vbs_file:
            vbs_file.write(f'CreateObject("Wscript.Shell").Run "{inst_path}{app}.lnk", {show}, False')


def bat(instal_path):  # this func is only called if the user choose to use bat files instead of exe
    instal_path += "\\Yosh\\"
    for script in apps:
        app = os.path.splitext(script)[0]
        with open(f"{instal_path}\\{app}.bat", 'w') as bat_file:
            bat_file.write(f'"{instal_path}launcher.pyw" {app}')


def step4_drive(letter, clean_inst):
    #with open('./Yosh/bstick.pyw', 'r+') as bstick:
        #data = bstick.read()
        #data = data.splitlines()
        #position = 0
        #for line in data:
        #    position += len(line)
        #    if line == '    Popen(("wscript.exe", "C:\\Yosh\\bstick.vbs"))':
        #        print(position)
    for element in os.listdir('./Yosh/'):
        if os.path.splitext(element)[-1] not in ['.pyw', '.py', '.vbs', '.bat']:
            continue
        with open(f'./Yosh/{element}', 'r+b') as file:
            data = file.read()
            for i in range(len(data) - 9):
                file.seek(i)
                if file.read(3) != b'C:\\':
                    continue
                file.seek(i)  # by default everything in Common.zip is for C:\\Yosh
                file.write(bytes(letter, 'latin-1'))  # this changes it to the drive letter :\\Yosh
    # os.system(f'xcopy Yosh "{letter}:\\Yosh" /i /y /q /s')

    no_exe = False
    mode = RUN.get()
    if mode == run[0] and exe:  # if user choosed to use exe
        with ZipFile('exe.zip', 'r') as zipexe:
            zipexe.extractall()
    else:
        no_exe = True

    if clean_inst:
        if os.path.exists(f"{letter}:\\Yosh"):
            shutil.rmtree(f"{letter}:\\Yosh")
        shutil.copytree('Yosh', f"{letter}:\\Yosh")
    else:
        os.system(f'xcopy Yosh "{letter}:\\Yosh" /i /y /q /s')
    # for el in png:
    #    os.system(f'xcopy "{el}" "{letter}:\\Yosh" /i /y /q')
    path = os.environ["PATH"]
    if "\\Yosh" in path or f'{letter}:\\Yosh' not in path:
        list_path = path.split(';')
        list_path = list(dict.fromkeys(list_path))  # removes duplicates
        if os.environ["APPDATA"]+'\\Yosh' in list_path:
            list_path.remove(os.environ["APPDATA"]+'\\Yosh')
        for character in string.ascii_uppercase:  # clean every possible installation path from path variable
            if character + ':\\Yosh' in list_path:
                list_path.remove(character + ':\\Yosh')
        path = ''
        for element in list_path:
            path += element + ';'
        while path[-1] == ';':
            path = path[:-1]  # removes the last semicolon
        with open('MSM-tools-installer.bat', 'w') as bat_file:
            bat_file.write(bat_code() + f'"{path};{letter}:\\Yosh;" /M')
        os.system('MSM-tools-installer.bat')
        #for character in string.ascii_uppercase:
        #    if character + ':\\Yosh' == path[:7]:
        #        path = path[7:]
        #    if character != letter and f'{character}:\\Yosh' in path:
        #        for i in range(len(path)):
        #            while f';{character}:\\Yosh' == path[i:i + 8]:
        #                path = path[0:i] + path[i + 8:]
                    # path = path.split(f';{character}:\\Yosh') doesn't work if there is twice the same value, as older versions added each time you install
                    # path = path[0] + path[1]
        #appdata = f'{os.environ["APPDATA"]}\\Yosh'
        #if appdata in path:
        #    size = len(appdata)
        #    if appdata == path[:size]:
        #        path = path[size:]
        #    z = 0
        #    while z < len(path):
        #        while ';' + appdata == path[z:z + size + 1]:
        #            # print('fixed 1 value in path')
        #            path = path[0:z] + path[z + size + 1:]
        #        # print(path[z:z+size+1])
        #        z += 1
                # path = path.split(f';{os.environ["APPDATA"]}\\Yosh')
                # path = path[0] + path[1]
            # os.system('pause')
    # if f'{letter}:\\Yosh' not in path:
    shutil.rmtree('Yosh')
    # for el in png:
    #    os.system(f'del "{el}"')
    for el in delete:
        os.system(f'del "{el}"')
    if no_exe:
        bat(f'{letter}:')
    vbs(f'{letter}:')
    a.quit()


def step4_appdata(clean_inst):
    #with open('./Yosh/bstick.pyw', 'r+') as bstick:
    #    data = bstick.read()
    #    data = data.splitlines()
    #    position = 0
    #    for line in data:
    #        position += len(line)
    #        if line == '    Popen(("wscript.exe", "C:\\Yosh\\bstick.vbs"))':
    #            print(position)
    # for el in png:
    #    os.system(f'xcopy "{el}" "{os.environ["APPDATA"]}\\Yosh" /i /y /q')
    # for el in png:
    #    os.system(f'del "{el}"')
    for el in delete:
        os.system(f'del "{el}"')
    # with open('./Yosh/lh.py', 'rb') as default_file:
    #    default_file.seek(0x132)
    #    path = default_file.read(10)  # C:\\\\Yosh doesn't work so instead I'll take it directly from lh.py as this script is at its final state
    #    print(path)
    path = b'C:\\\\Yosh\\\\'
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
                    py.write(content[:ignore[0]] + bytes(os.environ["APPDATA"].replace('\\', '\\\\'), 'latin-1') + b'\\\\Yosh\\\\')
                    for index in ignore:
                        if i == 1:
                            i = 2
                            offset = index
                        elif i == 2:
                            i = 1
                            py.write(content[offset:index] + bytes(os.environ["APPDATA"].replace('\\', '\\\\'), 'latin-1') + b'\\\\Yosh\\\\')
                        else:
                            i = 1
                    py.write(content[index:])
    # os.system(f'xcopy Yosh "{os.environ["APPDATA"]}\\Yosh" /i /y /q /s')
    no_exe = False
    mode = RUN.get()
    if mode == run[0] and exe:  # if user choosed to use exe
        with ZipFile('exe.zip', 'r') as zipexe:
            zipexe.extractall()
    else:
        no_exe = True

    if clean_inst:
        if os.path.exists(f"{os.environ['APPDATA']}\\Yosh"):
            shutil.rmtree(f"{os.environ['APPDATA']}\\Yosh")
        shutil.copytree('Yosh', f"{os.environ['APPDATA']}\\Yosh")
    else:
        os.system(f'xcopy Yosh "{os.environ["APPDATA"]}\\Yosh" /i /y /q /s')

    path = os.environ["PATH"]
    if ":\\Yosh" in path or f'{os.environ["APPDATA"]}\\Yosh' not in path:
        list_path = path.split(';')
        list_path = list(dict.fromkeys(list_path))  # removes duplicates
        if os.environ["APPDATA"] + '\\Yosh' in list_path:
            list_path.remove(os.environ["APPDATA"] + '\\Yosh')
        for character in string.ascii_uppercase:
            if character + ':\\Yosh' in list_path:
                list_path.remove(character + ':\\Yosh')
        path = ''
        for element in list_path:
            path += element + ';'
        while path[-1] == ';':
            path = path[:-1]  # removes the last semicolon
        with open('MSM-tools-installer.bat', 'w') as bat_file:
            bat_file.write(bat_code() + f'"{path};{os.environ["APPDATA"]}\\Yosh;" /M')
        os.system('MSM-tools-installer.bat')
            #if character + ':\\Yosh' == path[:7]:
            #    path = path[7:]
            #if f'{character}:\\Yosh' in path:
            #    for i in range(len(path)):
            #        while f';{character}:\\Yosh' == path[i:i + 9]:
            #            path = path[0:i] + path[i + 9:]
                    # path = path.split(f';{character}:\\Yosh') doesn't work if there is twice the same value, as older versions added each time you install
                    # path = path[0] + path[1]
    #if f'{os.environ["APPDATA"]}\\Yosh' not in path or edit_path:

    shutil.rmtree('Yosh')
    if no_exe:
        bat(os.environ["APPDATA"])
    vbs(os.environ["APPDATA"])
    a.quit()


def step4_local():
    with open('./Yosh/bstick.pyw', 'r+') as bstick:
        data = bstick.read()
        data = data.splitlines()
        new_data = ''
        for line in data:
            if line == '    Popen(("wscript.exe", "Z:\\Yosh\\bstick.vbs"))':
                new_data += '    # Popen(("wscript.exe", "Z:\\Yosh\\bstick.vbs"))\n'
            elif line == '    # Popen((sys.executable, "C:\\Yosh\\bstick.pyw"))':
                new_data += '    Popen((sys.executable, "C:\\Yosh\\bstick.pyw"))\n'
            else:
                new_data += line + '\n'
        bstick.seek(0)
        bstick.write(new_data)

    #        position += len(line)
    #        if line == '    Popen(("wscript.exe", "C:\\Yosh\\bstick.vbs"))':
    #            print(position)
    # for el in png:
    #    os.system(f'xcopy "{el}" Yosh /i /y /q')
    # for el in png:
    #    os.system(f'del "{el}"')
    try:
        for el in delete:
            os.remove(el)
    except:
        'do nothing'
        pass

    # with open('./Yosh/lh.py', 'rb') as default_file:
    #    default_file.seek(0x187)
    #    path = default_file.read(10)  # C:\\Yosh\\
    #    print(path)
    path = 'C:\\\\Yosh\\\\'
    with open('./Yosh/msm.pyw', 'r+') as msmp:
        msm_data = msmp.read()
        msm_data = msm_data.splitlines()
        new_data = ''
        for line in msm_data:
            if "Popen(('wscript.exe', " in line:
                line_os = line.split('"')[1]
                script = line_os.split(".")[0][10:] # removes C:\\Yosh\\
                if script == '{os':
                    new_data += '''    Popen((sys.executable.rstrip("w.exe")+".exe", f"C:\\\\Yosh\\\\{os.path.splitext(app.split('(')[-1])[0]}.py"))\n'''
                    continue
                # print('.\\Yosh\\'+script+'.py') # -> '.\Yosh\pack.py'
                if os.path.exists('.\\Yosh\\'+script+'.py'):
                    new_data += f'    Popen((sys.executable.rstrip("w.exe")+".exe", "{line_os.split(".")[0]}.py"))\n'
                else:
                    new_data += f'    Popen((sys.executable, "{line_os.split(".")[0]}.pyw"))\n'
            else:
                new_data += line + '\n'
    with open('./Yosh/#msm.pyw', "w") as msmpy:
        msmpy.write(new_data)
    os.remove('./Yosh/msm.pyw')
    for filee in os.listdir('./Yosh/'):
        if os.path.splitext(filee)[-1] in ['.pyw', '.py']:
            with open(f'./Yosh/{filee}', 'r+') as filoc:
                content = filoc.read()

                content = content.splitlines()
                new_data = ''
                for line in content:
                    if path in line:
                        new_data += line.split(path)[0] + line.split(path)[-1] + '\n'
                    else:
                        new_data += line + '\n'
                filoc.seek(0)
                filoc.write(new_data)

                """ignore = [] # there's an easier method above
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
                    py.write(content[index:])"""
    a.quit()


def step4_other(remove_ico):
    with open('./Yosh/bstick.pyw', 'r+') as bstick:
        data = bstick.read()
        data = data.splitlines()
        new_data = ''
        for line in data:
            if line == '    Popen(("wscript.exe", "Z:\\Yosh\\bstick.vbs"))':
                new_data += '    # Popen(("wscript.exe", "Z:\\Yosh\\bstick.vbs"))\n'
            elif line == '    # Popen((sys.executable, "C:\\Yosh\\bstick.pyw"))':
                new_data += '    Popen((sys.executable, "C:\\Yosh\\bstick.pyw"))\n'
            else:
                new_data += line + '\n'
        bstick.seek(0)
        bstick.write(new_data)
            # position += len(line)
            #    print(position)
    # for el in png:
    #    os.system(f'xcopy "{el}" Yosh /i /y /q')
    # for el in png:
    #    os.system(f'del "{el}"')
    try:
        for el in delete:
            os.remove(el)
    except:
        'do nothing'
        pass
    # with open('./Yosh/lh.py', 'rb') as default_file:
    #    default_file.seek(0x132)
    #    path = default_file.read(10)
    #    print(path)
    path = 'C://Yosh//'
    with open('./Yosh/msm.pyw', 'r+') as msmp:
        msm_data = msmp.read()
        msm_data = msm_data.splitlines()
        new_data = ''
        for line in msm_data:
            if "Popen(('wscript.exe', " in line:
                line_os = line.split('"')[1]
                script = line_os.split(".")[0][10:]  # removes C:\\Yosh\\
                if script == '{os':
                    new_data += """    Popen((sys.executable.rstrip("w.exe")+".exe", f"C:\\\\Yosh\\\\{os.path.splitext(app.split('(')[-1])[0]}.py"))\n"""
                    continue
                # print('.\\Yosh\\' + script + '.py')  # -> '.\Yosh\pack.py'
                if os.path.exists('./Yosh/' + script + '.py'):
                    new_data += f'    Popen((sys.executable.rstrip("w.exe")+".exe", "{line_os.split(".")[0]}.py"))\n'
                else:
                    new_data += f'    Popen((sys.executable, "{line_os.split(".")[0]}.pyw"))\n'
            else:
                new_data += line + '\n'
    with open('./Yosh/msm.py', "w") as msmpy:
        msmpy.write(new_data)
    os.remove("./Yosh/msm.pyw")
    if remove_ico:
        for file2 in os.listdir('./Yosh/'):
            if os.path.splitext(file2)[-1] in ['.pyw', '.py']:
                with open(f'./Yosh/{file2}', 'r+') as filoc:
                    file_data = filoc.read()
                    file_data = file_data.splitlines()
                    new_data = ''
                    for line in file_data:
                        if "a.iconbitmap(" in line:
                            continue
                        new_data += line + '\n'
                    filoc.seek(0)
                    filoc.write(new_data)

    for filee in os.listdir('./Yosh/'):  # replaces opening paths
        if os.path.splitext(filee)[-1] in ['.pyw', '.py']:
            print(filee)
            with open(f'./Yosh/{filee}', 'r+') as filoc:
                content = filoc.read()
                content = content.replace('\\', '/')  # unix systems only support front slashes
                content = content.replace('/n', '\\n') # lmao I like the snowball effect
                filoc.seek(0)
                filoc.write(content)

                content = content.splitlines()
                new_data = ''
                for line in content:
                    if path in line:
                        new_data += line.split(path)[0] + line.split(path)[-1] + '\n'
                    else:
                        new_data += line + '\n'
                filoc.seek(0)
                filoc.write(new_data)

                """ignore = [] 
                for i in range(len(content) - 9): # for some reason, the two last lines of each file get duplicated while it's the same code as local, WTF.
                    filoc.seek(i)
                    #if filoc.read(10) != path:
                    #    continue
                    if filoc.read(10) == path:
                        filoc.seek(i)
                        print(i, filoc.read(10))
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
                    print(content[index:])
                    print(content[offset:])
                    print(content[offset:index])"""
        if os.path.splitext(filee)[-1] == '.ico' and remove_ico:
            os.remove(f"./Yosh/{filee}")
        if os.path.splitext(filee)[-1] in ['.exe', '.bat', '.vbs', '.lnk']:
            os.remove(f"./Yosh/{filee}")
    a.quit()


def step3_drive(letter, clean_inst):
    a.config(bg="#aecfee")
    if not os.path.exists(f"{letter}:\\Yosh"):
        os.mkdir(f"{letter}:\\Yosh")
    print(f"installing to {letter}:\\Yosh")
    for everything in a.winfo_children():
        everything.destroy()
    os.system('Yosh\\how-to-run-msm.png')
    for element in jpg:
        os.system(f'del "{element}"')
    path = os.environ["PATH"]
    admin = ""
    admin_perm = False
    for drive in string.ascii_uppercase:
        if drive != letter and f'{drive}:\\Yosh' in path:
            admin_perm = True
    if f'{os.environ["APPDATA"]}\\Yosh' in path or f'{letter}:\\Yosh' not in path or admin_perm:
        admin = " click yes to cmd admin perm"
    step4 = partial(step4_drive, letter, clean_inst)
    title3 = Label(a, text=f"Click on this button to finish installation :){admin}.\n\nonce it's done you can delete the installer and enjoy the tools :D\n", bg="#aecfee", font=100)
    title3.grid(row=0)
    button3 = Button(a, text="Finish installation", command=step4, activebackground="#a9ff91", width=30)
    button3.grid(row=3)


def step3_appdata(clean_inst):
    a.config(bg="#aecfee")
    if not os.path.exists(f'{os.environ["APPDATA"]}\\Yosh'):
        os.mkdir(f'{os.environ["APPDATA"]}\\Yosh')

    for everything in a.winfo_children():
        everything.destroy()
    os.system('Yosh\\how-to-run-msm.png')
    for element in jpg:
        os.system(f'del "{element}"')
    for o in a.winfo_children():
        o.destroy()
    path = os.environ["PATH"]
    admin = ""
    if ":\\Yosh" in path or f'{os.environ["APPDATA"]}\\Yosh' not in path:
        admin = " click yes to cmd admin perm"
    title3 = Label(a, text=f"Click on this button to finish installation :){admin}.\nonce it's done you can delete the installer and enjoy the tools :D\n", bg="#aecfee", font=100)
    title3.grid(row=0)
    step4 = partial(step4_appdata, clean_inst)
    button3 = Button(a, text="Finish installation", command=step4, activebackground="#a9ff91", width=30)
    button3.grid(row=3)


def step3_local():
    a.config(bg="#aecfee")
    for everything in a.winfo_children():
        everything.destroy()
    os.system('Yosh\\how-to-run-msm.png')
    try:
        for element in jpg:
            os.remove(element)
    except:
        pass
    for o in a.winfo_children():
        o.destroy()
    title3 = Label(a, text="Click on this button to finish installation :)\nonce it's done you can delete the installer and enjoy the tools :D\n", bg="#aecfee", font=100)
    title3.grid(row=0)
    button3 = Button(a, text="Finish installation", command=step4_local, activebackground="#a9ff91", width=30)
    button3.grid(row=3)


def step3_other(remove_ico):
    a.config(bg="#aecfee")
    for everything in a.winfo_children():
        everything.destroy()
    # os.system('./Yosh/how-to-run-msm.png')  # this picture is only for windows
    try:
        for element in jpg:
            os.remove(element)
    except:
        pass
    for o in a.winfo_children():
        o.destroy()
    title3 = Label(a, text="Click on this button to finish installation :)\nonce it's done you can delete the installer and enjoy the tools :D\n", bg="#aecfee", font=100)
    title3.grid(row=0)
    step4 = partial(step4_other, remove_ico)
    button3 = Button(a, text="Finish installation", command=step4, activebackground="#a9ff91", width=30)
    button3.grid(row=3)


def step2():
    # def check():
    #     toogle(clean_cb)
    a.config(bg="#ff9b69")
    for everything in a.winfo_children():
        everything.destroy()
    title2 = Label(a, text="Please Choose your installation directory", font=300, bg="#ff9b69", height=3)
    title2.grid(row=0, columnspan=10)
    clean=StringVar()
    clean_cb = Checkbutton(a, text="Clean the installation directory", bg="#ff9b69", variable=clean)  # , width=20) #command=check
    clean_cb.grid(row=1, column=0)
    ico = StringVar()
    no_ico = Checkbutton(a, text="Don't use .ico files (for other OS not supporting them)", bg="#ff9b69", variable=ico)  # , width=20) #command=check
    no_ico.grid(row=1, column=1, columnspan=2)
    note2 = Label(a, text="Note: 'Local' is only intended to be used with a public computer (not your personal)\nyou will have to go to this folder to launch an app as it won't be added to path.\n", bg="#ff9b69")
    note2.grid(row=2, columnspan=3)
    title2 = Label(a, text='v-- Select how you would like to launch the apps from explorer.exe search bar --v', font=(None, 13), bg="#ff9b69")  # , font=0.5
    title2.grid(row=4, columnspan=10)
    Run = OptionMenu(a, RUN, *run)
    Run["menu"].config(bg="#000000", fg='#ffffff')
    if exe:
        RUN.set(run[0])
    else:
        RUN.set(run[1])
        Run["menu"].config(state=DISABLED)
    Run.config(width=90)
    Run.grid(row=5, column=0, columnspan=3)
    empty = Label(a, text="  ", font=(None, 2), bg="#ff9b69")
    empty.grid(row=6, column=0)
    for i in range(len(jpg)):  # resize all jpg to your screen dimension and convert them to png
        pic = Image.open(jpg[i])
        new_pic = pic.resize((w, h))
        new_pic.save(f"./Yosh/{png[i]}")
        pic.close()

    appdata = partial(step3_appdata, clean.get)
    path_appdata2 = Button(a, text="%AppData%\\Yosh", command=appdata, bg="#91ffc8", activebackground="#91ffc8", width=30)
    path_appdata2.grid(row=7, column=0)
    path_local2 = Button(a, text="Local (movable directory)\\Yosh", command=step3_local, bg="#ff9999", activebackground="#ff7f7f", width=30)
    path_local2.grid(row=7, column=1)
    other = partial(step3_other, ico.get)
    path_other2 = Button(a, text="Other OS than Windows", command=other, width=30)
    path_other2.grid(row=7, column=2)
    #for i in range(2):  # creates C and D drive buttons
    #    inva = Label(a, text="Invalid Drive", bg="#ff9b69", width=20)
    #    inva.grid(row=8, column=i, columnspan=2)

    def verify(drive_letter, index):
        if os.path.exists(f'{drive_letter}:\\'):
            a.config(bg="#aecfee")
            step3_drive(drive_letter, clean.get)
        else:
            button_list[index].destroy()

    row = [9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12, 12, 13, 13, 13, 14, 14, 14, 15, 15, 15, 16, 16, 16, 17, 17, 17]
    col = [0, 1, 2]
    button_list = []
    #verif = partial(verify, 'C', 0)
    empty2 = Label(a, text="  ", font=(None, 2), bg="#ff9b69")
    empty2.grid(row=8, column=0)
    #path_drive = Button(a, text=f"C:\\Yosh", command=verif, bg="#69ebff", activebackground="#69ebff", width=25)
    #path_drive.grid(row=8, column=0, columnspan=2)
    #button_list.append(path_drive)
    #verif = partial(verify, 'D', 1)
    #path_drive = Button(a, text=f"D:\\Yosh", command=verif, bg="#69ebff", activebackground="#69ebff", width=25)
    #path_drive.grid(row=8, column=1, columnspan=2)
    #button_list.append(path_drive)
    Checkbutton.deselect(clean_cb)
    Checkbutton.deselect(no_ico)
    for i in range(26):
        letter = string.ascii_uppercase[i]
        #if letter in ['C', 'D']:  # making C and D again would confuse the user
        #    continue
        verif = partial(verify, letter, i)
        inva = Label(a, text="Invalid Drive", bg="#ff9b69", width=30)
        inva.grid(row=row[i], column=col[i % 3])
        bg = "#a9ff91"
        if os.path.exists(f'{letter}:\\'):
            bg = "#69ebff"
        path_drive = Button(a, text=f"{letter}:\\Yosh", command=verif, bg=bg, activebackground=bg, width=30)
        path_drive.grid(row=row[i], column=col[i % 3])
        button_list.append(path_drive)


RUN = StringVar()
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
