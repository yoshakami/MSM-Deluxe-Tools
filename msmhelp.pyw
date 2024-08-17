from tkinter import Tk, Canvas, PhotoImage, Button, Label, font
from functools import partial
from textwrap import wrap
from math import e, log
from PIL import Image
import random
import os

install_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(install_dir, '#language.txt'), 'r', encoding="utf-8") as txt:
    language = txt.read()
    language = [''] + language.splitlines()

start = int(language[1].split(":")[31])
msm = int(language[1].split(":")[1])
hashtag = int(language[1].split(":")[3])
a = Tk()
a.title(language[start])
a.attributes('-fullscreen', True)
a.config(bg="#ff9696")
ico = os.path.join('msm_stuff', 'msmhelp.ico')
a.iconbitmap(os.path.join(install_dir, ico))
msm_stuff = os.path.join(install_dir, 'msm_stuff')
w = a.winfo_screenwidth()
h = a.winfo_screenheight()
font_name = 'IO Font v3 Solid'
s = font.Font(family=f'MAR{font_name}', size=15)
m = font.Font(family=f'MAR{font_name}', size=int(25 / 1536 * w))  # , weight='bold')
big = font.Font(family=f'MAR{font_name}', size=40)
man = font.Font(family=f'MAR{font_name}', size=50)

txt = Label(a, text=language[start + 2], font=300, bg="#ff9696")
txt.place(x=33 * w / 84, y=h / 20)
title = Label(a, text=language[start + 1], font=300, bg="#ff9696")
title.place(x=17 * w / 42, y=h / 50)
bye = Button(a, text=language[msm + 39], command=a.quit, bg="#9fff7f", font=2, activebackground='#8fff7f', width=24, height=2)
bye.place(x=63 * w / 80, y=h / 10)
dim = Label(a, text=language[hashtag + 11].replace('§', '\n').replace('#', str(w)).replace('%', str(h)), font=s, bg='#ff9696', fg='#2f2fff')
dim.place(x=w / 10, y=h / 10)
static = [title, txt, bye, dim]
# a.wm_attributes('-transparentcolor', a['bg'])

# print(f"screen dimensions : {w}x{h}")
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
        # text_list.append(language[start + 20 + k + (picture-16) * 2])
        splitted_txt = language[start + 20 + k + (picture-16) * 2].split('¤')
        paragraph = ''
        g = 1  # starting character of the text in #language.txt
        if splitted_txt[0][:g] == '*':  # * means the line won't be wrapped
            g = 2
        for line in splitted_txt:
            b = 1
            if line[1].isdigit():
                b = 2
            if g == 2:
                list_txt = ['¤' + line]
            else:  # tries to adapt the font size to the screen
                x = int(line[:b])
                list_txt = wrap('¤' + line, int(1.5/(0.00226 * x) + 3 * log(e, 70/(6 * x)) + 6))
                # list_txt = wrap('¤' + line, int(1 / (int(line[:b]) * w / 1920) * 990))
                # print(int(1 / (int(line[:b]) * w / 1920) * 950))
            for text1 in list_txt:
                paragraph += text1.replace('§', '\n').replace('\\n', '\n').replace('\\t', '\t')
                if text1 != list_txt[-1]:
                    paragraph += '\n'
        # print(paragraph)
        text_list.append(paragraph[g:])

    if picture != 27:
        # rendering the title text
        title_text = language[start + picture-13]
        if title_text[1].isnumeric():
            c.create_text((2 * w / 7, h / 8), text=title_text[3:], font=(f'MAR{font_name}', int(int(title_text[:2]) / 1920 * w)),
                          fill=title[picture-16], anchor='w')
        else:
            c.create_text((0, h / 8), text=title_text[2:], font=(f'MAR{font_name}', int(int(title_text[:1]) / 1920 * w)),
                          fill=title[picture-16], anchor='w')

        # rendering the left/right text with special markdown: type \n with 4 spaces to start a new line below,
        # type ¤ then the font size then a number between 0 and 36 followed by a space to change the text color
        # and ¤ for the colour id (from the list named minicolor). for example ¤0 for red or ¤36 for white text color
        left_text = text_list[0].split('¤')
        n_count = 0
        for k in range(len(left_text)):
            d = 1
            while left_text[k][:d].isnumeric():
                if left_text[k][:d] == left_text[k][:d+1]:  # prevents infinite loop if there is nothing behind
                    break
                d += 1
            g = d + 1
            while left_text[k][d:g].isnumeric():
                if left_text[k][d:g] == left_text[k][d:g+1]:  # prevents infinite loop if there is nothing behind
                    break
                g += 1
            beginning = g
            c.create_text((w / 14, h / 4), text='\n' * n_count + left_text[k][beginning:], font=(f'MAR{font_name}', int(int(left_text[k][:d-1]) / 1536 * w)), fill=minicolor[int(left_text[k][d:g])], anchor='nw')  # left text
            n_count += left_text[k].count('\n')

        right_text = text_list[1].split('¤')
        n_count = 0
        for x in range(len(right_text)):
            d = 1
            while right_text[x][:d].isnumeric():
                if right_text[x][:d] == right_text[x][:d+1]:  # prevents infinite loop if there is nothing behind
                    break
                d += 1
            g = d + 1
            while right_text[x][d:g].isnumeric():
                if right_text[x][d:g] == right_text[x][d:g+1]:  # prevents infinite loop if there is nothing behind
                    break
                g += 1
            beginning = g
            c.create_text((w / 2, 2 * h / 7), text='\n' * n_count + right_text[x][beginning:], font=(f'MAR{font_name}', int(int(right_text[x][:d-1]) / 1536 * w)), fill=minicolor[int(right_text[x][d:g])], anchor='nw')  # right text
            n_count += right_text[x].count('\n')


name = ["h", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "ha", "hb", "hc", "hd", "he", "hf", "hm", "m", "m2", "m3",
        "m4", "m5", "m6", "m7", "m8", "m9", "ma", "mb", "how-to-run-msm", "md", "me", "mf", "mm"]
miniatures = name[:16]  # from h to hm
large = name[16:]  # from m to end

with open(os.path.join(msm_stuff, "h.png"), 'rb') as minipic:
    minipic.seek(16)
    byte = minipic.read(4)
    # pic_width = (byte[0] * 16777216) + (byte[1] * 65536) + (byte[2] * 256) + byte[3]  # 4 bytes integer
    pic_width = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3]  # 4 bytes integer
    byte = minipic.read(4)
    pic_height = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3]  # 4 bytes integer

if (pic_width != w // 5) and (pic_height != h // 5):
    for n in range(len(miniatures)):
        picc = Image.open(os.path.join(msm_stuff, miniatures[n] + '.png'))
        new_pic = picc.resize((w // 5, h // 5))
        picc.close()
        new_pic.save(os.path.join(msm_stuff, + miniatures[n] + '.png'))

with open(os.path.join(msm_stuff, "m.png"), 'rb') as minipic:
    minipic.seek(16)
    byte = minipic.read(4)
    pic_width = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3]  # 4 bytes integer
    byte = minipic.read(4)
    pic_height = (byte[0] << 24) + (byte[1] << 16) + (byte[2] << 8) + byte[3]  # 4 bytes integer

if (pic_width != w) and (pic_height != h):
    for p in range(len(large)):
        picc = Image.open(os.path.join(msm_stuff, large[p] + '.png'))
        new_pic = picc.resize((w, h))
        picc.close()
        new_pic.save(os.path.join(msm_stuff, large[p] + '.png'))

image_list = []
for j in range(0, 32):
    pic = PhotoImage(file=os.path.join(msm_stuff, f'{name[j]}.png'))
    image_list.append(pic)
ListeNulle = [3, 7, 11]
eks = [0, w / 4, 2 * w / 4, 3 * w / 4]
whi = [h / 5, 2 * h / 5, 3 * h / 5, 4 * h / 5]
minicolor = ['#ff0000', '#ff7f7f', '#ff5f00', '#ff9f00', '#ffcf00',  # id 0 to 4
             '#ffff00', '#ffff7f', '#cfff00', '#9fff00', '#5fff00',  # id 5 to 9
             '#00ff00', '#7fff7f', '#00ff5f', '#00ff9f', '#00ffcf',  # id 10 to 14
             '#00ffff', '#7fffff', '#00cfff', '#009fff', '#005fff',  # id 15 to 19
             '#0000ff', '#7f7fff', '#5500a5', '#5f00ff', '#9f00ff', '#cf00ff',  # id 20 to 25
             '#ff00ff', '#ff7fff', '#ff00cf', '#ff009f', '#ff005f', '#b70f00',  # id 26 to 31
             '#000000', '#3f3f3f', '#7f7f7f', '#bfbfbf', '#ffffff']  # if 32 to 36 - white to black

#             5'#ff0000', '#00ff00', '#0000ff', '#00ffff', '#ff00ff', '#ffff00',  # 5primary and printing colours
#             11'#ff7f7f', '#7fff7f', '#7f7fff', '#7fffff', '#ff7fff', '#ffff7f',  # 11primary and printing colours lighter
#             17'#ff5f00', '#ff005f', '#5fff00', '#5f00ff', '#005fff', '#00ff5f',   # 17all combos with ff, 5f, and 00
#             23'#ff9f00', '#ff009f', '#9fff00', '#9f00ff', '#009fff', '#00ff9f',  # 23all combos with ff, 9f, and 00
#             29'#ffcf00', '#ff00cf', '#cfff00', '#cf00ff', '#00cfff', '#00ffcf',  # 29all combos with ff, cf, and 00
#             35'#5500a5', '#b70f00' # 35plum then maroon

# print(f'there are {len(minicolor)} colours available')
# green_cyan = minicolor[0] '#03ff81',
# lighter_blue = minicolor[1] '#0061ff',
# light_blue = minicolor[4] '#006eff',
blue = minicolor[20]
purple = minicolor[24]
light_blue = minicolor[17]
violet = minicolor[25]

fushia = minicolor[29]
pink = minicolor[30]
pink_orange = minicolor[1]
orange = minicolor[3]

cyan = minicolor[16]
green_cyan = minicolor[13]
light_green = minicolor[8]
lighter_blue = minicolor[15]

# light_gray gray dark_gray black red green yellow light_red orchid
# plum = minicolor[22]
# maroon = minicolor[31]
# chartreuse = minicolor[7]
# dodger_blue = minicolor[18]

title = [blue, purple, light_blue, violet,
         fushia, pink, pink_orange, orange,
         cyan, green_cyan, light_green, "",
         lighter_blue, blue, orange, violet]


for i in range(0, 16):  # displays the 16 little pictures + bind left click to the full-screen ones
    list_text = wrap(language[start + 3 + i].lstrip('0123456789 '), 12)  # doesn't create a title larger than 12 characters else it's off-picture
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
    info = f.create_text((w / 8, h / 9), text=text, font=m, fill=minicolor[(i+random.choice((11, 18, 20, 23))) % 32], justify="center")  # 11 18 20 23
    static.append(f)
    static.append(info)
a.mainloop()
