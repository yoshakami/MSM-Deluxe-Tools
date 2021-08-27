from tkinter import Tk, Label, Button, OptionMenu, StringVar, Checkbutton, DISABLED
# from subprocess import check_output
from functools import partial
from zipfile import ZipFile
# import webbrowser
import shutil
import string
import sys
import os

root = sys.argv[0]
root = os.path.splitext(root)[0]
a = Tk()
a.title("Mario Sports Mix Modding App Installer v" + root.rsplit('v', 1)[-1])
a.minsize(660, 495)
a.maxsize(660, 495)
a.config(bg="#aecfee")  # go to line 500 for the next part of code, then at the bottom and move up through functions

w = a.winfo_screenwidth()
h = a.winfo_screenheight()

languages = (
    'English', 'Français', 'Deutsch (Google Übersetzer)', 'Español (Traductor de google)', 'Italiano (Google Traduttore)',
    'Nederlands (Google Vertalen)', 'Português (Google Tradutor)', 'Pусский (Гугл переводчик)',  # PAL Wii U
    'Polskie (tłumacz Google)', '日本語 (グーグル翻訳)', '中国人 (谷歌翻译)', '한국어 (구글 번역)')
lang = [0]  # change it to your lang if you want : english is 0, french is 1, deutsch is 2 and so on
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
    'pip.exe nicht gefunden. diese Datei ist in Python >= 3.7 enthalten (oder Sie können die Module "pyperclip", "win10toast" und "Pillow" manuell installieren)',
    "Common.zip befindet sich nicht im selben Verzeichnis wie dieses Skript,\nwie zum Teufel wollen Sie die Tools ohne Skript verwenden!?\nDrücken Sie zum Beenden die Eingabetaste...",
    "exe.zip befindet sich nicht im selben Verzeichnis wie dieses Skript,\nIch nehme an, Sie möchten sie dann nicht verwenden.\nDrücken Sie die Eingabetaste, um fortzufahren...",
    "Hey Alter ! Du vermisst jpg.zip, lege es in das gleiche Verzeichnis wie dieses Skript\nDas Installationsprogramm funktioniert nicht ohne diese Bilder, für die ich viel Zeit aufgewendet habe.\nDrücke zum Beenden die Eingabetaste.. .",
    "Willkommen an der Konsole!",
    "Hier sehen Sie, was hinter dem Installer passiert",
    "Die Schaltflächen sind nur hier, um Aktionen zu trennen, damit sie beendet werden",
    f"Wenn Sie auf 'Ich stimme zu' klicken, wird die Größe von 18 jpg an Ihre Bildschirmabmessungen ({w}x{h}) angepasst",
    "Während der Installation werden Zips entpackt und der Inhalt in den Installationspfad Ihres Verzeichnisses verschoben",
    "Es löscht auch nutzlose Daten (außer dem Installationsprogramm, da es sich nicht selbst löschen kann)",
    "Der Installer fügt das Installationsverzeichnis zu PATH hinzu, damit Skripte von überall gestartet werden können!",
    "Willkommen beim Mario Sports Mix Modding App Installer!",
    "ein kostenloser Satz von Skripten, der von Yosh in Python entwickelt wurde",
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
    'Exe verwenden',
    'benutze bat (ein wildes schwarzes Fenster öffnet sich jedes Mal für eine halbe Sekunde, wenn du eine App startest)',
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
    "Beenden Sie die Installation"]
spanish = [
    'pip.exe no encontrado. este archivo se incluye con python> = 3.7 (o puede instalar manualmente los módulos "pyperclip", "win10toast" y "Pillow") ',
    "Common.zip no está en el mismo directorio que este script, \ncómo diablos quieres usar las herramientas sin ningún script? \npresiona enter para salir ...",
    "exe.zip no está en el mismo directorio que este script, \nCreo que no querrás usarlos entonces. \npresiona enter para continuar ...",
    "¡Oye amigo! Te falta jpg.zip, ponlo en el mismo directorio que este script \nel instalador no funcionará sin esas imágenes en las que he pasado una enorme cantidad de tiempo en hacer. \npresiona enter para salir ... . ",
    "¡Bienvenido a la consola!",
    "Aquí puedes ver lo que sucede detrás del instalador",
    "los botones están aquí para separar acciones y dejar que terminen",
    f"Cuando hagas clic en 'Acepto', cambiará el tamaño de 18 jpg a las dimensiones de tu pantalla ({w} x {h})",
    "Durante la instalación, extraerá las cremalleras y moverá su contenido a la ruta de instalación de su directorio",
    "también borrará datos inútiles (excepto el instalador, ya que no puede borrarse a sí mismo jajaja)",
    "¡el instalador agregará el directorio de instalación a PATH, por lo que los scripts podrán iniciarse desde cualquier lugar!",
    "¡Bienvenido al instalador de la aplicación Mario Sports Mix Modding!",
    "un conjunto gratuito de scripts desarrollado por Yosh en Python",
    "si ha pagado por este software, ha sido estafado",
    "Elige tu idioma",
    "Actualizar",
    "Términos del acuerdo",
    "Estoy de acuerdo",
    "(la aplicación se congelará 1 minuto mientras cambia el tamaño de todos los archivos jpg a las dimensiones de su pantalla)",
    "Elija su directorio de instalación",
    "Limpiar el directorio de instalación",
    "No utilice archivos .ico (para otros sistemas operativos que no los admitan)",
    "Nota: 'Local' solo está destinado a ser utilizado con una computadora pública (no la personal) \nDeberá ir a esta carpeta para iniciar una aplicación, ya que no se agregará a la ruta. \n",
    'v-- Seleccione cómo le gustaría iniciar las aplicaciones desde la barra de búsqueda explorer.exe --v',
    'use exe',
    'use bat (una ventana negra salvaje que se abre durante medio segundo cada vez que inicia una aplicación)',
    "otro sistema operativo que no sea Windows (no podrá comprimir ni descomprimir archivos)",
    "Local (directorio móvil)",
    "Otro sistema operativo distinto de Windows",
    "Unidad no válida",
    "Haga clic en este botón para finalizar la instalación :)",
    "una vez hecho esto, puede eliminar el instalador y disfrutar de las herramientas: D",
    "También puede instalar la fuente que apareció en este directorio",
    "ya que la aplicación de ayuda está especialmente diseñada para ello",
    "haga clic en sí para cmd admin perm",
    "instalando en",
    "Termina la instalación"]
italian = [
    'pip.exe non trovato. questo file è incluso con python >= 3.7 (oppure puoi installare manualmente i moduli "pyperclip", "win10toast" e "Pillow")',
    "Common.zip non si trova nella stessa directory di questo script,\ncome diamine vuoi usare gli strumenti senza alcun script!?\npremi invio per uscire...",
    "exe.zip non è nella stessa directory di questo script,\nImmagino che tu non voglia usarli allora.\npremi invio per continuare...",
    "Ehi amico! ti manca jpg.zip, mettilo nella stessa directory di questo script\nl'installer non funzionerà senza quelle immagini che ho impiegato un'enorme quantità di tempo a fare.\npremi invio per uscire.. .",
    "Benvenuto alla console!",
    "Qui puoi vedere cosa sta succedendo dietro l'installatore",
    "i pulsanti sono qui solo per separare le azioni per farle finire",
    f"Quando fai clic su 'Accetto', verrà ridimensionato 18 jpg alle dimensioni dello schermo ({w}x{h})",
    "Durante l'installazione, estrarrà gli zip e sposterà il suo contenuto nel percorso di installazione della directory",
    "cancellerà anche i dati inutili (tranne il programma di installazione in quanto non può cancellarsi da solo lol)",
    "il programma di installazione aggiungerà la directory di installazione a PATH, quindi gli script potranno essere avviati da qualsiasi luogo!",
    "Benvenuto in Mario Sports Mix Modding App Installer!",
    "un set gratuito di script sviluppati da Yosh in Python",
    "se hai pagato per questo software sei stato truffato",
    "Scegli la tua LINGUA",
    "Ricaricare",
    "Termini del contratto",
    "Sono d'accordo",
    "(l'app si bloccherà per 1 minuto mentre ridimensiona tutti i jpg alle dimensioni dello schermo)",
    "Scegli la directory di installazione",
    "Pulisci la directory di installazione",
    "Non utilizzare file .ico (per altri sistemi operativi che non li supportano)",
    "Nota: 'Locale' deve essere utilizzato solo con un computer pubblico (non personale)\ndovrai andare in questa cartella per avviare un'app poiché non verrà aggiunta al percorso.\n",
    'v-- Seleziona come desideri avviare le app dalla barra di ricerca di explorer.exe --v',
    'usa exe',
    "usa bat (una finestra nera selvaggia aperta per mezzo secondo ogni volta che avvii un'app)",
    "sistema operativo diverso da Windows (non sarai in grado di comprimere o decomprimere file)",
    "Locale (directory mobile)",
    "Sistema operativo diverso da Windows",
    "Unità non valida",
    "Fare clic su questo pulsante per terminare l'installazione :)",
    "una volta fatto puoi eliminare il programma di installazione e goderti gli strumenti :D",
    "Puoi anche installare il carattere che è apparso in questa directory,",
    "poiché l'app di aiuto è progettata appositamente per questo",
    "fai clic su sì per cmd admin perm",
    "installazione su",
    "Termina l'installazione"]
dutch = [
    'pip.exe niet gevonden. dit bestand wordt meegeleverd met python >= 3.7 (of u kunt handmatig "pyperclip", "win10toast" en "Pillow" Modules installeren)',
    "Common.zip bevindt zich niet in dezelfde map als dit script,\nhoe wil je in vredesnaam de tools gebruiken zonder enig script!?\ndruk op enter om af te sluiten...",
    "exe.zip staat niet in dezelfde map als dit script,\nIk denk dat je ze dan niet wilt gebruiken.\ndruk op enter om door te gaan...",
    "hey kerel! je mist jpg.zip, zet het in dezelfde map als dit script\nhet installatieprogramma zal niet werken zonder de afbeeldingen waar ik enorm veel tijd aan heb besteed.\ndruk op enter om af te sluiten.. .",
    "Welkom op de console!",
    "Hier kunt u zien wat er achter het installatieprogramma gebeurt",
    "de knoppen zijn er alleen om acties te scheiden om ze te laten eindigen",
    f"Als u op 'Ik ga akkoord' klikt, wordt 18 jpg aangepast aan uw schermafmetingen ({w}x{h})",
    "Tijdens de installatie zal het zips uitpakken en de inhoud verplaatsen naar het installatiepad van uw directory",
    "het zal ook nutteloze gegevens verwijderen (behalve het installatieprogramma omdat het zichzelf niet kan verwijderen lol)",
    "het installatieprogramma voegt de installatiemap toe aan PATH, zodat scripts overal kunnen worden gestart!",
    "Welkom bij Mario Sports Mix Modding App Installer!",
    "een gratis set scripts ontwikkeld door Yosh in Python",
    "als je voor deze software hebt betaald, ben je opgelicht",
    "Kies je taal",
    "Vernieuwen",
    "Voorwaarden",
    "Ik ga akkoord",
    "(de app bevriest 1 minuut omdat alle jpg wordt aangepast aan uw schermafmetingen)",
    "Kies uw installatiemap",
    "Reinig de installatiemap",
    "Gebruik geen .ico-bestanden (voor andere besturingssystemen die ze niet ondersteunen)",
    "Opmerking: 'Lokaal' is alleen bedoeld om te worden gebruikt met een openbare computer (niet uw persoonlijke)\nu zult naar deze map moeten gaan om een ​​app te starten, aangezien deze niet aan het pad wordt toegevoegd.\n",
    'v-- Selecteer hoe u de apps wilt starten vanuit de zoekbalk van explorer.exe --v',
    'gebruik exe',
    'gebruik bat (een wild zwart venster dat een halve seconde opengaat elke keer dat je een app start)',
    "ander besturingssysteem dan Windows (u kunt geen bestanden comprimeren of decomprimeren)",
    "Lokaal (verplaatsbare map)",
    "Ander besturingssysteem dan Windows",
    "Ongeldige schijf",
    "Klik op deze knop om de installatie te voltooien :)",
    "als het klaar is, kun je het installatieprogramma verwijderen en genieten van de tools :D",
    "U kunt ook het lettertype installeren dat in deze map verscheen,"
    "omdat de help-app er speciaal voor is ontworpen",
    " klik ja om cmd admin perm ",
    "installeren op",
    "Beëindig de installatie"]
portuguese = [
    'pip.exe não encontrado. este arquivo está incluído no python> = 3.7 (ou você pode instalar manualmente os módulos "pyperclip", "win10toast" e "Pillow") ',
    "Common.zip não está no mesmo diretório que este script, \ncomo diabos você deseja usar as ferramentas sem nenhum script!? \nPressione Enter para sair ...",
    "exe.zip não está no mesmo diretório que este script, \nAcho que você não deseja usá-los. \nPressione Enter para continuar ...",
    "Ei cara! está faltando jpg.zip, coloque-o no mesmo diretório que este script \no instalador não funcionará sem essas imagens que eu gastei muito tempo para fazer. \nprima enter para sair .. . ",
    "Bem-vindo ao console!",
    "Aqui você pode ver o que está acontecendo por trás do instalador",
    "os botões estão aqui apenas para separar ações para deixá-los terminar",
    f"Quando você clicar em 'Concordo', será redimensionado 18 jpg para as dimensões da tela ({w} x {h})",
    "Durante a instalação, ele extrairá zips e moverá seu conteúdo para o caminho de instalação do diretório",
    "também vai deletar dados inúteis (exceto o instalador, pois não pode deletar a si mesmo lol)",
    "o instalador irá adicionar o diretório de instalação ao PATH, então os scripts poderão ser iniciados de qualquer lugar!",
    "Bem-vindo ao instalador do aplicativo Mario Sports Mix Modding!",
    "um conjunto gratuito de Scripts desenvolvido por Yosh em Python",
    "se você pagou por este software, foi enganado",
    "Escolha o seu idioma",
    "Atualizar",
    "Termos do acordo",
    "Eu concordo",
    "(o aplicativo irá congelar 1 minuto enquanto está redimensionando todo o jpg para as dimensões da tela)",
    "Escolha o seu diretório de instalação",
    "Limpe o diretório de instalação",
    "Não use arquivos .ico (para outro sistema operacional que não os suporte)",
    "Nota: 'Local' destina-se apenas a ser usado com um computador público (não o seu pessoal) \nvocê terá que ir para esta pasta para iniciar um aplicativo, pois ele não será adicionado ao caminho. \n",
    'v-- Selecione como você gostaria de iniciar os aplicativos da barra de pesquisa do explorer.exe --v',
    'use exe',
    'use bat (uma janela preta selvagem aberta por meio segundo cada vez que você iniciar um aplicativo)',
    "outro sistema operacional além do Windows (você não poderá compactar ou descompactar arquivos)",
    "Local (diretório móvel)",
    "Outro sistema operacional além do Windows",
    "Unidade inválida",
    "Clique neste botão para terminar a instalação :)",
    "uma vez feito isso, você pode excluir o instalador e aproveitar as ferramentas: D",
    "Você também pode instalar a fonte que apareceu neste diretório,",
    "já que o aplicativo de ajuda é especialmente projetado para isso",
    "clique sim para cmd admin perm",
    "instalando em",
    "Conclua a instalação"]
russian = [
    'pip.exe не найден. этот файл включен в python> = 3.7 (или вы можете вручную установить модули "pyperclip", "win10toast" и "Pillow") ',
    "Common.zip не находится в том же каталоге, что и этот скрипт, \nкак, черт возьми, вы хотите использовать инструменты без скрипта!? \nНажмите Enter для выхода ...",
    "exe.zip находится не в том же каталоге, что и этот скрипт, \nЯ думаю, вы не хотите их использовать в таком случае. \nнажмите Enter, чтобы продолжить ...",
    "Эй, чувак! тебе не хватает jpg.zip, поместите его в тот же каталог, что и этот скрипт. \nинсталлятор не будет работать без тех изображений, на которые я потратил огромное количество времени. \nНажмите Enter для выхода .. . ",
    "Добро пожаловать в консоль!",
    "Здесь вы можете увидеть, что происходит за установщиком",
    "кнопки предназначены только для разделения действий, чтобы они закончились",
    f'Когда вы нажмете" Я согласен ", размер изображения изменится на 18 jpg до размеров вашего экрана ({w} x {h})',
    "Во время установки он распакует zip-архивы и переместит свое содержимое в путь установки вашего каталога",
    "он также удалит ненужные данные (кроме установщика, так как он не может удалить себя lol)",
    "установщик добавит каталог установки в PATH, так что скрипты можно будет запускать отовсюду!",
    "Добро пожаловать в установщик приложения для моддинга Mario Sports Mix!",
    "бесплатный набор скриптов, разработанный Йошем на Python",
    "если вы заплатили за это программное обеспечение, вас обманули",
    "Выберите свой язык",
    "Обновить",
    "Условия соглашения",
    "Я согласен",
    "(приложение остановится на 1 минуту, поскольку оно изменяет размер всех jpg до размеров вашего экрана)",
    "Выберите каталог для установки",
    "Очистить каталог установки",
    "Не используйте файлы .ico (для других ОС, не поддерживающих их)",
    "Примечание: 'Local' предназначен только для использования с общедоступным компьютером (не вашим личным) \n вам нужно будет перейти в эту папку, чтобы запустить приложение, поскольку оно не будет добавлено в путь. \n",
    'v-- Выберите способ запуска приложений из строки поиска explorer.exe --v',
    'использовать exe',
    'использовать bat (дикое черное окно открывается на полсекунды при каждом запуске приложения)',
    "другая ОС, кроме Windows (вы не сможете сжимать или распаковывать файлы)",
    "Локальный (подвижный каталог)",
    "Другая ОС, кроме Windows",
    "Недействительный диск",
    "Нажмите эту кнопку, чтобы завершить установку :)",
    "как только это будет сделано, вы можете удалить установщик и пользоваться инструментами: D",
    "Вы также можете установить шрифт, который появился в этом каталоге",
    "поскольку приложение помощи разработано специально для этого",
    'нажмите" Да ", чтобы получить команду" Администратор cmd ',
    "установка в",
    "Завершить установку"]
polish = [
    'Nie znaleziono pliku pip.exe. ten plik jest dołączony do Pythona >= 3.7 (możesz też ręcznie zainstalować moduły "pyperclip", "win10toast" i "Pillow")',
    "Common.zip nie znajduje się w tym samym katalogu co ten skrypt,\njak u licha chcesz używać narzędzi bez żadnego skryptu!?\nnaciśnij enter, aby wyjść...",
    "exe.zip nie znajduje się w tym samym katalogu co ten skrypt,\nWydaje mi się, że nie chcesz ich wtedy używać.\nNaciśnij enter, aby kontynuować...",
    "hej koleś! brakuje ci pliku jpg.zip, umieść go w tym samym katalogu co ten skrypt\ninstalator nie będzie działał bez tych obrazów, na których wykonanie spędziłem ogromną ilość czasu.\nnaciśnij enter, aby wyjść.. ",
    "Witamy w konsoli!",
    "Tutaj możesz zobaczyć, co dzieje się za instalatorem",
    "przyciski są tu tylko po to, aby oddzielić akcje i pozwolić im zakończyć",
    f"Kiedy klikniesz 'Zgadzam się', rozmiar 18 jpg zostanie zmieniony na wymiary twojego ekranu ({w}x{h})",
    "Podczas instalacji rozpakuje zipy i przeniesie ich zawartość do ścieżki instalacyjnej twojego katalogu",
    "usunie również bezużyteczne dane (poza instalatorem, ponieważ nie może sam usunąć lol)",
    "instalator doda katalog instalacyjny do PATH, dzięki czemu skrypty będą mogły być uruchamiane z dowolnego miejsca!",
    "Witamy w instalatorze aplikacji Mario Sports Mix Modding!",
    "darmowy zestaw Skryptów opracowanych przez Yosha w Pythonie",
    "jeśli zapłaciłeś za to oprogramowanie, zostałeś oszukany",
    "Wybierz swój język",
    "Odświeżać",
    "Warunki porozumienia",
    "Zgadzam się",
    "(aplikacja zatrzyma się na 1 minutę, ponieważ zmienia rozmiar wszystkich jpg do wymiarów ekranu)",
    "Proszę wybrać katalog instalacyjny",
    "Wyczyść katalog instalacyjny",
    "Nie używaj plików .ico (dla innych systemów operacyjnych, które ich nie obsługują)",
    "Uwaga: 'Lokalny' jest przeznaczony tylko do użytku z komputerem publicznym (nie osobistym)\nbędziesz musiał przejść do tego folderu, aby uruchomić aplikację, ponieważ nie zostanie ona dodana do ścieżki.\n",
    'v-- Wybierz sposób uruchamiania aplikacji z paska wyszukiwania explorer.exe --v',
    'użyj exe',
    "użyj bat (dzikiego czarnego okna otwierającego się na pół sekundy za każdym razem, gdy uruchamiasz aplikację)",
    "inny system operacyjny niż Windows (nie będziesz mógł kompresować ani dekompresować plików)",
    "Lokalny (katalog ruchomy)",
    "Inny system operacyjny niż Windows",
    "Nieprawidłowy Dysk",
    "Kliknij ten przycisk, aby zakończyć instalację :)",
    "po zakończeniu możesz usunąć instalator i cieszyć się narzędziami :D",
    "Możesz też zainstalować czcionkę, która pojawiła się w tym katalogu",
    "ponieważ aplikacja pomocy jest specjalnie do tego zaprojektowana",
    " kliknij tak aby cmd admin perm",
    "instalacja do",
    "Zakończ instalację"]
japanese = [
    'pip.exe が見つかりません。このファイルは python >= 3.7 に含まれています (または、「pyperclip」、「win10toast」、および「Pillow」モジュールを手動でインストールできます)',
    "Common.zip はこのスクリプトと同じディレクトリにありません。\nスクリプトなしでツールを使用するにはどうすればよいですか?\nEnter キーを押して終了します...",
    "exe.zip はこのスクリプトと同じディレクトリにありません。\nそれらを使用したくないと思います.\n続行するには Enter キーを押してください...",
    "ねえねえ、jpg.zip がありません。このスクリプトと同じディレクトリに置いてください\nインストーラーは、私が膨大な時間を費やした画像がないと機能しません。\n終了するには Enter キーを押してください.. .",
    "コンソールへようこそ!",
    "ここでは、インストーラーの背後で何が起こっているかを確認できます",
    "ボタンは、アクションを分離して終了させるためのものです",
    f"[同意する] をクリックすると、18 jpg が画面サイズ ({w}x{h}) にサイズ変更されます",
    "インストール中に、zip を抽出し、そのコンテンツをディレクトリ インストール パスに移動します",
    "不要なデータも削除します (インストーラーは自分自身を削除できないため、インストーラーを除く)",
    "インストーラーはインストール ディレクトリを PATH に追加するので、スクリプトはどこからでも起動できるようになります!",
    "マリオ スポーツ ミックス モッディング アプリ インストーラーへようこそ!",
    "Python で Yosh によって開発されたスクリプトの無料セット",
    "このソフトウェアにお金を払ったことがあるなら、あなたは詐欺に遭っています",
    "言語を選択してください",
    "リフレッシュ",
    "契約条件",
    "同意する",
    "(すべての jpg を画面サイズにサイズ変更しているため、アプリは 1 分間フリーズします)",
    "インストールディレクトリを選択してください",
    "インストール ディレクトリをクリーンアップ",
    ".ico ファイルを使用しないでください (それらをサポートしていない他の OS の場合)",
    "注: 'ローカル' は、公共のコンピューター (個人用ではありません) でのみ使用することを目的としています\nアプリを起動するには、このフォルダーに移動する必要があります。パスには追加されないためです。\n",
    'v-- explorer.exe 検索バー --v からアプリを起動する方法を選択します',
    "exeを使用する",
    'batを使用する (アプリを起動するたびに 0.5 秒間開く野生の黒いウィンドウ)',
    "Windows 以外の OS (ファイルの圧縮または解凍はできません)",
    "ローカル (移動可能なディレクトリ)",
    "Windows以外のOS",
    "無効なドライブ",
    "このボタンをクリックしてインストールを終了します:)",
    "完了したら、インストーラーを削除してツールを楽しむことができます:D",
    "このディレクトリにあるフォントをインストールすることもできます",
    "ヘルプ アプリはそのために特別に設計されているため",
    " はいをクリックして cmd admin perm へ",
    "インストール先",
    "インストールを終了する"]
chinese = [
    '找不到pip.exe。此文件包含在 python >= 3.7 中（或者您可以手动安装“pyperclip”、“win10toast”和“Pillow”模块）',
    "Common.zip 和这个脚本不在同一个目录下，\n你想怎么使用没有任何脚本的工具！？\n按回车退出...",
    "exe.zip 与此脚本不在同一目录中，\n我猜你那时不想使用它们。\n按 Enter 继续...",
    "嘿，伙计！您缺少 jpg.zip，请将其放在与此脚本相同的目录中\n如果没有我花费大量时间制作的那些图像，安装程序将无法运行。\n按 Enter 退出.. .",
    "欢迎来到控制台！",
    "在这里你可以看到安装程序背后发生了什么",
    "按钮只是在这里分开动作，让它们完成",
    f"当您点击'我同意'时，它会根据您的屏幕尺寸 ({w}x{h}) 调整 18 jpg",
    "在安装过程中，它会解压 zip 并将其内容移动到您的目录安装路径",
    "它还会删除无用的数据（安装程序除外，因为它无法删除自己，哈哈）",
    "安装程序会将安装目录添加到 PATH，这样脚本就可以从任何地方启动了！",
    "欢迎使用 Mario Sports Mix Modding App Installer！",
    "Yosh 用 Python 开发的一组免费脚本",
    "如果你为这个软件付费，你就被骗了",
    "选择你的语言",
    "刷新",
    "协议条款",
    "我同意",
    "（该应用程序将冻结 1 分钟，因为它会将所有 jpg 的大小调整为您的屏幕尺寸）",
    "请选择您的安装目录",
    "清理安装目录",
    "不要使用 .ico 文件（对于不支持它们的其他操作系统）",
    "注意：'Local' 仅用于公共计算机（不是您的个人计算机）\n您必须转到此文件夹才能启动应用程序，因为它不会被添加到路径中。\n",
    'v-- 从 explorer.exe 搜索栏选择您希望如何启动应用程序 --v',
    '使用 exe',
    '使用 bat（每次启动应用程序时都会打开一个狂野的黑色窗口半秒）',
    "Windows 以外的其他操作系统（您将无法压缩或解压缩文件）",
    "本地（可移动目录）",
    "Windows 以外的其他操作系统",
    "无效驱动器",
    "点击此按钮完成安装:)",
    "完成后，您可以删除安装程序并享受这些工具：D",
    "你也可以安装出现在这个目录下的字体",
    "因为帮助应用程序是专门为它设计的",
    "点击yes to cmd admin perm",
    "安装到",
    "完成安装"]
korean = [
    'pip.exe를 찾을 수 없습니다. 이 파일은 python> = 3.7에 포함되어 있습니다 (또는 "pyperclip", "win10toast"및 "Pillow"모듈을 수동으로 설치할 수 있음) ',
    "Common.zip은이 스크립트와 동일한 디렉토리에 없습니다.\n 스크립트없이 도구를 사용 하시겠습니까?\n 종료하려면 Enter 키를 누르십시오 ...",
    "exe.zip이이 스크립트와 동일한 디렉토리에 없습니다.\n 그러면 사용하지 않으실 것 같습니다.\n 계속하려면 Enter 키를 누르십시오 ...",
    "야, 친구! jpg.zip이 누락되었습니다.이 스크립트와 동일한 디렉토리에 넣으십시오.\n 내가 수행하는 데 엄청난 시간을 소비 한 이미지가 없으면 설치 프로그램이 작동하지 않습니다.\n 종료하려면 Enter 키를 누르십시오 .. . ",
    "콘솔에 오신 것을 환영합니다!",
    "여기에서 설치 프로그램 뒤에서 일어나는 일을 볼 수 있습니다.",
    "버튼은 완료 할 수 있도록 작업을 분리하기 위해 여기에 있습니다.",
    f" '동의 함'을 클릭하면 화면 크기 ({w} x {h})에 맞게 18jpg 크기가 조정됩니다.",
    "설치하는 동안 압축을 풀고 해당 내용을 디렉토리 설치 경로로 이동합니다.",
    "쓸모없는 데이터도 삭제됩니다 (설치 프로그램은 스스로 삭제할 수 없기 때문에 제외)",
    "설치 프로그램은 PATH에 설치 디렉토리를 추가하므로 어디서나 스크립트를 실행할 수 있습니다!",
    "마리오 스포츠 믹스 모딩 앱 설치 프로그램에 오신 것을 환영합니다!",
    "Yosh가 Python으로 개발 한 무료 스크립트 세트",
    "이 소프트웨어에 대한 비용을 지불했다면 사기를당했습니다.",
    "당신의 언어를 고르시 오",
    "새롭게 하다",
    "계약 조건",
    "나는 동의한다",
    "(모든 jpg의 크기를 화면 크기로 조정하기 때문에 앱이 1 분 동안 멈춤)",
    "설치 디렉토리를 선택하십시오",
    "설치 디렉토리 정리",
    ".ico 파일을 사용하지 마십시오 (지원하지 않는 다른 OS의 경우)",
    "참고 : '로컬'은 개인 컴퓨터가 아닌 공용 컴퓨터에서만 사용할 수 있습니다.\n 앱이 경로에 추가되지 않으므로이 폴더로 이동하여 앱을 실행해야합니다.\n",
    'v-- explorer.exe 검색 창에서 앱 실행 방법 선택 --v',
    'exe를 사용하십시오 ',
    'bat를 사용하십시오 (앱을 실행할 때마다 0.5 초 동안 검은 색 창이 열립니다)',
    "Windows 이외의 OS (파일을 압축하거나 압축 해제 할 수 없음)",
    "로컬 (이동 가능한 디렉토리)",
    "Windows 이외의 OS",
    "잘못된 드라이브",
    "설치를 완료하려면이 버튼을 클릭하십시오. :)",
    "완료되면 설치 프로그램을 삭제하고 도구를 즐길 수 있습니다. : D",
    "이 디렉토리에 나타난 글꼴을 설치할 수도 있습니다.",
    "도움말 앱이 특별히 설계 되었기 때문에",
    "cmd admin perm에 예를 클릭하십시오",
    "설치",
    "설치 완료"]
language = (english, french, german, spanish, italian, dutch, portuguese, russian, polish, japanese, chinese, korean)


def input_lang():
    return input('Languages Available:\n0: English\n1: French (Français)\n2: German (Deutsch)\n3: Spanish (Español)\n4: Italian (Italiano)\n5: Dutch (Nederlands)\n6: Portuguese (Português)\n7: Russian (Pусский)\n8: Polish (Polskie)\n9: Japanese (日本語)\n10: Chinese (中国人)\n11: Korean (한국어)\n\nheyy, type your language number : ')


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
        input(language[int(input_lang()[0])][0])
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
apps = ['arc.py', 'brsar.pyw', 'bstick.pyw', 'c.py', 'dec.py', 'dump.py', 'hexf.py', 'int.py', 'iso.py', 'isox.py',
        'lh.py', 'map.pyw', 'msm.pyw', 'msmhelp.pyw', 'p.py', 'pack.py', 'png.py', 'rEtUrN-tExT.py',
        'sizeC.pyw', 't.py', 'tex.py', 'tex3.pyw', 'thp.pyw', 'trib.py', 'vaporwave.py', 'web.pyw', 'x.py', 'yt.pyw']
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
                bat_file.write(bat_code() + f'setx path "{path};{letter}:\\Yosh;" /M')

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
    for el in delete:
        if os.path.exists(el):
            os.system(f'del "{el}"')
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
            bat_file.write(bat_code() + f'setx path "{path};{os.environ["APPDATA"]}\\Yosh;" /M')

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
    with open(f'./Yosh/lang/{LANGUAGES.get()}.txt', 'rb') as txt1:
        new_lang = txt1.read()
    with open('./Yosh/#language.txt', 'wb') as txt2:
        txt2.write(new_lang)
    if func_called[0] != lang[0]:
        clearConsole()
        func_called[0] = lang[0]
        for some_tkstuff in a.winfo_children():
            some_tkstuff.destroy()
        title = Label(a, text=language[lang[0]][11], font=300, bg="#aecfee", height=3, width=70)
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
