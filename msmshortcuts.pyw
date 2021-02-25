from tkinter import Canvas, Label, PhotoImage, Tk, Button

a = Tk()
a.title("Mario Sports Mix Modding App Shortcuts")
a.attributes('-fullscreen', True)
a.config(bg="#aecfee")
a.iconbitmap('C:\\Yosh\\msmshortcuts.ico')


width = a.winfo_screenwidth()
height = a.winfo_screenheight()
window = Canvas(a, width=width, height=height, bd=-2)  # image will be displayed on fullscreen
picture = PhotoImage(file="C:\\Yosh\\MSM Shortcuts.png")
window.create_image(width / 2, height / 2, image=picture)
window.grid(row=0, column=0, rowspan=100, columnspan=100)

exit_app = Button(a, text='Exit', command=a.quit, bg="#7fff7f", font=2, activebackground='#7fff7f', width=30, height=2)
exit_app.grid(row=88, column=87)

dim = Label(a, text=f'Your screen dimensions are\n{width}x{height} pixels', font=2, bg='#fffbde', width=30)
dim.grid(row=82, column=87, rowspan=6)
a.mainloop()
