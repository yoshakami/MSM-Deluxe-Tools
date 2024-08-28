from tkinter import Tk, Label, Button, Entry, OptionMenu, StringVar, Checkbutton, DISABLED
# from subprocess import check_output
from functools import partial
from zipfile import ZipFile
# import webbrowser
import shutil
import string
import sys
import os

apps = ['arc.py', 'brsar.pyw', 'bstick.pyw', 'c.py', 'dec.py', 'dump.py', 'gmk.py', 'hexf.py', 'hz.py', 
        'int.py', 'iso.py', 'isox.py', 'lh.py', 'map.pyw', 'miku.py', 'msm.pyw', 'msmhelp.pyw', 'p.py', 
        'pack.py', 'png.py', 'rEtUrN-tExT.py', 'sizeC.pyw', 'slot.py', 'stage.py', 'stream.py', 't.py', 
        'tex.py', 'tex3.pyw', 'thp.py', 'trib.py', 'vaporwave.py', 'web.pyw', 'x.py', 'yt.pyw']

root = sys.argv[0]
root = os.path.splitext(root)[0]
a = Tk()
a.title("Mario Sports Mix Modding App Installer v1.0")
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
    "you're missing jpg.zip, put it in the same directory as this script\nthe installer will not work without those images that I've spend an enormous amount of time to do.\npress enter to exit...",
    "Welcome to the console!", # 4
    "Here you can see what's happening behind the installer", # 5
    "the buttons are just here to separate actions to let them finish",
    f"When you'll click on 'I agree', it will resize 18 jpg's to your screen dimensions ({w}x{h})",
    "During the installation, it will extract .zips and move their contents to your installation directory ",
    "If you desire, with admin permission, the installer could (optionnally) add the installation directory to PATH", # 9
    "so scripts will be able to be launched from everywhere !", # 10
    "you can also install a font for the help app to work as intended", # 11
    "Welcome to Mario Sports Mix Modding App Installer !", # 12
    "a free set of Scripts developed by Yosh in Python", # 13
    "if you've paid for this software you have been scammed", # 14
    "Choose Your Language", # 15
    "Refresh", # 16
    "Terms of Agreement", # 17
    "I agree", # 18
    "(the app will freeze 1 minute as it's resizing all jpgs to your screen dimensions)", # 19
    "Please Choose your installation directory", # 20
    "Clean the installation directory", # 21
    "Don't use .ico files (for other OS not supporting them)", # 22
    "Note: 'Local' is only intended to be used with a public computer (not your personal)\nyou will have to go to this folder to launch an app as it won't be added to path.\n",
    'v-- Select how you would like to launch the apps from explorer.exe search bar --v', # 24
    'use .exe', # 25
    'use .bat (a harmless black window open for half a second each time you launch an app)', # 26
    "other OS than Windows (you won't be able to compress files but try looking at n.exe with Wine)", # 27
    "Local (movable directory)", # 28
    "Other OS than Windows", # 29
    "Invalid Drive", # 30
    "Click on this button to finish installation :)", # 31
    "once it's done you can delete the installer and enjoy the tools :D", # 32
    "You can also install the font that appeared in this directory,", # 33
    "as the help app is specially designed for it", # 34
    f"msmhelp font is not installed (msmhelp help app won't work as intended)\nyou can install it manually, it's the otf file in the current directory ({os.getcwd()})",
    "installing to", # 36
    "Finish installation", # 37
    "add to PATH", # 38
    "install font", # 39
    "[requires admin perm]", # 40
    "another msm folder is already added to PATH, please check both USER and SYSTEM PATH variable", # 41
    "current installation's msm folder is not added to PATH. You won't be able to launch scripts from the explorer menu if it's not added to PATH.", # 42
    "Edit PATH manually" # 43
    ]

french = [
    'pip.exe introuvable. ce fichier est inclus avec python >= 3.7 (ou tu peux installer manuellement les modules "pyperclip", "win10toast" et "Pillow")',
    "Common.zip est pas dans le même dossier que ce script,\ncomment veux-tu utiliser mon pack sans aucun script !?\nappuie sur Entrée pour quitter...",
    "exe.zip est pas dans le même dossier que ce script,\nJe suppose que vous ne voulez pas les utiliser alors.\nappuie sur Entrée pour continuer...",
    "il te manque jpg.zip, place-le dans le même dossier que ce script\nce script d'installation fonctionnera pas sans ces images que j'ai passé énormément de temps à faire.\nappuie sur Entrée pour quitter.. .",
    "Bienvenue dans la console !", # 4
    "Ici tu peux voir ce qui se passe derrière l'installateur - interface de hackeur - ", # 5
    "les boutons sont juste là pour séparer les actions pour les laisser finir en fait mdrr\nau moins t'as un peu d'intéraction hein", # 6
    f"Lorsque te cliqueras sur 'J'accepte', ça va redimentionner 18 jpg aux dimensions de ton écran, ({w}x{h})\nme remercie pas pour ces infos c'est cadeau", # 7
    "Pendant l'installation, le programme va extraire les zips (comme tu t'en doutes hein) et va déplacer son contenu vers le chemin d'installation que tu choisiras", # 8
    "Si tu veux, avec les permissions d'admin, tu peux ajouter ton installation à PATH (sur windows 10 ou 11 c'est mieux de faire à la main. et on va pas se mentir, c'est giga pratique PATH)", # 9
    "ajouter à PATH, ça te permet de lancer les scripts depuis la barre de l'explorateur de fichier Windows ! plutôt chouette non ?" # 10
    "tu peux aussi installer la police d'écriture pour que l'application d'aide s'affiche correctement", # 11
    "Bienvenue dans l'installateur de mon pack de scripts\npour modder Mario Sports Mix !", # 12
    "scripts gratuitement développés par Yosh en Python", # 13
    "si t'as payé pour ce logiciel, t'es un gros pigeon\nabonné de cod forlan qui s'est fais arnaquer", # 14
    "Choisis ta langue", # 15
    "Rafraîchir", # 16
    "Termes et Conditions", # 17
    "J'accepte", # 18
    "l'application va faire le fameux (ne réponds pas) 1 minute\ncar elle redimensionne toutes les jpg aux dimensions de l'écran", # 19
    "Choisis ton chemin d'installation", # 20
    "Nettoyer le dossier d'installation", # 21
    "retirer les .ico (pour les autres OS qui connaissent pas ce format)", # 22
    "Remarque : 'Local' est uniquement destiné à être utilisé avec un ordinateur public (pas ton pc perso)\nsinon tu devras accéder à ce dossier pour lancer un script car le dossier ne sera pas ajouté à %PATH%.\n", # 23
    "v-- Sélectionne comment tu veux lancer les scripts (exe c'est mieux) --v", # 24
    'utiliser les .exe', # 25
    "utiliser les .bat (une putain de fenêtre noire s'ouvre une demi-seconde à chaque script lancé)", # 26
    "autres OS que Windows (tu pourras pas compresser les fichiers, sauf si n.exe marche avec Wine en CLI)", # 27
    "Local (version portable)", # 28
    "Autre OS que Windows", # 29
    "Lecteur invalide", # 30
    "Clique sur ce bouton pour terminer l'installation :)  < " + '"CLIQUEZ, CLIQUEZ B"', # 31
    "une fois que c'est fait, tu peux supprimer ce script d'installation\n^-^ profite bien des scripts :D", # 32
    "Tu peux aussi installer la police d'écriture (font) qui est apparue dans ce dossier", # 33
    "car l'application d'aide est spécialement conçue pour ce font", # 34
    f"la police d'écriture pour msmhelp n'est pas installée (l'application va mal s'afficher sinon)\ntu peux l'installer manuellement, c'est le fichier otf dans le dossier actuel ({os.getcwd()})", # 35
    "installation dans le dossier", # 36
    "Terminer l'installation" # 37
    "ajouter à PATH", # 38
    "installer la police d'écriture" # 39
    "[admin]" # 40
    "un autre dossier de mes scripts est déjà ajouté dans PATH, il faudrait que tu regardes à la fois la vaiable PATH utilisateur, et la variable PATH système", # 41
    "l'installation actuelle n'est pas ajoutée à PATH. Tu pourras pas lancer les scripts depuis la barre de l'explorateur sans ajouter le dossier à PATH",
    "Modifier PATH manuellement" # 43
    ]

german = [
    'pip.exe wurde nicht gefunden. Diese Datei ist in Python >= 3.7 enthalten (oder man kann die Module "pyperclip", "win10toast" und "Pillow" manuell installieren)',
    "Common.zip befindet sich nicht im selben Verzeichnis wie dieses Skript,\nwie zum Teufel wollen Sie die Tools ohne Skripts verwenden!?\nDrücke zum Beenden die Eingabetaste...",
    "exe.zip befindet sich nicht im selben Verzeichnis wie dieses Skript,\nIch nehme an, dass du sie dann nicht verwenden möchtest.\nDrücke die Eingabetaste, um fortzufahren...",
    "Es existiert keine jpg.zip, kopier es in das gleiche Verzeichnis wie dieses Skript\nDas Installationsprogramm funktioniert nicht ohne diese Bilder, für die ich viel Zeit gebraucht habe.\nDrücke zum Beenden die Eingabetaste.. .",
    "Willkommen an der Konsole!", # 4
    "Hier siehst du, was hinter dem Installer passiert", # 5
    "Die Schaltflächen sind nur hier, um Aktionen zu trennen, damit sie beendet werden", # 6
    f"Wenn 'Ich stimme zu' geklickt wird, wird die Größe von 18 Bilder an deine Bildschirmgröße ({w}x{h}) angepasst", # 7
    "", # 8 outdated "Während der Installation werden Zips entpackt und der Inhalt in den Installationspfad Ihres Verzeichnisses verschoben",
    "", # 9 outdated "Es löscht auch nutzlose Daten (außer dem Installationsprogramm, da es sich nicht selbst löschen kann)",
    "", # 10 outdated "Der Installer fügt das Installationsverzeichnis zu PATH hinzu, damit Skripte von überall gestartet werden können!",
    "", # 11 outdated 
    "Willkommen zum Mario Sports Mix Modding Tool Installer!", # 12
    "ein paar Skripte, die von Yosh in Python entwickelt wurde", # 13
    "Wenn Sie für diese Software bezahlt haben, wurden Sie betrogen", # 14
    "Wähle deine Sprache", # 15
    "Aktualisierung", # 16
    "Vertragsbedingungen", # 17
    "Genau", # 18
    "(die App friert 1 Minute ein, da sie die Größe aller JPGs auf Ihre Bildschirmabmessungen ändert)", # 19
    "Bitte wählen Sie Ihr Installationsverzeichnis", # 20
    "Installationsverzeichnis bereinigen", # 21
    "Verwenden Sie keine .ico-Dateien (für andere Betriebssysteme, die sie nicht unterstützen)", # 22
    "Hinweis: 'Lokal' ist nur für die Verwendung mit einem öffentlichen Computer (nicht Ihrem persönlichen) vorgesehen.\nSie müssen in diesen Ordner gehen, um eine App zu starten, da sie nicht zum Pfad hinzugefügt wird.\n", # 23
    'v-- Wählen Sie aus, wie Sie die Apps über die Suchleiste von explorer.exe starten möchten --v', # 24
    'EXE verwenden (kann Windows Defender wütend machen)', # 25
    'Batch benutzen (ein schwarzes Fenster öffnet sich jedes Mal für eine halbe Sekunde, wenn du eine App startest)', # 26
    "anderes Betriebssystem als Windows (Sie können keine Dateien komprimieren oder dekomprimieren)", # 27
    "Lokal (bewegliches Verzeichnis)", # 28
    "Anderes Betriebssystem als Windows", # 29
    "Ungültiges Laufwerk", # 30
    "Klicken Sie auf diese Schaltfläche, um die Installation abzuschließen :)", # 31
    "Sobald es fertig ist, können Sie das Installationsprogramm löschen und die Tools genießen :D", # 32
    "Sie können auch die in diesem Verzeichnis erschienene Schriftart installieren", # 33
    "da die Hilfe-App speziell dafür entwickelt wurde", # 34
    "", # 35 outdated "klicken Sie auf Ja, um cmd admin perm zu aktivieren", # 35
    "installieren auf", # 36
    "Beende die Installation" # 37
    "", # 38
    "", # 39
    "", # 40
    "", # 41
    "", # 42
    "" # 43
    ]

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
# files = ['jpg.zip', 'Common.zip', 'exe.zip', 'MSM-tools-installer.bat', "run this if installer doesn't open.bat"]

run = [language[lang[0]][25], language[lang[0]][26], language[lang[0]][27]]
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


def step4_drive(letter, clean_inst, edit_path=False, install_font=False):
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
    if edit_path:
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
    if install_font:
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
    if no_exe:
        bat(f'{letter}:')
    vbs(f'{letter}:')
    a.quit()


def step4_appdata(clean_inst, edit_path=False, install_font=False):
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

    if edit_path:
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
    if install_font:
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
    if no_exe:
        bat(os.environ["APPDATA"])
    vbs(os.environ["APPDATA"])
    a.quit()


def use_python_file_instead_of_vbs():
    with open('./Yosh/bstick.pyw', 'r+', encoding='utf-8') as bstick:
        data = bstick.read()
        data = data.splitlines()
        new_data = ''
        for line in data:
            if line == '    Popen(("wscript.exe", f"{install_dir}/bstick.vbs"))':
                new_data += '    # Popen(("wscript.exe", f"{install_dir}/bstick.vbs"))\n'
            elif line == '    # Popen((sys.executable, f"{install_dir}/bstick.pyw"))':
                new_data += '    Popen((sys.executable, f"{install_dir}/bstick.pyw"))\n'
            else:
                new_data += line + '\n'
        bstick.seek(0)
        bstick.write(new_data)
    # change msm's way of launching apps.
    with open('./Yosh/msm.pyw', 'r+', encoding='utf-8') as msmp:
        msm_data = msmp.read()
        msm_data = msm_data.splitlines()
        new_data = ''
        for line in msm_data:
            if "Popen(('wscript.exe', " in line:
                line_os = line.split('"')[1]
                script = line_os.split(".")[0]
                if script.startswith('{os'):
                    new_data += """    Popen((sys.executable.rstrip("w.exe")+".exe", os.path.join(install_dir, f"{os.path.splitext(app.split('(')[-1])[0]}.py")))\n"""
                    continue
                # print('.\\Yosh\\' + script + '.py')  # -> '.\Yosh\pack.py'
                if os.path.exists('./Yosh/' + script + '.py'):
                    new_data += f'    Popen((sys.executable.rstrip("w.exe")+".exe", "{script}.py"))\n'
                else:
                    new_data += f'    Popen((sys.executable, "{script}.pyw"))\n'
            else:
                new_data += line + '\n'
        msmp.seek(0)
        msmp.write(new_data)
        
def step4_local():
    use_python_file_instead_of_vbs()
    a.quit()

def step4_other(remove_ico):
    use_python_file_instead_of_vbs()
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
                        if ".iconbitmap" in line:
                            continue
                        new_data += line + '\n'

                with open(f'./Yosh/{file2}', 'w') as py:
                    py.write(new_data)

    for filee in os.listdir('./Yosh/'):
        if os.path.splitext(filee)[-1] in ['.exe', '.bat', '.vbs', '.lnk']:
            os.remove(f"./Yosh/{filee}")
    a.quit()

def launch_path_app():
    os.system('systempropertiesadvanced')

def step3_drive(letter, clean_inst):
    a.config(bg="#aecfee")
    if not os.path.exists(f"{letter}:\\Yosh"):
        os.mkdir(f"{letter}:\\Yosh")
    print(f"{language[lang[0]][36]} {letter}:\\Yosh")
    for everything in a.winfo_children():
        everything.destroy()
    os.system('Yosh\\msm_stuff\\how-to-run-msm.png')
    for element in jpg:
        os.system(f'del "{element}"')
    path = os.environ["PATH"]
    admin = ""
    install_font = False
    edit_path = False
    font = 'Windows\\Fonts\\MAR'
    if not os.path.exists(f'C:\\{font}IO Font v3 Solid.otf'):
        admin = language[lang[0]][35] + "\n"
        install_font = True
    for drive in string.ascii_uppercase:
        if drive != letter and f'{drive}:\\Yosh' in path:
            admin += language[lang[0]][41] + "\n"
            edit_path = True
    if f'{os.environ["APPDATA"]}\\Yosh' in path and not edit_path:
        admin += language[lang[0]][41] + "\n"
        edit_path = True
    if f'{letter}:\\Yosh' not in path:
        admin += language[lang[0]][42] + "\n"
        edit_path = True
    title3 = Label(a, text=f"{language[lang[0]][31]}\n{admin}\n{language[lang[0]][32]}\n", bg="#aecfee", font=100)
    title3.grid(row=1, rowspan=5)
    all_button_text = ""
    if edit_path or install_font:
        all_button_text += language[lang[0]][40] + " "  # requires admin perm
    all_button_text += language[lang[0]][37] + " (" # finish installation
    if edit_path:
        all_button_text+= language[lang[0]][38]  # add to path
    if install_font:
        if edit_path:
            all_button_text += " + "
        all_button_text += language[lang[0]][39] # + install font
        font_step4 = partial(step4_drive, letter, clean_inst, edit_path=False, install_font=True)
        button3_font = Button(a, text=language[lang[0]][40] + " " + language[lang[0]][37] + f" ({language[lang[0]][39]})", command=font_step4, bg="#ff9b69", activebackground="#a9ff91", width=30)
        button3_font.grid(row=3, col=3)
    all_step4 = partial(step4_drive, letter, clean_inst, edit_path, install_font)
    
    all_button_text += ")"
    button3 = Button(a, text=all_button_text, command=all_step4, bg="#ff9b69", activebackground="#a9ff91", width=30)
    button3.grid(row=3, col=1, columnspan=2)
    
    step4_no_admin = partial(step4_drive, letter, clean_inst)
    button3_no_admin = Button(a, text=language[lang[0]][37], command=step4_no_admin, activebackground="#a9ff91", width=30)
    button3_no_admin.grid(row=3, col=4)
    
    
    launch_path = partial(launch_path_app, clean_inst)
    button3_launch_path = Button(a, text=language[lang[0]][37], command=launch_path, activebackground="#a9ff91", width=30)
    button3_launch_path.grid(row=4, col=1, columnspan=2)


def step3_appdata(clean_inst):
    # print(clean_inst, clean_inst(), type(clean_inst()), clean_inst == '1')
    a.config(bg="#aecfee")
    appdata = f'{os.environ["APPDATA"]}\\Yosh'
    print(f"{language[lang[0]][36]} {appdata}")
    if not os.path.exists(appdata):
        os.mkdir(appdata)

    for everything in a.winfo_children():
        everything.destroy()
    os.system('Yosh\\msm_stuff\\how-to-run-msm.png')
    for element in jpg:
        os.system(f'del "{element}"')
    path = os.environ["PATH"]
    admin = ""
    install_font = False
    edit_path = False
    font = 'Windows\\Fonts\\MAR'
    if not os.path.exists(f'C:\\{font}IO Font v3 Solid.otf'):
        admin = language[lang[0]][35] + "\n"
        install_font = True
    if ":\\Yosh" in path:
        admin += language[lang[0]][41] + "\n"
        edit_path = True
    if appdata not in path:
        admin += language[lang[0]][42] + "\n"
        edit_path = True
    title3 = Label(a, text=f"{language[lang[0]][31]}\n{admin}\n{language[lang[0]][32]}\n", bg="#aecfee", font=100)
    title3.grid(row=1, rowspan=5)
    all_button_text = ""
    if edit_path or install_font:
        all_button_text += language[lang[0]][40] + " "  # requires admin perm
    all_button_text += language[lang[0]][37] + " (" # finish installation
    if edit_path:
        all_button_text+= language[lang[0]][38]  # add to path
    if install_font:
        if edit_path:
            all_button_text += " + "
        all_button_text += language[lang[0]][39] # + install font
        font_step4 = partial(step4_appdata, clean_inst, edit_path=False, install_font=True)
        button3_font = Button(a, text=language[lang[0]][40] + " " + language[lang[0]][37] + f" ({language[lang[0]][39]})", command=font_step4, bg="#ff9b69", activebackground="#a9ff91", width=30)
        button3_font.grid(row=3, col=3)
    all_step4 = partial(step4_appdata, clean_inst, edit_path, install_font)
    
    all_button_text += ")"
    button3 = Button(a, text=all_button_text, command=all_step4, bg="#ff9b69", activebackground="#a9ff91", width=30)
    button3.grid(row=3, col=1, columnspan=2)
    
    step4_no_admin = partial(step4_appdata, clean_inst)
    button3_no_admin = Button(a, text=language[lang[0]][37], command=step4_no_admin, activebackground="#a9ff91", width=30)
    button3_no_admin.grid(row=3, col=4)
    
    
    launch_path = partial(launch_path_app, clean_inst)
    button3_launch_path = Button(a, text=language[lang[0]][37], command=launch_path, activebackground="#a9ff91", width=30)
    button3_launch_path.grid(row=4, col=1, columnspan=2)


def step3_local():
    a.config(bg="#aecfee")
    for everything in a.winfo_children():
        everything.destroy()
    msm_stuff = os.path.join('Yosh', 'msm_stuff')
    os.system(os.path.join(msm_stuff, 'how-to-run-msm.png'))
    try:
        for element in jpg:
            os.remove(element)
    except:
        pass
    for o in a.winfo_children():
        o.destroy()
    title3 = Label(a, text=f"{language[lang[0]][31]}\n{language[lang[0]][32]}\n\n{language[lang[0]][33]}\n{language[lang[0]][34]}", bg="#aecfee", font=100)
    title3.grid(row=0)
    button3 = Button(a, text=language[lang[0]][37], command=step4_local, activebackground="#a9ff91", width=30)
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
    title3 = Label(a, text=f"{language[lang[0]][31]}\n{language[lang[0]][32]}\n\n{language[lang[0]][33]}\n{language[lang[0]][34]}", bg="#aecfee", font=100)
    title3.grid(row=0)
    step4 = partial(step4_other, remove_ico)
    button3 = Button(a, text=language[lang[0]][37], command=step4, activebackground="#a9ff91", width=30)
    button3.grid(row=3)


def step2():
    refresh_func()
    a.config(bg="#ff9b69")
    for everything in a.winfo_children():
        everything.destroy()
    font = 'MAR'
    if not os.path.exists(font + 'IO Font v3 Solid.otf'):
        os.rename(font, font + 'IO Font v3 Solid.otf')
    title2 = Label(a, text=language[lang[0]][20], font=300, bg="#ff9b69", height=3)
    title2.grid(row=0, columnspan=10)
    clean = StringVar()
    clean_cb = Checkbutton(a, text=language[lang[0]][21], bg="#ff9b69", variable=clean)  # , width=20) #command=check
    clean_cb.grid(row=1, column=0)
    ico = StringVar()
    no_ico = Checkbutton(a, text=language[lang[0]][22], bg="#ff9b69", variable=ico)  # , width=20) #command=check
    no_ico.grid(row=1, column=1, columnspan=2)
    note2 = Label(a, text=language[lang[0]][23], bg="#ff9b69")
    note2.grid(row=2, columnspan=3)
    title2 = Label(a, text=language[lang[0]][24], font=(None, 13), bg="#ff9b69")  # , font=0.5
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
    path_local2 = Button(a, text=f"{language[lang[0]][28]}\\Yosh", command=step3_local, bg="#ff9999",
                         activebackground="#ff7f7f", width=30)
    path_local2.grid(row=7, column=1)
    other = partial(step3_other, ico.get)
    path_other2 = Button(a, text=language[lang[0]][29], command=other, width=30)
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
        inva = Label(a, text=language[lang[0]][30], bg="#ff9b69", width=30)
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
        run[n] = language[lang[0]][25 + n]
    chosen_language = f'./Yosh/languages/{LANGUAGES.get()}.txt'
    if not os.path.exists(chosen_language):
        chosen_language = './Yosh/languages/English.txt'
    with open(chosen_language, 'rb') as txt1:
        new_lang = txt1.read()
    with open('./Yosh/#language.txt', 'wb') as txt2:
        txt2.write(new_lang)
    if func_called[0] != lang[0]:
        clearConsole()
        func_called[0] = lang[0]
        for some_tkstuff in a.winfo_children():
            some_tkstuff.destroy()
        title = Label(a, text=language[lang[0]][12], font=300, bg="#aecfee", height=3, width=60)
        title.grid(row=0)
        desc = Label(a, text=language[lang[0]][13], font=300, bg="#aecfee", height=3)
        desc.grid(row=1)
        info = Label(a, text=language[lang[0]][14], font=300, bg="#aecfee", height=3)
        info.grid(row=2)
        info2 = Label(a, text=language[lang[0]][15], font=(None, 13), bg="#aecfee")
        info2.grid(row=5)

        Languages = OptionMenu(a, LANGUAGES, *languages)
        Languages["menu"].config(bg="#000000", fg='#ffffff')
        Languages.config(width=15)
        Languages.grid(row=6, column=0, columnspan=2)
        emptya = Label(a, text="  ", font=(None, 1), bg="#aecfee")
        emptya.grid(row=7, column=0)
        refresh = Button(a, text=language[lang[0]][16], command=refresh_func, activebackground="#a9ff91", width=10)
        refresh.grid(row=8, column=0, columnspan=3)
        emptyb = Label(a, text="  ", font=(None, 5), bg="#aecfee")
        emptyb.grid(row=9, column=0)

        joke = Label(a, text=language[lang[0]][17], font=300, bg="#aecfee", height=3)
        joke.grid(row=10)
        launch_step2 = Button(a, text=language[lang[0]][18], command=step2, activebackground="#a9ff91", width=30)
        launch_step2.grid(row=11)
        backend = Label(a, text=language[lang[0]][19], bg="#aecfee")
        backend.grid(row=12)
        for j in range(4, 12):
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
