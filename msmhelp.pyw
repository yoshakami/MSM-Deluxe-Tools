from tkinter import Tk, Canvas, PhotoImage, Button, Label
from functools import partial
from PIL import Image

a = Tk()
a.title("Mario Sports Mix Modding App Help")
a.attributes('-fullscreen', True)
a.config(bg="#ff9696")
a.iconbitmap('C:\\Yosh\\msmhelp.ico')
title = Label(a, text="Mario Sports Mix Modding Help Menu", font=300, bg="#ff9696", height=3)
title.grid(row=0, columnspan=30)
txt = Label(a, text="Click on the pictures to view on fullscreen", font=300, bg="#ff9696", height=3)
txt.grid(row=3, columnspan=30)
w = a.winfo_screenwidth()
h = a.winfo_screenheight()

exitbu = Button(a, text='Exit', command=a.quit, bg="#7fff7f", font=2, activebackground='#7fff7f', width=30, height=2)
exitbu.grid(row=2, column=6, rowspan=2)


def menu(garbage):  # goes back to the menu with 16 little pictures
    for z in a.winfo_children():
        if z in static:
            continue
        z.destroy()


def display(picture, garbage_sent_by_bind):
    c = Canvas(a, width=w, height=h, bd=-2, bg="#ff9696")
    c.bind("<Button-1>", menu)
    c.create_image(w / 2, h / 2, image=image_list[picture])
    c.grid(row=0, column=0, rowspan=100, columnspan=100)


name = ["h", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "ha", "hb", "hc", "hd", "he", "hf", "hm", "m", "m2", "m3", "m4", "m5", "m6", "m7", "how-to-run-msm", "m9", "ma", "mb", "mc", "md", "me", "mf", "mm"]
miniatures = name[:16]  # from h to hm
large = name[16:]  # from m to end


with open("C:\\Yosh\\h.png", 'rb') as minipic:
    minipic.seek(16)
    byte = minipic.read(4)
    pic_width = (byte[0] * 16777216) + (byte[1] * 65536) + (byte[2] * 256) + byte[3] - 64  # 4 bytes integer
    byte = minipic.read(4)
    pic_height = (byte[0] * 16777216) + (byte[1] * 65536) + (byte[2] * 256) + byte[3] - 64  # 4 bytes integer

if (pic_width != w // 5) and (pic_height != h // 5):
    for n in range(len(miniatures)):
        picc = Image.open('C:\\Yosh\\' + miniatures[n] + '.png')
        new_pic = picc.resize((w // 5, h // 5))
        picc.close()
        new_pic.save('C:\\Yosh\\' + miniatures[n] + '.png')

with open("C:\\Yosh\\m.png", 'rb') as minipic:
    minipic.seek(16)
    byte = minipic.read(4)
    pic_width = (byte[0] * 16777216) + (byte[1] * 65536) + (byte[2] * 256) + byte[3] - 64  # 4 bytes integer
    byte = minipic.read(4)
    pic_height = (byte[0] * 16777216) + (byte[1] * 65536) + (byte[2] * 256) + byte[3] - 64  # 4 bytes integer

if (pic_width != w) and (pic_height != h):
    for p in range(len(miniatures)):
        picc = Image.open('C:\\Yosh\\' + miniatures[p] + '.png')
        new_pic = picc.resize((w, h))
        picc.close()
        new_pic.save('C:\\Yosh\\' + miniatures[p] + '.png')

image_list = []
for j in range(0, 32):
    pic = PhotoImage(file=f"C:\\Yosh\\{name[j]}.png")
    image_list.append(pic)
col = 0
static = [title, txt, exitbu]
ListeNulle = [3, 7, 11]
rao = [4, 4, 4, 4, 10, 10, 10, 10, 15, 15, 15, 15, 20, 20, 20, 20]

for i in range(0, 16):  # displays the 16 little pictures + bind left click to the full-screen ones
    f = Canvas(a, width=w / 4, height=h / 5, bd=-2, bg="#ff9696")
    func = partial(display, i + 16)
    f.bind("<Button-1>", func)
    f.create_image(w / 8, h / 10, image=image_list[i])
    f.grid(row=rao[i], column=col)
    if i in ListeNulle:
        col = -2  # line below will set it to 0
    col += 2
    static.append(f)
a.mainloop()
