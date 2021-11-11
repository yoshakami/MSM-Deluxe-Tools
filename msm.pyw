import os
import webbrowser
# from random import randint
from subprocess import Popen
from winsound import PlaySound
from tkinter.filedialog import askdirectory
from tkinter import Button, Label, Entry, OptionMenu, Tk, Canvas, PhotoImage, DISABLED, StringVar, _setit

if ':\\Windows' in os.getcwd():
    os.chdir(os.environ['userprofile'] + '\\Desktop')

with open('C:\\Yosh\\#language.txt', 'r', encoding="utf-8") as txt:
    language = txt.read()
    language = [''] + language.splitlines()

start = int(language[1].split(":")[1])
a = Tk()
a.title(language[start + 2] + " v0.91")
a.minsize(680, 495)
a.maxsize(680, 495)
a.config(bg="#aecfee")
a.iconbitmap('C:\\Yosh\\msm_stuff\\msm.ico')

run = [f'{language[start + 26]} (c.py)', f'{language[start + 27]} (x.py)', f'{language[start + 28]} (tex3.pyw)',
       f'{language[start + 29]} (hexf.py)', f'{language[start + 30]} (dec.py)', f'{language[start + 31]} (int.py)',
       f'{language[start + 32]} (rEtUrN-tExT.py)', f'{language[start + 33]} (vaporwave.py)',
       f'{language[start + 34]} (yt.pyw)', f'{language[start + 35]} (sizeC.pyw)', f'{language[start + 41]} (slot.py)',
       f'{language[start + 36]} (p.py)', f'{language[start + 37]} (t.py)', f'{language[start + 38]} (png.py)'
       ]
RUN = StringVar()
RUN.set(language[start + 25])
Run = OptionMenu(a, RUN, *run)
Run["menu"].config(bg="#000000", fg='#ffffff')

language_list = [
    'English', 'Français', 'Deutsch', 'Español', 'Italiano',
    'Nederlands', 'Português', 'Pусский',  # PAL Wii U
    'Polskie', '日本語', '中国人', '한국어']
languages = []
for lang in language_list:
    if os.path.exists(f'C:\\Yosh\\lang\\{lang}.txt'):
        languages.append(lang)
LANGUAGES = StringVar()
LANGUAGES.set(language[start + 21])  # Change Language
Languages = OptionMenu(a, LANGUAGES, *languages)
Languages["menu"].config(bg="#000000", fg='#ffffff')
Languages.config(width=15)

random = (
    'question_mark_coin.wav', 'gnomed.wav',
    f'os.environ["ProgramFiles"]\\Internet Explorer\\iexplore.exe',
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    'https://cdn.discordapp.com/attachments/604971224040472577/831235648886407188/rick.gif',
    'https://www.youtube.com/watch?v=hJxFfeyyIXE',
    'https://cdn.discordapp.com/attachments/604971224040472577/831238407971274853/rick.png',
    'https://gamepadviewer.com/', 'https://www.youtube.com/watch?v=vCbwXQuHAIE',  # Waluigi sounds
    'https://www.youtube.com/watch?v=GPMq_PxMTUI&list=PLGr95qH5dmjDiy8NZ8xNA7HE57JyMSU7y&index=18',
    'https://www.youtube.com/watch?v=tHjwySePzH0&list=PLk28dkfJOGjBWGTK6MP6m3qNRIc88VES9&index=37',
    'https://www.youtube.com/watch?v=kE8xdRjxuIs', 'https://www.youtube.com/watch?v=4X4DAg9K-co',  # Wario sounds
    'https://www.youtube.com/watch?v=t7qdHQRJjeE', 'https://www.youtube.com/watch?v=ZS8FLG3kLQc',  # Pizza Pasta
    'https://www.youtube.com/watch?v=Mr8h_T4UPEA', 'https://www.youtube.com/watch?v=utRC8rZSiBI',  # Wii Sports
    'https://www.youtube.com/watch?v=U2SpYoH2GDY', 'https://www.youtube.com/watch?v=K0kvlULMBQ8',  # Pizza Pasta and SMBWii meme
    'https://www.youtube.com/watch?v=Fc1P-AEaEp8&list=PL_90hJucBAcPmFxcbTea81OKGkQevH2F9&index=5',  # meme playlist
    'https://www.youtube.com/watch?v=Til6kcoY0Yk', 'https://www.youtube.com/watch?v=Ps-XsGP5QO4',  # nyanya and vector U
    'https://www.youtube.com/watch?v=fyoH_EH4QHI', 'https://www.youtube.com/watch?v=CinHish38Lc',  # noteblock and guesswhatmusic
    'https://www.youtube.com/watch?v=IgA4AeaG1Cg', 'https://www.youtube.com/watch?v=Xdr2mTHS_Sc',  # Player2 and VGR
    'https://www.youtube.com/watch?v=getEE8cDlGM', 'https://www.youtube.com/watch?v=hZzwIdaRQwk',  # Thomniverse and NintegaDario
    'https://www.youtube.com/watch?v=nNMfGLMvc14', 'https://www.youtube.com/watch?v=-GNMe6kF0j0',  # CG5 and Goblin From Mars
    'https://www.youtube.com/watch?v=YqrxIimmiqs', 'https://www.youtube.com/watch?v=WInN2ljOnSU',  # TheFatRat and Alan Walker
    'https://www.youtube.com/watch?v=wbYM2Ax3gS8', 'https://www.youtube.com/watch?v=EAvYUm57vI8',  # pepensow and sheddy Splatoon
    'https://www.youtube.com/watch?v=C_fA9JQJj1M', 'https://www.youtube.com/watch?v=4NLD6NDcs_k',  # Gametrack Remixes and Mayro alt
    'https://www.youtube.com/watch?v=7D9MwBW5VaQ', 'https://www.youtube.com/watch?v=39enH5NI2zY',  # Amazing Gaming Music and Yume
    'https://www.youtube.com/watch?v=x8eu2YzTKh4', 'https://www.youtube.com/watch?v=hxjkUzFzshE',  # Acid-Notation and Dominic Ninmark
    'https://www.youtube.com/watch?v=NpC9BRVx-Oc', 'https://www.youtube.com/watch?v=AU1TvJ124w0',  # Qumu and guesswhatmusic
    'https://www.youtube.com/watch?v=W0h6c7Lbfdc', 'https://www.youtube.com/watch?v=D984mRYiBkw',  # Raymusique and EliteMeats Music
    'https://www.youtube.com/watch?v=ywXf_sENMYY', 'https://www.youtube.com/watch?v=t3Hz36cPIJA')  # NOQQYSC


def question_mark():
    rewrite = False
    default_size = 18  # total config size including all apps reading it
    with open('C:\\Yosh\\a', 'r+b') as config:
        size = os.path.getsize('C:\\Yosh\\a')
        for n in range(size, default_size):
            config.write(b'0')
        # ints = []
        config.seek(default_size)
        data = config.read()
        if len(data) != len(random):  # if user didn't triggered all events, trigger the next from the list
            config.seek(len(data))
            if not data:  # if the string is empty
                play(0)
                config.write(b'\x00')
            else:
                play(data[-1] + 1)
                config.write(bytes(chr(data[-1] + 1), 'latin-1'))
            # tu regardes le dernier octet écrit et tu lances random[octet+1]
            # it looks at the last byte and adds one, to play the list in loop
        else:
            config.seek(0)
            content = config.read(default_size)
            rewrite = True
            # this used to play 50 times random events then rewrite config, but as the list is too big now it's better to rewrite
            # config.seek(default_size)
            # count = config.read(1)[0]
            # config.seek(default_size)
            # config.write(bytes(chr(count + 1), 'latin-1'))
            # if count > 50:
            #     config.seek(0)
            #     content = config.read(default_size)
            #    rewrite = True
            # # for j in range(len(data)):
            # #    ints.append(data[j])
            # i = randint(0, len(data))
            # while i == data[0]:
            #    i = randint(0, len(data))
            # config.write(bytes(chr(i), 'latin-1'))
            # play(i)
    if rewrite:
        with open('C:\\Yosh\\a', 'wb') as config2:
            config2.write(content)
            question_mark()


def play(num):
    if num in [0, 1]:
        PlaySound(random[num], 1)
    elif num in [2]:
        Popen(random[num])
    else:
        webbrowser.open(random[num])


def refresh():
    with open('C:\\Yosh\\#language.txt', 'r', encoding="utf-8") as text:
        language = text.read()
        language = [''] + language.splitlines()
    run = [f'{language[start + 26]} (c.py)', f'{language[start + 27]} (x.py)', f'{language[start + 28]} (tex3.pyw)',
           f'{language[start + 29]} (hexf.py)', f'{language[start + 30]} (dec.py)', f'{language[start + 31]} (int.py)',
           f'{language[start + 32]} (rEtUrN-tExT.py)', f'{language[start + 33]} (vaporwave.py)',
           f'{language[start + 34]} (yt.pyw)', f'{language[start + 35]} (sizeC.pyw)', f'{language[start + 41]} (slot.py)',
           f'{language[start + 36]} (p.py)', f'{language[start + 37]} (t.py)', f'{language[start + 38]} (png.py)'
           ]
    Run['menu'].delete(0, 'end')

    # Insert list of new options (tk._setit hooks them up to var)
    for app in run:
        Run['menu'].add_command(label=app, command=_setit(RUN, app))

    ltitle.config(text=language[start + 3])
    lp.config(text=language[start + 4])
    lt.config(text=language[start + 5])
    lbrsar.config(text=language[start + 6])
    llh.config(text=language[start + 7])
    lweb.config(text=language[start + 8])
    lisox.config(text=language[start + 9])
    ldump.config(text=language[start + 10])
    liso.config(text=language[start + 11])
    larc.config(text=language[start + 12])
    lbstick.config(text=language[start + 13])
    ltex.config(text=language[start + 14])
    lmappyw.config(text=language[start + 15])
    lcmn.config(text=language[start + 16])
    ltrib.config(text=language[start + 17])
    lcwd.config(text=language[start + 18])
    dirbutton.config(text=language[start + 19])
    lenter.config(text=language[start + 20])
    LANGUAGES.set(language[start + 21])  # Change Language
    lhelp.config(text=language[start + 22])
    lquestion.config(text=language[start + 23])
    lconfig.config(text=language[start + 24])
    RUN.set(language[start + 25])  # Instant Run Apps (no UI)



def enter():  # "Run Instant App (Enter)" Button
    app = RUN.get()
    lang = LANGUAGES.get()
    cwd = cwd_entry.get()
    if cwd == '':
        cwd = os.getcwd()  # returns current working directory
    else:
        current_cwd.configure(text=cwd)
    cwd_entry.delete(0, 'end')  # empties the entry and change current working directory if it exists
    os.chdir(cwd)
    if lang != language[start + 21]:
        with open(f'C:\\Yosh\\lang\\{lang}.txt', 'rb') as txt1:
            new_lang = txt1.read()
        with open('C:\\Yosh\\#language.txt', 'wb') as txt2:
            txt2.write(new_lang)
        refresh()
        return
    if app == language[start + 25]:
        return
    Popen(('wscript.exe', f"C:\\Yosh\\{os.path.splitext(app.split('(')[-1])[0]}.vbs"))


def change_directory():  # executed when you press "Open FIle Explorer" button
    new_cwd = askdirectory(initialdir=os.getcwd())
    os.chdir(new_cwd)
    current_cwd.configure(text=new_cwd)


def pack():
    Popen(('wscript.exe', "C:\\Yosh\\pack.vbs"))


def thp():
    Popen(('wscript.exe', "C:\\Yosh\\thp.vbs"))


def brsar():  # run with the current executable (pythonw.exe full path)
    Popen(('wscript.exe', "C:\\Yosh\\brsar.vbs"))


def lh():  # run with command line window (else wszst opens too many windows and closes them instantly too frequently)
    Popen(('wscript.exe', "C:\\Yosh\\lh.vbs"))


def web():
    Popen(('wscript.exe', "C:\\Yosh\\web.vbs"))


def isox():
    Popen(('wscript.exe', "C:\\Yosh\\isox.vbs"))


def dump():
    Popen(('wscript.exe', "C:\\Yosh\\dump.vbs"))


def iso():
    Popen(('wscript.exe', "C:\\Yosh\\iso.vbs"))


def arc():
    Popen(('wscript.exe', "C:\\Yosh\\arc.vbs"))


def bstick():
    Popen(('wscript.exe', "C:\\Yosh\\bstick.vbs"))


def tex():
    Popen(('wscript.exe', "C:\\Yosh\\tex.vbs"))


def mappyw():
    Popen(('wscript.exe', "C:\\Yosh\\map.vbs"))


def trib():
    Popen(('wscript.exe', "C:\\Yosh\\trib.vbs"))


def msmhelp():
    Popen(('wscript.exe', "C:\\Yosh\\msmhelp.vbs"))


def cmn():
    os.system('taskkill /im "python.exe"')
    os.system('taskkill /im "pythonw.exe"')
    os.system('taskkill /im "arc.exe"')
    os.system('taskkill /im "brsar.exe"')
    os.system('taskkill /im "bstick.exe"')
    os.system('taskkill /im "c.exe"')
    os.system('taskkill /im "dec.exe"')
    os.system('taskkill /im "dump.exe"')
    os.system('taskkill /im "hexf.exe"')
    os.system('taskkill /im "int.exe"')
    os.system('taskkill /im "iso.exe"')
    os.system('taskkill /im "isox.exe"')
    os.system('taskkill /im "lh.exe"')
    os.system('taskkill /im "map.exe"')
    os.system('taskkill /im "msm.exe"')
    os.system('taskkill /im "msmhelp.exe"')
    os.system('taskkill /im "p.exe"')
    os.system('taskkill /im "pack.exe"')
    os.system('taskkill /im "png.exe"')
    os.system('taskkill /im "rEtUrN-tExT.exe"')
    os.system('taskkill /im "sizeC.exe"')
    os.system('taskkill /im "slot.exe"')
    os.system('taskkill /im "t.exe"')
    os.system('taskkill /im "tex.exe"')
    os.system('taskkill /im "tex3.exe"')
    os.system('taskkill /im "thp.exe"')
    os.system('taskkill /im "trib.exe"')
    os.system('taskkill /im "vaporwave.exe"')
    os.system('taskkill /im "web.exe"')
    os.system('taskkill /im "x.exe"')
    os.system('taskkill /im "yt.exe"')


ltitle = Label(a, text=language[start + 3], font=(None, 15), bg="#aecfee", height=3)
ltitle.grid(row=0, columnspan=3)
lp = Button(a, text=language[start + 4], command=pack, width=30)
lp.grid(row=3, column=0)
lt = Button(a, text=language[start + 5], command=thp, width=30)
lt.grid(row=3, column=1)
lbrsar = Button(a, text=language[start + 6], command=brsar, width=30)
lbrsar.grid(row=3, column=2)
l1 = Label(a, text="", bg="#aecfee", width=6)
l1.grid(row=4, column=1)
llh = Button(a, text=language[start + 7], command=lh, width=30)
llh.grid(row=5, column=0)
lweb = Button(a, text=language[start + 8], command=web, width=30)
lweb.grid(row=5, column=1)
lisox = Button(a, text=language[start + 9], command=isox, width=30)
lisox.grid(row=5, column=2)
l2 = Label(a, text="", bg="#aecfee")
l2.grid(row=6)
ldump = Button(a, text=language[start + 10], command=dump, width=30)
ldump.grid(row=7, column=0)
liso = Button(a, text=language[start + 11], state=DISABLED, command=iso, width=30)
liso.grid(row=7, column=1)
larc = Button(a, text=language[start + 12], command=arc, width=30)
larc.grid(row=7, column=2)
l3 = Label(a, text="", bg="#aecfee")
l3.grid(row=8, column=1)
lbstick = Button(a, text=language[start + 13], command=bstick, width=30)
lbstick.grid(row=9, column=0)
ltex = Button(a, text=language[start + 14], command=tex, width=30)
ltex.grid(row=9, column=1)
lmappyw = Button(a, text=language[start + 15], command=mappyw, width=30)
lmappyw.grid(row=9, column=2)
l4 = Label(a, text="", bg="#aecfee")
l4.grid(row=10)
lcmn = Button(a, text=language[start + 16], command=cmn, width=30)
lcmn.grid(row=11, column=0)
Run.config(width=30)
Run.grid(row=11, column=1)
ltrib = Button(a, text=language[start + 17], command=trib, width=30)
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

    lcmn.config(activebackground="#ff99ff", bg="#f0f0f0")

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

    lcmn.config(bg="#ffbbff", activebackground="#ffbbff")

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

    lcmn.config(bg="#ffaaff", activebackground="#ffaaff")

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

    lcmn.config(bg="#ff99ff", activebackground="#ff99ff")

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

    lcmn.config(bg="#ff90ff", activebackground="#ff90ff")

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

    lcmn.config(bg="#ff7fff", activebackground="#ff7fff")

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
lcwd = Label(a, text=language[start + 18], bg="#aecfee")
lcwd.grid(row=13, column=0)
current_cwd = Label(a, text=os.getcwd(), bg="#aecfee", width=70, anchor='w')
current_cwd.grid(row=13, column=1, columnspan=3)
cwd_entry = Entry(a, width=30)
cwd_entry.grid(row=14, column=1)
dirbutton = Button(a, text=language[start + 19], command=change_directory, activebackground='#96c7ff', width=30)
dirbutton.grid(row=14, column=0)
lenter = Button(a, text=language[start + 20], command=enter, activebackground="#a9ff91", width=29)
lenter.grid(row=14, column=2)
Languages.grid(row=15, column=1)
# Language OptionMenu is being at language[start + 21]
lhelp = Button(a, text=language[start + 22], activebackground="#a9ff91", command=msmhelp, width=25)
lhelp.grid(row=16, column=1)
lquestion = Button(a, text=language[start + 23], activebackground="#a9ff91", command=question_mark, width=25)
lquestion.grid(row=17, column=1)
lconfig = Button(a, text=language[start + 24], activebackground="#ff9999", command=change_config, width=25)
lconfig.grid(row=18, column=1)
msm1 = Canvas(a, width=220, height=148, bd=-2, bg="#aecfee")
msm_msm = PhotoImage(file="C:\\Yosh\\msm_stuff\\msm3.png")
msm1.create_image(110, 74, image=msm_msm)
msm1.grid(row=15, column=0, rowspan=6)
msm2 = Canvas(a, width=216, height=148, bd=-2, bg="#aecfee")
msm_png = PhotoImage(file="C:\\Yosh\\msm_stuff\\msm4.png")
msm2.create_image(100, 100, image=msm_png)
msm2.grid(row=15, column=2, rowspan=6)
a.mainloop()
