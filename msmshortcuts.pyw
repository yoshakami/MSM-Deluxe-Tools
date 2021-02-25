from tkinter import Canvas, Label, PhotoImage, Tk, Button
from PIL import Image

a = Tk()
a.title("Mario Sports Mix Modding App Shortcuts")
a.attributes('-fullscreen', True)
a.config(bg="#aecfee")
a.iconbitmap('C:\\Yosh\\msmshortcuts.ico')


width = a.winfo_screenwidth()
height = a.winfo_screenheight()

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
window.grid(row=0, column=0, rowspan=100, columnspan=100)

exit_app = Button(a, text='Exit', command=a.quit, bg="#7fff7f", font=2, activebackground='#7fff7f', width=30, height=2)
exit_app.grid(row=88, column=87)

dim = Label(a, text=f'Your screen dimensions are\n{width}x{height} pixels', font=2, bg='#fffbde', width=30)
dim.grid(row=82, column=87, rowspan=6)
a.mainloop()
