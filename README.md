# MSM-Deluxe-Tools
Set of more than 20 python scripts used to edit Mario Sports Mix files or any Wii game !

I wrote these scripts alone and keep maintaining them up to date by adding new scripts/fixing bugs/adding features/cleaning code

You will need <a href="https://szs.wiimm.de/download.html#vers">Wiimms SZS Tools</a>, <a href="https://wit.wiimm.de/download.html#vers">Wiimms ISO Tools</a>, and <a href="https://www.python.org/downloads/release/python-392#files">python 3.X</a>.

for the modules pyperclip, win10toast and Pillow, the installer should install them automatically. If not, in cmd or your terminal type 
```python" -m pip install --upgrade pip
pip install Pillow
pip install requests
pip install pyperclip
pip install win10toast
pip install win10toast_click
```
(linux users have to do it with pip3, and probably install tkinter)

if you plan looking at the source code, be aware that they are written to be used in C:/Yosh. the installer's job is to edit these paths (and also add assets)
the reason why path is not relative is because the tools are being added to %path% environment variable, in order to be used everywhere
you can easily change the language with #language.txt or from the main menu

All scripts have a special utility, sometimes it's just for fun, or very useful

they are all independent scripts, they just need to access the config file named 'a' (bstick + checkbuttons), or some png (especially for msmhelp, I made all these png) and of course the icons and #language.txt

if you want to know what's happening when you launch an app by the explorer navbar, it simply run an exe that will run a vbs which will state wether or not the app needs a console, make that console associated with the app on the taskbar, and will make it an alone process by launching a .lnk shortcut file of the python script, so there's a custom icon on the taskbar

## if the installer doesn't open
check what the console says
if it instantly closes, run "run this if installer doesn't open.bat" and check what the console says
the last option is to get in contact with me (yosh) either by discord, or your preferred way.

## why is there C programming here ?
in order for the scripts to be launched from everywhere, I needed to use files with an extension in %pathext% BUT explorer.exe has a modified pathext environment variable that we can't edit, and it only contains .exe, .com, and .bat
therefore, I developped programs in C that would launch the apps. It's been automated in a python scripts, but the two .c files in the source code are not automated and manually edited to launch msm_cli.py if any arg has been added after the exe name.
(yep, I programmed my own version of strcat, you shouldn't rely too much libraries if you're doing C programming, as strcat was splitting args randomly after a dot or some other characters)
if you plan to use .bat instead of exe, you will need to type "msm_cli.py" instead of msm in order to use the command line tools.

## scripts description
arc.py -----------  arc extract and compress, creates U8 archive with/without compression

brsar.pyw ------- Every Game Brsar Patcher

bstick.pyw ------ Change bstick colour

c.py ------------- Compress files in cwd

dump.py -------- Dump all textures to png

hexf.py --------- Convert decimal to hex-float

isox.py --------- MSM iso/wbfs extract and compress

lh.py ----------- MSM files extract and compress

map.pyw -------- MSM Symbol Map Viewer

msm.pyw -------- Mario Sports Mix Modding App Menu

msmhelp.pyw ---- Help pictures I made

p.py ---------------- Png texture replace (CLI no png extension)

pack.py ------------- Pack all edited png's dumped with dump.py into a brres, or an arc file (also works with TPL files !)

png.py -------------- Png texture replace (CLI with png extension)

rEtUrN-tExT.py ----- CaPiTaLiSe

sizeC.pyw ----------- Prints C:\pagefile.sys, C:\hiberfil.sys, and C:\swapfile.sys filesize

slot.py -------------- Change a character slot by renaming all its files in cwd (it will close automatically after start if no character mot or mdl files are found in the cwd)

t.py ----------------- Encoded texture replace (CLI)

tex.py --------------- Encode png to tex0

tex3.py -------------- Fix all textures to version 3

trib.py --------------- Change root bone attributes

vaporwave.py ------- V a p o r w a v e

web.pyw ------------ Website

x.py ----------------- Extract files in cwd

yt.pyw --------------- YT Videos Thumbnails Download
