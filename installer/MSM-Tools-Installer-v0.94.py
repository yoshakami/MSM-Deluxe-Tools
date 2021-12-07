from tkinter import Tk, Label, Button, OptionMenu, StringVar, Checkbutton, DISABLED
# from subprocess import check_output
from functools import partial
from zipfile import ZipFile
# import webbrowser
import shutil
import string
import sys
import os

apps = ['arc.py', 'brsar.pyw', 'bstick.pyw', 'c.py', 'dec.py', 'dump.py', 'hexf.py', 'int.py', 'iso.py', 'isox.py',
        'lh.py', 'map.pyw', 'msm.pyw', 'msmhelp.pyw', 'p.py', 'pack.py', 'png.py', 'rEtUrN-tExT.py', 'sizeC.pyw',
        'slot.py', 't.py', 'tex.py', 'tex3.pyw', 'thp.pyw', 'trib.py', 'vaporwave.py', 'web.pyw', 'x.py', 'yt.pyw']

root = sys.argv[0]
root = os.path.splitext(root)[0]
a = Tk()
a.title("Mario Sports Mix Modding App Installer v" + root.rsplit('v', 1)[-1])
a.minsize(660, 495)
a.maxsize(660, 495)
a.config(bg="#aecfee")  # go to line 500 for the next part of code, then at the bottom and move up through functions

w = a.winfo_screenwidth()
h = a.winfo_screenheight()

if not os.path.exists("run this if installer doesn't open.bat"):
    with open("run this if installer doesn't open.bat", "w") as batch:
        batch.write('"' + sys.argv[0].split('\\')[-1] + '"\npause')
languages = (
    'English', 'Français', 'Deutsch')  # needs people to translate in other languages
lang = [0]  # change it to your lang if you want : english is 0, french is 1, deutsch is 2 and so on (if someone adds it)
# only lists can be changed in functions, not variables.
english = [
    'pip.exe not found. this file is included with python >= 3.7 (or you can manually install "pyperclip", "win10toast", and "Pillow" Modules)',
    "Common.zip isn't in the same directory as this script,\nhow the heck do you want to use the tools without any script!?\npress enter to exit...",
    "exe.zip isn't in the same directory as this script,\nI guess you don't want to use them then.\npress enter to continue...",
    "hey dude ! you're missing jpg.zip, put it in the same directory as this script\nthe installer will not work without those images that I've spend an enormous amount of time to do.\npress enter to exit...",
    "Welcome to the console!",
    "Here you can see what's happening behind the installer",
    "the buttons are just here to separate actions to let them finish",
    f"When you'll click on 'I agree', it will resize 18 jpg's to your screen dimensions ({w}x{h})",
    "During the installation, it will extract .zips and move their contents to your installation directory ",
    "It'll also delete useless data (except the installer as it can't delete itself lol)",
    "The installer will add the installation directory to PATH, so scripts will be able to be launched from everywhere !",
    "Welcome to Mario Sports Mix Modding App Installer !",
    "a free set of Scripts developed by Yosh in Python",
    "if you've paid for this software you have been scammed",
    "Choose Your Language",
    "Refresh",
    "Terms of Agreement",
    "I agree",
    "(the app will freeze 1 minute as it's resizing all jpgs to your screen dimensions)",
    "Please Choose your installation directory",
    "Clean the installation directory",
    "Don't use .ico files (for other OS not supporting them)",
    "Note: 'Local' is only intended to be used with a public computer (not your personal)\nyou will have to go to this folder to launch an app as it won't be added to path.\n",
    'v-- Select how you would like to launch the apps from explorer.exe search bar --v',
    'use .exe',
    'use .bat (a harmless black window open for half a second each time you launch an app)',
    "other OS than Windows (you won't be able to compress files but try looking at n.exe with Wine)",
    "Local (movable directory)",
    "Other OS than Windows",
    "Invalid Drive",
    "Click on this button to finish installation :)",
    "once it's done you can delete the installer and enjoy the tools :D",
    "You can also install the font that appeared in this directory,",
    "as the help app is specially designed for it",
    " Click yes for CMD admin perm",
    "installing to",
    "Finish installation"]

french = [
    'pip.exe introuvable. ce fichier est inclus avec python >= 3.7 (ou tu peux installer manuellement les modules "pyperclip", "win10toast" et "Pillow")',
    "Common.zip est pas dans le même dossier que ce script,\ncomment veux-tu utiliser mon pack sans aucun script !?\nappuie sur Entrée pour quitter...",
    "exe.zip est pas dans le même dossier que ce script,\nJe suppose que vous ne voulez pas les utiliser alors.\nappuie sur Entrée pour continuer...",
    "hey mec ! il te manque jpg.zip, place-le dans le même dossier que ce script\nce script d'installation fonctionnera pas sans ces images que j'ai passé énormément de temps à faire.\nappuie sur Entrée pour quitter.. .",
    "Bienvenue dans la console !",
    "Ici tu peux voir ce qui se passe derrière l'installateur - interface de hackeur - ",
    "les boutons sont juste là pour séparer les actions pour les laisser finir en fait mdrr\nau moins t'as un peu d'intéraction hein",
    f"Lorsque te cliqueras sur 'J'accepte', ça va redimentionner 18 jpg aux dimensions de ton écran, ({w}x{h})\nme remercie pas pour ces infos c'est cadeau",
    "Pendant l'installation, le programme va extraire les zips (comme tu t'en doutes hein) et va déplacer son contenu vers le chemin d'installation que tu choisiras",
    "à la fin, ce script va aussi supprimer les zips et les autres fichiers poubelle qu'il a pu laisser (sauf le programme d'installation car il ne peut pas se supprimer lol)",
    "le dossier d'installation va être ajouté à PATH, en gros, c'est une variable windows qui permettra aux scripts d'être lancés de n'importe où ! plutôt chouette non?",
    "Bienvenue dans l'installateur de mon pack de scripts\npour modder Mario Sports Mix !",
    "scripts gratuitement développés par Yosh en Python",
    "si t'as payé pour ce logiciel, t'es un gros pigeon\nabonné de cod forlan qui s'est fais arnaquer",
    "Choisis ta langue",
    "Rafraîchir",
    "Termes et Conditions",
    "J'accepte",
    "l'application va faire le fameux (ne réponds pas) 1 minute\ncar elle redimensionne toutes les jpg aux dimensions de l'écran",
    "Choisis ton chemin d'installation",
    "Nettoyer le dossier d'installation",
    "retirer les .ico (pour les autres OS qui connaissent pas ce format)",
    "Remarque : 'Local' est uniquement destiné à être utilisé avec un ordinateur public (pas ton pc perso)\nsinon tu devras accéder à ce dossier pour lancer un script car le dossier ne sera pas ajouté à %PATH%.\n",
    "v-- Sélectionne comment tu veux lancer les scripts (exe c'est mieux) --v",
    'utiliser les .exe',
    "utiliser les .bat (une putain de fenêtre noire s'ouvre une demi-seconde à chaque script lancé)",
    "autres OS que Windows (tu pourras pas compresser les fichiers, sauf si n.exe marche avec Wine en CLI)",
    "Local (version portable)",
    "Autre OS que Windows",
    "Lecteur invalide",
    "Clique sur ce bouton pour terminer l'installation :)  < " + '"CLIQUEZ, CLIQUEZ B"',
    "une fois que c'est fait, tu peux supprimer ce script d'installation\n^-^ profite bien des scripts :D",
    "Tu peux aussi installer la police d'écriture (font) qui est apparue dans ce dossier",
    "car l'application d'aide est spécialement conçue pour ce font",
    "\ncliques sur oui pour donner les droits d'admin",
    "installation dans le dossier",
    "Finir l'installation"]

german = [
    'pip.exe wurde nicht gefunden. Diese Datei ist in Python >= 3.7 enthalten (oder man kann die Module "pyperclip", "win10toast" und "Pillow" manuell installieren)',
    "Common.zip befindet sich nicht im selben Verzeichnis wie dieses Skript,\nwie zum Teufel wollen Sie die Tools ohne Skripts verwenden!?\nDrücke zum Beenden die Eingabetaste...",
    "exe.zip befindet sich nicht im selben Verzeichnis wie dieses Skript,\nIch nehme an, dass du sie dann nicht verwenden möchtest.\nDrücke die Eingabetaste, um fortzufahren...",
    "Hey Digga! Es existiert keine jpg.zip, kopier es in das gleiche Verzeichnis wie dieses Skript\nDas Installationsprogramm funktioniert nicht ohne diese Bilder, für die ich viel Zeit gebraucht habe.\nDrücke zum Beenden die Eingabetaste.. .",
    "Willkommen an der Konsole!",
    "Hier siehst du, was hinter dem Installer passiert",
    "Die Schaltflächen sind nur hier, um Aktionen zu trennen, damit sie beendet werden",
    f"Wenn 'Ich stimme zu' geklickt wird, wird die Größe von 18 Bilder an deine Bildschirmgröße ({w}x{h}) angepasst",
    "Während der Installation werden Zips entpackt und der Inhalt in den Installationspfad Ihres Verzeichnisses verschoben",
    "Es löscht auch nutzlose Daten (außer dem Installationsprogramm, da es sich nicht selbst löschen kann)",
    "Der Installer fügt das Installationsverzeichnis zu PATH hinzu, damit Skripte von überall gestartet werden können!",
    "Willkommen zum Mario Sports Mix Modding Tool Installer!",
    "ein paar Skripte, die von Yosh in Python entwickelt wurde",
    "Wenn Sie für diese Software bezahlt haben, wurden Sie betrogen",
    "Wähle deine Sprache",
    "Aktualisierung",
    "Vertragsbedingungen",
    "Genau",
    "(die App friert 1 Minute ein, da sie die Größe aller JPGs auf Ihre Bildschirmabmessungen ändert)",
    "Bitte wählen Sie Ihr Installationsverzeichnis",
    "Installationsverzeichnis bereinigen",
    "Verwenden Sie keine .ico-Dateien (für andere Betriebssysteme, die sie nicht unterstützen)",
    "Hinweis: 'Lokal' ist nur für die Verwendung mit einem öffentlichen Computer (nicht Ihrem persönlichen) vorgesehen.\nSie müssen in diesen Ordner gehen, um eine App zu starten, da sie nicht zum Pfad hinzugefügt wird.\n",
    'v-- Wählen Sie aus, wie Sie die Apps über die Suchleiste von explorer.exe starten möchten --v',
    'EXE verwenden (kann Windows Defender wütend machen)',
    'Batch benutzen (ein schwarzes Fenster öffnet sich jedes Mal für eine halbe Sekunde, wenn du eine App startest)',
    "anderes Betriebssystem als Windows (Sie können keine Dateien komprimieren oder dekomprimieren)",
    "Lokal (bewegliches Verzeichnis)",
    "Anderes Betriebssystem als Windows",
    "Ungültiges Laufwerk",
    "Klicken Sie auf diese Schaltfläche, um die Installation abzuschließen :)",
    "Sobald es fertig ist, können Sie das Installationsprogramm löschen und die Tools genießen :D",
    "Sie können auch die in diesem Verzeichnis erschienene Schriftart installieren",
    "da die Hilfe-App speziell dafür entwickelt wurde",
    "klicken Sie auf Ja, um cmd admin perm zu aktivieren",
    "installieren auf",
    "Beende die Installation"]

spanish = []
italian = []
dutch = []
portuguese = []
russian = []
polish = []
japanese = []
chinese = []
korean = []
language = (english, french, german, spanish, italian, dutch, portuguese, russian, polish, japanese, chinese, korean)


def input_lang():
    return input('Languages Available:\n0: English\n1: French (Français)\n2: German (Deutsch)\n\nheyy, type your language number : ')
    # \n2: German (Deutsch)\n3: Spanish (Español)\n4: Italian (Italiano)\n5: Dutch (Nederlands)\n6: Portuguese (Português)\n7: Russian (Pусский)\n8: Polish (Polskie)\n9: Japanese (日本語)\n10: Chinese (中国人)\n11: Korean (한국어)

try:
    import pyperclip
    from PIL import Image
    import win10toast
    import requests
    import win10toast_click
except ModuleNotFoundError or ImportError:
    os.system('python -m pip install --upgrade pip')
    os.system('pip install Pillow')
    os.system('pip install requests')
    os.system('pip install pyperclip')
    os.system('pip install win10toast')
    os.system('pip install win10toast_click')
try:
    from PIL import Image
except ModuleNotFoundError or ImportError:
    try:
        pip = sys.executable[:-10] + "Scripts\\pip.exe"
        os.system(f'{pip} install Pillow')
        os.system(f'{pip} install requests')
        os.system(f'{pip} install pyperclip')
        os.system(f'{pip} install win10toast')
        os.system(f'{pip} install win10toast_click')
        from PIL import Image
    except ModuleNotFoundError and ImportError:
        a.minsize(0, 0)
        a.maxsize(0, 0)
        input(language[int(input_lang())][0])
        """ # the best way is really to install python again
        print("pip.exe not found, this installer has a built in pip installer,")
        input("if you're on windows press enter, else you'll have to manually install pip...")
        if not os.path.exists('pip.zip'):
            print(f'press enter to download the additional zip file containing pip.exe, please paste this zip in this current directory ({os.getcwd()})')
            os.system('pause')
            webbrowser.open("https://cdn.discordapp.com/attachments/652624217333956619/857245728019709952/pip.zip")
        print('press enter to install pip to python (pip.zip should be in this directory before you press enter)')
        while not os.path.exists('pip.zip'):
            input(f'haha, nice joke but that zip is still not in {os.getcwd}....\npress enter to redownload...')
            webbrowser.open("https://cdn.discordapp.com/attachments/652624217333956619/857245728019709952/pip.zip")

        os.system('pause')
        if os.path.exists(f'{sys.executable[:-10]}\\pip.zip'):
            os.remove(f'{sys.executable[:-10]}\\pip.zip')
        os.rename('pip.zip', sys.executable[:-10] + '\\pip.zip')
        previous_dir = os.getcwd()
        os.chdir(sys.executable[:-10])
        with ZipFile('pip.zip', 'r') as pip_zip:
            pip_zip.extractall()
        # os.chdir(sys.executable[:-10] + "Scripts")
        # os.system('pip install Pillow')
        # os.system('pip install requests')
        # os.system('pip install pyperclip')
        # os.system('pip install win10toast')
        # os.system('pip install win10toast_click')
        try:
            from PIL import Image
            print('successfully installed pip and all addons (FYNALLY, IT WORKS OMFG)')
            os.system('pause')
            os.system('del pip.zip')
            os.chdir(previous_dir)
        except ModuleNotFoundError and ImportError:
            print("damn, pip.exe is kinda hard to install, please contact yosh if you want help")
            os.system('pause')
            exit(0)
            if not os.path.exists('addons.zip'):
                print("uh, probably manual install would work, sorry, I know that's a lot of downloads but you will put the next zip in this directory")
                os.system('pause')
                webbrowser.open("add_addons_here")
            print('press enter to install manually the addons')
            os.system('pause')
            os.rename('addons.zip', sys.executable[:-10] + '\\addons.zip')
            os.chdir(sys.executable[:-10])
            with ZipFile('addons.zip', 'r') as addons_zip:
                addons_zip.extractall()"""


exe = True
if not os.path.exists('Common.zip'):
    a.minsize(0, 0)
    a.maxsize(0, 0)
    input(language[int(input_lang())][1])
    exit()
if not os.path.exists('exe.zip'):
    input(language[int(input_lang())][2])
    exe = False
if not os.path.exists('jpg.zip'):
    a.minsize(0, 0)
    a.maxsize(0, 0)
    input(language[int(input_lang())][3])
    exit()

jpg = ['msma.jpg', 'msmb.jpg', 'r.png', 'r2.png', 'r3.png', 'r4.png', 'r5.png', 'r6.png', 'r7.png', 'r8.png', 'r9.png',
       'ra.png', 'rb.png', 'rc.png', 'rd.png', 're.png', 'rf.png', 'rm.png']
png = ['how-to-run-msm.png', 'MSM Shortcuts.png', 'm.png', 'm2.png', 'm3.png', 'm4.png', 'm5.png', 'm6.png', 'm7.png',
       'm8.png', 'm9.png', 'ma.png', 'mb.png', 'mc.png', 'md.png', 'me.png', 'mf.png', 'mm.png']
# delete = []
delete = ['jpg.zip', 'Common.zip', 'exe.zip', 'MSM-tools-installer.bat', "run this if installer doesn't open.bat"]

run = [language[lang[0]][24], language[lang[0]][25], language[lang[0]][26]]
with ZipFile('jpg.zip', 'r') as zipObj:
    zipObj.extractall()  # extracts jpg.zip (its content is in the jpg list)

with ZipFile('Common.zip', 'r') as zipcommon:
    zipcommon.extractall()


def bat_code():  # this func just requests admin perm
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
'''


def vbs(inst_path):  # this func will create all shortcuts to apps adding a custom icon + create all launchers
    inst_path += "\\Yosh\\"
    for script in apps:
        show = 1
        app = app2 = os.path.splitext(script)[0]
        python = sys.executable
        if script[-1] == 'w':
            python = python.rstrip('.exe') + "w.exe"
            show = 0
        if not os.path.exists(f"{inst_path}msm_stuff\\{app2}.ico"):
            app2 = 'gal'  # default ico in case I'm lazy, shoutout to Ryujinx
        with open(f'{app}.vbs', 'w') as vbs_file:
            vbs_file.write(f'''Set objShell = WScript.CreateObject("WScript.Shell")
lnkfile = "{inst_path}{app}.lnk"
Set obj = objShell.CreateShortcut(lnkfile)
obj.TargetPath = "{python}"
obj.Arguments = "{inst_path}{script}"
obj.Description = "Mario Sports Mix App"
obj.HotKey = ""
obj.IconLocation = "{inst_path}msm_stuff\\{app2}.ico"
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

    no_exe = False
    mode = RUN.get()
    if mode == run[0] and exe:  # if user choosed to use exe
        with ZipFile('exe.zip', 'r') as zipexe:
            zipexe.extractall()
    else:
        no_exe = True

    if clean_inst() == '1':
        if os.path.exists(f"{letter}:\\Yosh"):
            shutil.rmtree(f"{letter}:\\Yosh")
        shutil.copytree('Yosh', f"{letter}:\\Yosh")
    else:
        os.system(f'xcopy Yosh "{letter}:\\Yosh" /i /y /q /s')
    path = os.environ["PATH"]
    if "\\Yosh" in path or f'{letter}:\\Yosh' not in path:
        admin = False
        if f'{letter}:\\Yosh' not in path:
            admin = True
        list_path = path.split(';')
        list_path = list(dict.fromkeys(list_path))  # removes duplicates
        if os.environ["APPDATA"] + '\\Yosh' in list_path:
            list_path.remove(os.environ["APPDATA"] + '\\Yosh')
            admin = True
        for character in string.ascii_uppercase:  # clean every possible installation path from path variable
            if character + ':\\Yosh' in list_path:
                if character != letter:  # don't ask for admin perm
                    admin = True
                list_path.remove(character + ':\\Yosh')
        path = ''
        for element in list_path:
            path += element + ';'
        while path[-1] == ';':
            path = path[:-1]  # removes the last semicolon
        if admin:
            with open('MSM-tools-installer.bat', 'w') as bat_file:
                bat_file.write(bat_code() + f'setx path "{path};{letter}:\\Yosh" /M')

    font = 'Windows\\Fonts'
    m = 'MAR'
    if not os.path.exists(f'C:\\{font}\\{m}IO Font v3 Solid.otf'):
        if os.path.exists('MSM-tools-installer.bat'):
            with open('MSM-tools-installer.bat', 'a') as bat_file:
                bat_file.write(f'\nxcopy "{m}IO Font v3 Solid.otf" C:\\{font} /i /y /q /s\nreg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Fonts" /v "{m}IO Font v3 Solid (OpenType)" /t REG_SZ /d "{m}IO Font v3 Solid.otf" /f')
        else:
            with open('MSM-tools-installer.bat', 'w') as bat_file:
                bat_file.write(bat_code() + f'xcopy "{m}IO Font v3 Solid.otf" C:\\{font} /i /y /q /s\nreg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Fonts" /v "{m}IO Font v3 Solid (OpenType)" /t REG_SZ /d "{m}IO Font v3 Solid.otf" /f')
    if os.path.exists('MSM-tools-installer.bat'):
        os.system('MSM-tools-installer.bat')
#        os.system('pause')
    shutil.rmtree('Yosh')
    for el in delete:
        if os.path.exists(el):
            os.system(f'del "{el}"')
    if no_exe:
        bat(f'{letter}:')
    vbs(f'{letter}:')
    os.remove(f"{m}IO Font v3 Solid.otf")
    a.quit()


def step4_appdata(clean_inst):
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
                    py.write(content[:ignore[0]] + bytes(os.environ["APPDATA"].replace('\\', '\\\\'),
                                                         'latin-1') + b'\\\\Yosh\\\\')
                    for index in ignore:
                        if i == 1:
                            i = 2
                            offset = index
                        elif i == 2:
                            i = 1
                            py.write(content[offset:index] + bytes(os.environ["APPDATA"].replace('\\', '\\\\'),
                                                                   'latin-1') + b'\\\\Yosh\\\\')
                        else:
                            i = 1
                    py.write(content[index:])
    no_exe = False
    mode = RUN.get()
    if mode == run[0] and exe:  # if user choosed to use exe
        with ZipFile('exe.zip', 'r') as zipexe:
            zipexe.extractall()
    else:
        no_exe = True

    if clean_inst() == '1':
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
            bat_file.write(bat_code() + f'setx path "{path};{os.environ["APPDATA"]}\\Yosh" /M')

    font = 'Windows\\Fonts'
    m = 'MAR'
    if not os.path.exists(f'C:\\{font}\\{m}IO Font v3 Solid.otf'):
        if os.path.exists('MSM-tools-installer.bat'):
            with open('MSM-tools-installer.bat', 'a') as bat_file:
                bat_file.write(
                    f'\nxcopy "{m}IO Font v3 Solid.otf" C:\\{font} /i /y /q /s\nreg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Fonts" /v "{m}IO Font v3 Solid (OpenType)" /t REG_SZ /d "{m}IO Font v3 Solid.otf" /f')
        else:
            with open('MSM-tools-installer.bat', 'w') as bat_file:
                bat_file.write(
                    bat_code() + f'xcopy "{m}IO Font v3 Solid.otf" C:\\{font} /i /y /q /s\nreg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Fonts" /v "{m}IO Font v3 Solid (OpenType)" /t REG_SZ /d "{m}IO Font v3 Solid.otf" /f')
    if os.path.exists('MSM-tools-installer.bat'):
        os.system('MSM-tools-installer.bat')
    shutil.rmtree('Yosh')
    if no_exe:
        bat(os.environ["APPDATA"])
    vbs(os.environ["APPDATA"])
    os.remove(f'{m}IO Font v3 Solid.otf')
    a.quit()


def step4_local():
    with open('./Yosh/bstick.pyw', 'r+') as bstick:
        data = bstick.read()
        data = data.splitlines()
        new_data = ''
        for line in data:
            if line == '    Popen(("wscript.exe", "C:\\Yosh\\bstick.vbs"))':
                new_data += '    # Popen(("wscript.exe", "C:\\Yosh\\bstick.vbs"))\n'
            elif line == '    # Popen((sys.executable, "C:\\Yosh\\bstick.pyw"))':
                new_data += '    Popen((sys.executable, "C:\\Yosh\\bstick.pyw"))\n'
            else:
                new_data += line + '\n'
        bstick.seek(0)
        bstick.write(new_data)
    try:
        for el in delete:
            if os.path.exists(el):
                os.remove(el)
    except:
        'do nothing'
        pass
    path = 'C:\\\\Yosh\\\\'
    with open('./Yosh/msm.pyw', 'r+') as msmp:
        msm_data = msmp.read()
        msm_data = msm_data.splitlines()
        new_data = ''
        for line in msm_data:
            if "Popen(('wscript.exe', " in line:
                line_os = line.split('"')[1]
                script = line_os.split(".")[0][10:]  # removes C:\\Yosh\\
                if script == '{os':
                    new_data += '''    Popen((sys.executable.rstrip("w.exe")+".exe", f"C:\\\\Yosh\\\\{os.path.splitext(app.split('(')[-1])[0]}.py"))\n'''
                    continue
                # print('.\\Yosh\\'+script+'.py') # -> '.\Yosh\pack.py'
                if os.path.exists('.\\Yosh\\' + script + '.py'):
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

            with open(f'./Yosh/{filee}', 'w') as py:
                py.write(new_data)
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
    try:
        for el in delete:
            if os.path.exists(el):
                os.remove(el)
    except:
        'do nothing'
        pass
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
    if remove_ico() == '1':
        for ico in os.listdir('./Yosh/msm_stuff/'):
            if os.path.splitext(ico)[-1] == '.ico' and remove_ico() == '1':
                os.remove(f"./Yosh/msm_stuff/{ico}")
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

                with open(f'./Yosh/{file2}', 'w') as py:
                    py.write(new_data)

    for filee in os.listdir('./Yosh/'):  # replaces opening paths
        if os.path.splitext(filee)[-1] in ['.pyw', '.py']:
            # print(filee)
            with open(f'./Yosh/{filee}', 'r+') as filoc:
                content = filoc.read()
                content = content.replace('\\', '/')  # unix systems only support front slashes
                content = content.replace('/n', '\\n')  # lmao I like the snowball effect
                filoc.seek(0)
                filoc.write(content)

                content = content.splitlines()
                new_data = ''
                for line in content:
                    if path in line:
                        new_data += line.split(path)[0] + line.split(path)[-1] + '\n'
                    else:
                        new_data += line + '\n'

            with open(f'./Yosh/{filee}', 'w') as py:
                py.write(new_data)
        if os.path.splitext(filee)[-1] in ['.exe', '.bat', '.vbs', '.lnk']:
            os.remove(f"./Yosh/{filee}")
    a.quit()


def step3_drive(letter, clean_inst):
    a.config(bg="#aecfee")
    if not os.path.exists(f"{letter}:\\Yosh"):
        os.mkdir(f"{letter}:\\Yosh")
    print(f"{language[lang[0]][35]} {letter}:\\Yosh")
    for everything in a.winfo_children():
        everything.destroy()
    os.system('Yosh\\msm_stuff\\how-to-run-msm.png')
    for element in jpg:
        os.system(f'del "{element}"')
    path = os.environ["PATH"]
    admin = ""
    admin_perm = False
    for drive in string.ascii_uppercase:
        if drive != letter and f'{drive}:\\Yosh' in path:
            admin_perm = True
    font = 'Windows\\Fonts\\MAR'
    if f'{os.environ["APPDATA"]}\\Yosh' in path or f'{letter}:\\Yosh' not in path or admin_perm or not os.path.exists(f'C:\\{font}IO Font v3 Solid.otf'):
        admin = language[lang[0]][34]
    title3 = Label(a, text=f"{language[lang[0]][30]}{admin}.\n{language[lang[0]][31]}\n", bg="#aecfee", font=100)
    title3.grid(row=0)
    step4 = partial(step4_drive, letter, clean_inst)
    button3 = Button(a, text=language[lang[0]][36], command=step4, activebackground="#a9ff91", width=30)
    button3.grid(row=3)


def step3_appdata(clean_inst):
    # print(clean_inst, clean_inst(), type(clean_inst()), clean_inst == '1')
    a.config(bg="#aecfee")
    appdata = f'{os.environ["APPDATA"]}\\Yosh'
    print(f"{language[lang[0]][35]} {appdata}")
    if not os.path.exists(appdata):
        os.mkdir(appdata)

    for everything in a.winfo_children():
        everything.destroy()
    os.system('Yosh\\msm_stuff\\how-to-run-msm.png')
    for element in jpg:
        os.system(f'del "{element}"')
    for o in a.winfo_children():
        o.destroy()
    path = os.environ["PATH"]
    admin = ""
    font = 'Windows\\Fonts\\MAR'
    if ":\\Yosh" in path or appdata not in path or not os.path.exists(f'C:\\{font}IO Font v3 Solid.otf'):
        admin = language[lang[0]][34]
    title3 = Label(a, text=f"{language[lang[0]][30]}{admin}.\n{language[lang[0]][31]}\n", bg="#aecfee", font=100)
    title3.grid(row=0)
    step4 = partial(step4_appdata, clean_inst)
    button3 = Button(a, text=language[lang[0]][36], command=step4, activebackground="#a9ff91", width=30)
    button3.grid(row=3)


def step3_local():
    a.config(bg="#aecfee")
    for everything in a.winfo_children():
        everything.destroy()
    os.system('Yosh\\msm_stuff\\how-to-run-msm.png')
    try:
        for element in jpg:
            os.remove(element)
    except:
        pass
    for o in a.winfo_children():
        o.destroy()
    title3 = Label(a, text=f"{language[lang[0]][30]}\n{language[lang[0]][31]}\n\n{language[lang[0]][32]}\n{language[lang[0]][33]}", bg="#aecfee", font=100)
    title3.grid(row=0)
    button3 = Button(a, text=language[lang[0]][36], command=step4_local, activebackground="#a9ff91", width=30)
    button3.grid(row=3)


def step3_other(remove_ico):
    # print(remove_ico, remove_ico(), type(remove_ico()), remove_ico() == '1', remove_ico() == ('1'), sep='\n')
    a.config(bg="#aecfee")
    for everything in a.winfo_children():
        everything.destroy()
    # os.system('./Yosh/msm_stuff/how-to-run-msm.png')  # this picture is only for windows
    try:
        for element in jpg:
            os.remove(element)
    except:
        pass
    for o in a.winfo_children():
        o.destroy()
    title3 = Label(a, text=f"{language[lang[0]][30]}\n{language[lang[0]][31]}\n\n{language[lang[0]][32]}\n{language[lang[0]][33]}", bg="#aecfee", font=100)
    title3.grid(row=0)
    step4 = partial(step4_other, remove_ico)
    button3 = Button(a, text=language[lang[0]][36], command=step4, activebackground="#a9ff91", width=30)
    button3.grid(row=3)


def step2():
    refresh_func()
    a.config(bg="#ff9b69")
    for everything in a.winfo_children():
        everything.destroy()
    font = 'MAR'
    if not os.path.exists(font + 'IO Font v3 Solid.otf'):
        os.rename(font, font + 'IO Font v3 Solid.otf')
    title2 = Label(a, text=language[lang[0]][19], font=300, bg="#ff9b69", height=3)
    title2.grid(row=0, columnspan=10)
    clean = StringVar()
    clean_cb = Checkbutton(a, text=language[lang[0]][20], bg="#ff9b69", variable=clean)  # , width=20) #command=check
    clean_cb.grid(row=1, column=0)
    ico = StringVar()
    no_ico = Checkbutton(a, text=language[lang[0]][21], bg="#ff9b69", variable=ico)  # , width=20) #command=check
    no_ico.grid(row=1, column=1, columnspan=2)
    note2 = Label(a, text=language[lang[0]][22], bg="#ff9b69")
    note2.grid(row=2, columnspan=3)
    title2 = Label(a, text=language[lang[0]][23], font=(None, 13), bg="#ff9b69")  # , font=0.5
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
        new_pic.save(f"./Yosh/msm_stuff/{png[i]}")
        pic.close()

    appdata = partial(step3_appdata, clean.get)
    path_appdata2 = Button(a, text="%AppData%\\Yosh", command=appdata, bg="#91ffc8", activebackground="#91ffc8",
                           width=30)
    path_appdata2.grid(row=7, column=0)
    path_local2 = Button(a, text=f"{language[lang[0]][27]}\\Yosh", command=step3_local, bg="#ff9999",
                         activebackground="#ff7f7f", width=30)
    path_local2.grid(row=7, column=1)
    other = partial(step3_other, ico.get)
    path_other2 = Button(a, text=language[lang[0]][28], command=other, width=30)
    path_other2.grid(row=7, column=2)

    def verify(drive_letter, index):
        if os.path.exists(f'{drive_letter}:\\'):
            a.config(bg="#aecfee")
            step3_drive(drive_letter, clean.get)
        else:
            button_list[index].destroy()

    row = [9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12, 12, 13, 13, 13, 14, 14, 14, 15, 15, 15, 16, 16, 16, 17, 17, 17]
    col = [0, 1, 2]
    button_list = []
    # verif = partial(verify, 'C', 0)
    empty2 = Label(a, text="  ", font=(None, 2), bg="#ff9b69")
    empty2.grid(row=8, column=0)
    Checkbutton.deselect(clean_cb)
    Checkbutton.deselect(no_ico)
    for i in range(26):
        letter = string.ascii_uppercase[i]
        verif = partial(verify, letter, i)
        inva = Label(a, text=language[lang[0]][29], bg="#ff9b69", width=30)
        inva.grid(row=row[i], column=col[i % 3])
        bg = "#a9ff91"
        if os.path.exists(f'{letter}:\\'):
            bg = "#69ebff"
        path_drive = Button(a, text=f"{letter}:\\Yosh", command=verif, bg=bg, activebackground=bg, width=30)
        path_drive.grid(row=row[i], column=col[i % 3])
        button_list.append(path_drive)

func_called = [-1]
def refresh_func():
    for i in range(12):
        if languages[i] == LANGUAGES.get():
            lang[0] = i
            break
    for n in range(3):
        run[n] = language[lang[0]][24 + n]
    chosen_language = f'./Yosh/lang/{LANGUAGES.get()}.txt'
    if not os.path.exists(chosen_language):
        chosen_language = './Yosh/lang/English.txt'
    with open(chosen_language, 'rb') as txt1:
        new_lang = txt1.read()
    with open('./Yosh/#language.txt', 'wb') as txt2:
        txt2.write(new_lang)
    if func_called[0] != lang[0]:
        clearConsole()
        func_called[0] = lang[0]
        for some_tkstuff in a.winfo_children():
            some_tkstuff.destroy()
        title = Label(a, text=language[lang[0]][11], font=300, bg="#aecfee", height=3, width=60)
        title.grid(row=0)
        desc = Label(a, text=language[lang[0]][12], font=300, bg="#aecfee", height=3)
        desc.grid(row=1)
        info = Label(a, text=language[lang[0]][13], font=300, bg="#aecfee", height=3)
        info.grid(row=2)
        info2 = Label(a, text=language[lang[0]][14], font=(None, 13), bg="#aecfee")
        info2.grid(row=5)

        Languages = OptionMenu(a, LANGUAGES, *languages)
        Languages["menu"].config(bg="#000000", fg='#ffffff')
        Languages.config(width=15)
        Languages.grid(row=6, column=0, columnspan=2)
        emptya = Label(a, text="  ", font=(None, 1), bg="#aecfee")
        emptya.grid(row=7, column=0)
        refresh = Button(a, text=language[lang[0]][15], command=refresh_func, activebackground="#a9ff91", width=10)
        refresh.grid(row=8, column=0, columnspan=3)
        emptyb = Label(a, text="  ", font=(None, 5), bg="#aecfee")
        emptyb.grid(row=9, column=0)

        joke = Label(a, text=language[lang[0]][16], font=300, bg="#aecfee", height=3)
        joke.grid(row=10)
        launch_step2 = Button(a, text=language[lang[0]][17], command=step2, activebackground="#a9ff91", width=30)
        launch_step2.grid(row=11)
        backend = Label(a, text=language[lang[0]][18], bg="#aecfee")
        backend.grid(row=12)
        for j in range(4, 11):
            print(language[lang[0]][j] + '\n' * (j % 2))

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


LANGUAGES = StringVar()
RUN = StringVar()
LANGUAGES.set(languages[0])
refresh_func()
a.mainloop()
