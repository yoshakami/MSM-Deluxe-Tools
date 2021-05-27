from tkinter import Canvas, Label, PhotoImage, Tk, Button, font
from PIL import Image
from ctypes import windll, byref, create_unicode_buffer, create_string_buffer

a = Tk()
a.title("Mario Sports Mix Modding App Shortcuts")
a.attributes('-fullscreen', True)
a.config(bg="#aecfee")
a.iconbitmap('C:\\Yosh\\msmshortcuts.ico')

FR_PRIVATE = 0x10
FR_NOT_ENUM = 0x20


def loadfont(fontpath, private=True, enumerable=False):
    # Makes fonts located in file `fontpath` available to the font system.
    #
    # `private`     if True, other processes cannot see this font, and this
    #              font will be unloaded when the process dies
    # `enumerable`  if True, this font will appear when enumerating fonts
    # See https://msdn.microsoft.com/en-us/library/dd183327(VS.85).aspx
    #
    # This function was taken from
    # https://github.com/ifwe/digsby/blob/f5fe00244744aa131e07f09348d10563f3d8fa99/digsby/src/gui/native/win/winfonts.py#L15
    # This function is written for Python 2.x. For 3.x, you
    # have to convert the isinstance checks to bytes and str
    if isinstance(fontpath, bytes):
        pathbuf = create_string_buffer(fontpath)
        AddFontResourceEx = windll.gdi32.AddFontResourceExA
    elif isinstance(fontpath, str):
        pathbuf = create_unicode_buffer(fontpath)
        AddFontResourceEx = windll.gdi32.AddFontResourceExW
    else:
        raise TypeError('fontpath must be of type str or bytes')

    flags = (FR_PRIVATE if private else 0) | (FR_NOT_ENUM if not enumerable else 0)
    numFontsAdded = AddFontResourceEx(byref(pathbuf), flags, 0)
    return bool(numFontsAdded)


loadfont('C:\\Yosh\\m.otf')
width = a.winfo_screenwidth()
height = a.winfo_screenheight()
#  print(font.families())
m = font.Font(family='MARIO Font v3 Solid', size=15)  # , weight='bold')
with open("C:\\Yosh\\MSM Shortcuts.png", 'rb') as minipic:
    minipic.seek(16)
    byte = minipic.read(4)
    pic_width = (byte[0] * 16777216) + (byte[1] * 65536) + (byte[2] * 256) + byte[3] - 64  # 4 bytes integer
    byte = minipic.read(4)
    pic_height = (byte[0] * 16777216) + (byte[1] * 65536) + (byte[2] * 256) + byte[3] - 64  # 4 bytes integer

if (pic_width != width) and (pic_height != height):
    pic = Image.open('C:\\Yosh\\MSM Shortcuts.png')
    new_pic = pic.resize((width, height))
    pic.close()
    new_pic.save('C:\\Yosh\\MSM Shortcuts.png')

window = Canvas(a, width=width, height=height, bd=-2)  # image will be displayed on fullscreen
picture = PhotoImage(file="C:\\Yosh\\MSM Shortcuts.png")
window.create_image(width / 2, height / 2, image=picture)
window.place(x=0, y=0)

exit_app = Button(a, text='Exit', command=a.quit, bg="#7fff7f", font=2, activebackground='#7fff7f', width=25, height=2)
exit_app.place(x=7 * width / 10, y=3 * height / 4)

dim = Label(a, text=f'Your screen dimensions\n are {width}x{height} pixels', font=m, bg='#fffbde', fg='#ff2f2f')
dim.place(x=7 * width / 10, y=3 * height / 4 + 60)
a.mainloop()
