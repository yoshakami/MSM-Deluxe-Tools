# MSM-Deluxe-Tools
Set of more than 20 python scripts used to edit Mario Sports Mix files or any Wii game !

I wrote these scripts alone and keep maintaining them up to date by adding new scripts/fixing bugs/adding features/cleaning code

You will need <a href="https://szs.wiimm.de/download.html#vers">Wiimms SZS Tools</a>, <a href="https://wit.wiimm.de/download.html#vers">Wiimms ISO Tools</a>, and <a href="https://www.python.org/downloads/release/python-392#files">python 3.X</a>
for the modules pyperclip, win10toast and Pillow, the installer should install them automatically. If not, in cmd or your terminal type ```pip install pyperclip```, ```pip install win10toast```  and ```pip install Pillow```

if you plan looking at the source code, be aware that they are written to be used in C:/Yosh. the installer's job is to edit these paths (and also add assets)
the reason why path is not relative is because the tools are being added to %path% environment variable, in order to be used everywhere
you can easily change the language with #lang.txt

They all have a special utility, sometimes it's just for fun, or very useful

they are all independent scripts, they just need to access the config file named 'a' (bstick + checkbuttons), or some png (especially for msmhelp, I made all these png)


arc.py ----------- arc extract and compress, creates U8 archive with/without compression

brsar.pyw ------- Every Game Brsar Patcher

bstick.pyw ------ Change bstick colour

c.py ------------- Compress files in cwd

dump.py -------- Dump all textures to png

hexf.py --------- Convert decimal to hex-float

isox.py --------- MSM iso/wbfs extract and compress

lh.py ----------- MSM files extract and compress

map.pyw -------- MSM Symbol Map Viewer

msm.pyw -------- Mario Sports Mix Modding App Menu

msmhelp.pyw ---- Help pictures I made

msmshortcuts.pyw- Shortcuts (file name and full title)

p.py ---------------- Png texture replace (CLI no png extension)

png.py -------------- Png texture replace (CLI with png extension)

rEtUrN-tExT.py ----- CaPiTaLiSe

t.py ----------------- Encoded texture replace (CLI)

tex.py --------------- Encode png to tex0

tex3.py -------------- Fix all textures to version 3

trib.py --------------- Change root bone attributes

vaporwave.py ------- V a p o r w a v e

web.pyw ------------ Website

x.py ----------------- Extract files in cwd
