from tkinter import Tk, Canvas, PhotoImage, Button, Label, font
from textwrap import wrap
from functools import partial
from PIL import Image

with open('C:\\Yosh\\#language.txt', 'r', encoding="utf-8") as txt:
    language = txt.read()
    language = [''] + language.splitlines()

start = int(language[1].split(":")[31])
msm = int(language[1].split(":")[1])
a = Tk()
a.title(language[start])
a.attributes('-fullscreen', True)
a.config(bg="#ff9696")
a.iconbitmap('C:\\Yosh\\msm_stuff\\msmhelp.ico')
w = a.winfo_screenwidth()
h = a.winfo_screenheight()

s = font.Font(family='MARIO Font v3 Solid', size=15)
m = font.Font(family='MARIO Font v3 Solid', size=25)  # , weight='bold')
big = font.Font(family='MARIO Font v3 Solid', size=40)
man = font.Font(family='MARIO Font v3 Solid', size=50)

txt = Label(a, text=language[start + 2], font=300, bg="#ff9696")
txt.place(x=33 * w / 84, y=h / 20)
title = Label(a, text=language[start + 1], font=300, bg="#ff9696")
title.place(x=17 * w / 42, y=h / 50)
bye = Button(a, text=language[msm + 39], command=a.quit, bg="#9fff7f", font=2, activebackground='#8fff7f', width=24, height=2)
bye.place(x=63 * w / 80, y=h / 10)
dim = Label(a, text=f'Your screen dimensions\n are {w}x{h} pixels', font=s, bg='#ff9696', fg='#2f2fff')
dim.place(x=w / 10, y=h / 10)
static = [title, txt, bye, dim]
# a.wm_attributes('-transparentcolor', a['bg'])


# print(font.families())

def menu(garbage):  # goes back to the menu with 16 little pictures
    for z in a.winfo_children():
        if z in static:
            continue
        z.destroy()


def display(picture, garbage_sent_by_bind):  # displays the big png
    c = Canvas(a, width=w, height=h, bd=-2, bg="#ff9696")
    c.bind("<Button-1>", menu)
    c.create_image(w / 2, h / 2, image=image_list[picture])
    c.place(x=0, y=0)

    # centered_title = language[start + (picture-16)]
    # centered_title = (50 - 2 * len(string)) * ' ' + language[217 + (picture-16) * 3] + (12 - 2 * len(string)) * ' '
    text_list = []
    for k in range(2):
        splitted_txt = wrap(language[start + 20 + k + (picture-16) * 3], 25)
        paragraph = ''
        for line in splitted_txt:
            if paragraph == splitted_txt[-1]:  # don't add a new line after the last line else it'll screw up the display
                paragraph += line.replace('\\n    ', '\n')
            else:
                paragraph += line.replace('\\n    ', '\n') + '\n'
        text_list.append(paragraph)

    if picture != 27:
        # rendering the title text
        if picture in (18, 20, 22, 24, 30):
            c.create_text((3 * w / 5, h / 8), text=language[start + picture-13], font=big, fill=title[picture-16])  # title
        elif picture in (19, 31):
            c.create_text((w / 2, h / 8), text=language[start + picture-13], font=man, fill=title[picture-16])  # title
        else:
            c.create_text((w / 3, h / 8), text=language[start + picture-13], font=man, fill=title[picture-16], anchor='w')  # title

        # rendering the left text with special markdown: type \n with 4 spaces to start a new line below,
        # type ¤ then a number between 0 and 15 followed by a space to change the text color
        # and ¤ for the colour id (from the list named minicolor). for example ¤9 for pink or ¤15 for maroon text color
        left_text = text_list[0].split('¤')
        n_count = 0
        for k in range(len(left_text)):
            if left_text[k][1].isdigit():
                c.create_text((w / 14, h / 4), text='\n' * n_count + left_text[k][3:], font=m, fill=minicolor[int(left_text[k][:2])], anchor='nw')  # left text
            else:
                c.create_text((w / 14, h / 4), text='\n' * n_count + left_text[k][2:], font=m, fill=minicolor[int(left_text[k][0])], anchor='nw')  # left text
            n_count += left_text[k].count('\n')

        right_text = text_list[1].split('¤')
        n_count = 0
        for x in range(len(right_text)):
            if left_text[x][1].isdigit():
                c.create_text((w / 14, h / 4), text='\n' * n_count + left_text[x][3:], font=m, fill=minicolor[int(left_text[x][:2])], anchor='nw')  # right text
            else:
                c.create_text((w / 14, h / 4), text='\n' * n_count + left_text[x][2:], font=m, fill=minicolor[int(left_text[x][0])], anchor='nw')  # right text
            n_count += left_text[x].count('\n')
        c.create_text((w / 14, h / 4), text=text_list[0], font=m, fill=minicolor[picture-16], anchor='nw')  # left text
        c.create_text((w / 2, 2 * h / 7), text=text_list[1], font=m, fill=minicolor[picture-16], anchor='nw')  # right text


name = ["h", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "ha", "hb", "hc", "hd", "he", "hf", "hm", "m", "m2", "m3",
        "m4", "m5", "m6", "m7", "m8", "m9", "ma", "mb", "how-to-run-msm", "md", "me", "mf", "mm"]
miniatures = name[:16]  # from h to hm
large = name[16:]  # from m to end

with open("C:\\Yosh\\msm_stuff\\h.png", 'rb') as minipic:
    minipic.seek(16)
    byte = minipic.read(4)
    # pic_width = (byte[0] * 16777216) + (byte[1] * 65536) + (byte[2] * 256) + byte[3]  # 4 bytes integer
    pic_width = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3]  # 4 bytes integer
    byte = minipic.read(4)
    pic_height = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3]  # 4 bytes integer

if (pic_width != w // 5) and (pic_height != h // 5):
    for n in range(len(miniatures)):
        picc = Image.open('C:\\Yosh\\msm_stuff\\' + miniatures[n] + '.png')
        new_pic = picc.resize((w // 5, h // 5))
        picc.close()
        new_pic.save('C:\\Yosh\\msm_stuff\\' + miniatures[n] + '.png')

with open("C:\\Yosh\\msm_stuff\\m.png", 'rb') as minipic:
    minipic.seek(16)
    byte = minipic.read(4)
    pic_width = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3]  # 4 bytes integer
    byte = minipic.read(4)
    pic_height = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3]  # 4 bytes integer

if (pic_width != w) and (pic_height != h):
    for p in range(16, len(miniatures)):
        picc = Image.open('C:\\Yosh\\msm_stuff\\' + miniatures[p] + '.png')
        new_pic = picc.resize((w, h))
        picc.close()
        new_pic.save('C:\\Yosh\\msm_stuff\\' + miniatures[p] + '.png')

image_list = []
for j in range(0, 32):
    pic = PhotoImage(file=f"C:\\Yosh\\msm_stuff\\{name[j]}.png")
    image_list.append(pic)
ListeNulle = [3, 7, 11]
eks = [0, w / 4, 2 * w / 4, 3 * w / 4]
whi = [h / 5, 2 * h / 5, 3 * h / 5, 4 * h / 5]
minicolor = ['#03ff81', '#0061ff', '#0000ff', '#7f00ff',
             '#006eff', '#952bff', '#ff00a1', '#ff5d00',
             '#5500a5', '#ff77df', '#ff8282', '#ffbf00',
             '#35ff7f', '#99ff00', '#c700ff', '#b70f00',
             '#000000', '#7f7f7f', '#ffffff']
green_cyan = minicolor[0]
lighter_blue = minicolor[1]
blue = minicolor[2]
purple = minicolor[3]
light_blue = minicolor[4]
violet = minicolor[5]
fushia = minicolor[6]
red = minicolor[7]
plum = minicolor[8]
pink = minicolor[9]
pink_orange = minicolor[10]
orange = minicolor[11]
cyan = minicolor[12]
light_green = minicolor[13]
orchid = minicolor[14]
maroon = minicolor[15]
black = minicolor[16]
gray = minicolor[17]
white = minicolor[18]

title = [blue, purple, light_blue, violet,
         fushia, pink, pink_orange, orange,
         cyan, green_cyan, light_green, "",
         lighter_blue, blue, orange, violet]



for i in range(0, 16):  # displays the 16 little pictures + bind left click to the full-screen ones
    list_text = wrap(language[start + 3 + i], 12)  # doesn't create a title larger than 12 characters else it's off-picture
    text = ''
    for string in list_text:
        if string == list_text[-1]:
            text += string  # (13 - 2 * len(string)) * ' ' + string + (12 - 2 * len(string)) * ' '  # old (and worse) method for justify="center"
        else:
            text += string + '\n'  # (13 - 2 * len(string)) * ' ' + string + (12 - 2 * len(string)) * ' ' + '\n'

    f = Canvas(a, width=w / 4, height=h / 5, bd=-2, bg="#ff9696")
    func = partial(display, i + 16)
    f.bind("<Button-1>", func)
    f.create_image(w / 8, h / 10, image=image_list[i])
    f.place(x=eks[i % 4], y=whi[i // 4])  # + '\n' + language[201 + i][10:20] + '\n' + language[201 + i][20:]
    info = f.create_text((w / 8, h / 9), text=text, font=m, fill=minicolor[i], justify="center")
    static.append(f)
    static.append(info)
a.mainloop()
