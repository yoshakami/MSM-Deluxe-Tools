import os
from tkinter import Tk, Label, Button, END, Entry
from tkinter.filedialog import askdirectory

d = b'\xff\xff\xff\xff'
a = Tk()
a.title('MSM Toolbox : every brsar patch')
a.minsize(660, 440)
a.config(bg='#bfaaff')
a.iconbitmap('C:\\Yosh\\every-brsar-patcher.ico')
q = 0


def J():
	o = q + 1
	if o == 2:
		for o in a.winfo_children():
			if o in [D, E, F, G, H, K]:
				continue
			o.destroy()
	z1 = z2 = z3 = z4 = z5 = z6 = z7 = z8 = z9 = i = 0

	def ctrlV(Name):
		b = g = 0
		with open(Name, "r+b") as h:
			while b < 0x400000:
				b = b + 1
				h.seek(b)
				c = h.read(6)
				if c == b'.brstm':
					e = b
					g = g + 1
					while c != d:
						b = b - 1
						h.seek(b)
						c = h.read(4)
					b = b - 8
					h.seek(b)
					h.write(d)
					b = e
					if b == 0x100000:
						p = Label(a, text="25% done", bg='#bfaaff', width=30)
						p.grid(row=5, column=1)
					if b == 0x200000:
						p = Label(a, text="50% done", bg='#bfaaff', width=30)
						p.grid(row=5, column=1)
					if b == 0x300000:
						p = Label(a, text="75% done", bg='#bfaaff', width=30)
						p.grid(row=5, column=1)
		return g

	def f1():
		num = ctrlV(z1)
		p = Label(a, text=f"patched {num} brstm", bg='#bfaaff', width=30)
		p.grid(row=5, column=1)
		c1.destroy()

	def f2():
		num = ctrlV(z2)
		p = Label(a, text=f"patched {num} brstm", bg='#bfaaff', width=30)
		p.grid(row=5, column=0)
		c2.destroy()

	def f3():
		num = ctrlV(z3)
		p = Label(a, text=f"patched {num} brstm", bg='#bfaaff', width=30)
		p.grid(row=5, column=2)
		c3.destroy()

	def f4():
		num = ctrlV(z4)
		p = Label(a, text=f"patched {num} brstm", bg='#bfaaff', width=30)
		p.grid(row=6, column=1)
		c4.destroy()

	def f5():
		num = ctrlV(z5)
		p = Label(a, text=f"patched {num} brstm", bg='#bfaaff', width=30)
		p.grid(row=6, column=0)
		c5.destroy()

	def f6():
		num = ctrlV(z6)
		p = Label(a, text=f"patched {num} brstm", bg='#bfaaff', width=30)
		p.grid(row=6, column=2)
		c6.destroy()

	def f7():
		num = ctrlV(z7)
		p = Label(a, text=f"patched {num} brstm", bg='#bfaaff', width=30)
		p.grid(row=7, column=1)
		c7.destroy()

	def f8():
		num = ctrlV(z8)
		p = Label(a, text=f"patched {num} brstm", bg='#bfaaff', width=30)
		p.grid(row=7, column=0)
		c8.destroy()

	def f9():
		num = ctrlV(z9)
		p = Label(a, text=f"patched {num} brstm", bg='#bfaaff', width=30)
		p.grid(row=7, column=2)
		c9.destroy()

	for u in os.listdir('./'):
		if not os.path.isfile(u):
			continue
		b = os.path.getsize(u)
		if b < 4:
			continue
		b = open(u, "rb")
		c = b.read(4)
		b.close()
		if c == b"RSAR":
			if i == 0:
				g = Label(a, text='every brsar patch', font=500, bg='#bfaaff', height=3)
				g.grid(row=2, columnspan=20)
			i = i + 1
			if i == 1:
				z1 = u
				c1 = Button(a, text=z1, command=f1, activebackground='#a9ff91', width=30)
				c1.grid(row=5, column=1)
			if i == 2:
				z2 = u
				c2 = Button(a, text=z2, command=f2, activebackground='#a9ff91', width=30)
				c2.grid(row=5, column=0)
			if i == 3:
				z3 = u
				c3 = Button(a, text=z3, command=f3, activebackground='#a9ff91', width=30)
				c3.grid(row=5, column=2)
			if i == 4:
				z4 = u
				c4 = Button(a, text=z4, command=f4, activebackground='#a9ff91', width=30)
				c4.grid(row=6, column=1)
			if i == 5:
				z5 = u
				c5 = Button(a, text=z5, command=f5, activebackground='#a9ff91', width=30)
				c5.grid(row=6, column=0)
			if i == 6:
				z6 = u
				c6 = Button(a, text=z6, command=f6, activebackground='#a9ff91', width=30)
				c6.grid(row=6, column=2)
			if i == 7:
				z7 = u
				c7 = Button(a, text=z7, command=f7, activebackground='#a9ff91', width=30)
				c7.grid(row=7, column=1)
			if i == 8:
				z8 = u
				c8 = Button(a, text=z8, command=f8, activebackground='#a9ff91', width=30)
				c8.grid(row=7, column=0)
			if i == 9:
				z9 = u
				c9 = Button(a, text=z9, command=f9, activebackground='#a9ff91', width=30)
				c9.grid(row=7, column=2)


def A():
	B = D.get()
	if B == '':
		B = os.getcwd()
	else:
		F.configure(text=B)
	D.delete(0, END)
	os.chdir(B)
	J()


def L():
	M = askdirectory(initialdir=B)
	os.chdir(M)
	F.configure(text=M)
	J()


def Q():
	a.quit()


B = os.getcwd()
E = Label(a, text='Current working directory is', bg='#bfaaff', width=30)
E.grid(row=0, column=0)
F = Label(a, text=B, bg='#bfaaff', width=30)
F.grid(row=1, column=0)
D = Entry(a, width=30)
D.grid(row=1, column=1)
G = Button(a, text='Enter', command=A, activebackground='#ff9999', width=30)
G.grid(row=1, column=2)
H = Button(a, text='Exit', command=Q, activebackground='#d9ff8c', width=15)
H.grid(row=0, column=2)
K = Button(a, text='Open file Explorer', command=L, activebackground='#96c7ff', width=15)
K.grid(row=0, column=1)
J()
q = 1
a.mainloop()
