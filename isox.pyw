import os, shutil
from tkinter import Tk, Label, Button, END, Entry
from tkinter.filedialog import askdirectory

a = Tk()
a.title('Mario Sports Mix Modding iso/wbfs extract and compress')
a.minsize(660, 440)
a.config(bg='#aaffaa')
a.iconbitmap('C:\\Yosh\\isox.ico')
q = 0


def J():
    o = q + 1
    if o == 2:
        for o in a.winfo_children():
            if o == D or o == E or o == F or o == G or o == H or o == K:
                continue
            o.destroy()
    z1 = z2 = z3 = z4 = z5 = z6 = z7 = z8 = z9 = w1 = w2 = w3 = w4 = w5 = w6 = w7 = w8 = w9 = i = f = na = nb = nc = nd = ne = nf = ng = nh = ni = nj = nk = nl = nm = nn = no = m = 0

    def ctrlV(name):
        os.system(f'wit extract "{name}" Mario-Sports-Mix')
        os.system('del Mario-Sports-Mix\\UPDATE /q /f')
        shutil.rmtree('Mario-Sports-Mix\\UPDATE')
        os.system('xcopy Mario-Sports-Mix\\DATA Mario-Sports-Mix /i /y /q /s')
        os.system('del Mario-Sports-Mix\\DATA /q /f')
        shutil.rmtree('Mario-Sports-Mix\\DATA')

    def f1():
        ctrlV(z1)
        c1.destroy()

    def f2():
        ctrlV(z2)
        c2.destroy()

    def f3():
        ctrlV(z3)
        c3.destroy()

    def f4():
        ctrlV(z4)
        c4.destroy()

    def f5():
        ctrlV(z5)
        c5.destroy()

    def f6():
        ctrlV(z6)
        c6.destroy()

    def f7():
        ctrlV(z7)
        c7.destroy()

    def f8():
        ctrlV(z8)
        c8.destroy()

    def f9():
        ctrlV(z9)
        c9.destroy()

    def ctrlC(Name):
        os.system(f'wit copy "{Name}" Mario-Sports-Mix.iso')
        os.system('del Mario-Sports-Mix\\UPDATE /q /f')
        shutil.rmtree('Mario-Sports-Mix\\UPDATE')
        os.system('xcopy Mario-Sports-Mix\\DATA Mario-Sports-Mix /i /y /q /s')
        os.system('del Mario-Sports-Mix\\DATA /q /f')
        shutil.rmtree('Mario-Sports-Mix\\DATA')

    def g1():
        ctrlC(w1)
        b1.destroy()

    def g2():
        ctrlC(w2)
        b2.destroy()

    def g3():
        ctrlC(w3)
        b3.destroy()

    def g4():
        ctrlC(w4)
        b4.destroy()

    def g5():
        ctrlC(w5)
        b5.destroy()

    def g6():
        ctrlC(w6)
        b6.destroy()

    def g7():
        ctrlC(w7)
        b7.destroy()

    def g8():
        ctrlC(w8)
        b8.destroy()

    def g9():
        ctrlC(w9)
        b9.destroy()

    def i1():
        os.system(f'wit copy "{na}" "{na}.iso" -o')
        d1.destroy()

    def i2():
        os.system(f'wit copy "{nb}" "{nb}.iso" -o')
        d2.destroy()

    def i3():
        os.system(f'wit copy "{nc}" "{nc}.iso" -o')
        d3.destroy()

    def i4():
        os.system(f'wit copy "{nd}" "{nd}.iso" -o')
        d4.destroy()

    def i5():
        os.system(f'wit copy "{ne}" "{ne}.iso" -o')
        d5.destroy()

    def i6():
        os.system(f'wit copy "{nf}" "{nf}.iso" -o')
        d6.destroy()

    def i7():
        os.system(f'wit copy "{ng}" "{ng}.iso" -o')
        d7.destroy()

    def i8():
        os.system(f'wit copy "{nh}" "{nh}.iso" -o')
        d8.destroy()

    def i9():
        os.system(f'wit copy "{ni}" "{ni}.iso" -o')
        d9.destroy()

    def i10():
        os.system(f'wit copy "{nj}" "{nj}.iso" -o')
        d10.destroy()

    def i11():
        os.system(f'wit copy "{nk}" "{nk}.iso" -o')
        d11.destroy()

    def i12():
        os.system(f'wit copy "{nl}" "{nl}.iso" -o')
        d12.destroy()

    def i13():
        os.system(f'wit copy "{nm}" "{nm}.iso" -o')
        d13.destroy()

    def i14():
        os.system(f'wit copy "{nn}" "{nn}.iso" -o')
        d14.destroy()

    def i15():
        os.system(f'wit copy "{no}" "{no}.iso" -o')
        d15.destroy()

    def h1():
        os.system(f'wit copy "{na}" "{na}.wbfs" -o')
        e1.destroy()

    def h2():
        os.system(f'wit copy "{nb}" "{nb}.wbfs" -o')
        e2.destroy()

    def h3():
        os.system(f'wit copy "{nc}" "{nc}.wbfs" -o')
        e3.destroy()

    def h4():
        os.system(f'wit copy "{nd}" "{nd}.wbfs" -o')
        e4.destroy()

    def h5():
        os.system(f'wit copy "{ne}" "{ne}.wbfs" -o')
        e5.destroy()

    def h6():
        os.system(f'wit copy "{nf}" "{nf}.wbfs" -o')
        e6.destroy()

    def h7():
        os.system(f'wit copy "{ng}" "{ng}.wbfs" -o')
        e7.destroy()

    def h8():
        os.system(f'wit copy "{nh}" "{nh}.wbfs" -o')
        e8.destroy()

    def h9():
        os.system(f'wit copy "{ni}" "{ni}.wbfs" -o')
        e9.destroy()

    def h10():
        os.system(f'wit copy "{nj}" "{nj}.wbfs" -o')
        e10.destroy()

    def h11():
        os.system(f'wit copy "{nk}" "{nk}.wbfs" -o')
        e11.destroy()

    def h12():
        os.system(f'wit copy "{nl}" "{nl}.wbfs" -o')
        e12.destroy()

    def h13():
        os.system(f'wit copy "{nm}" "{nm}.wbfs" -o')
        e13.destroy()

    def h14():
        os.system(f'wit copy "{nn}" "{nn}.wbfs" -o')
        e14.destroy()

    def h15():
        os.system(f'wit copy "{no}" "{no}.wbfs" -o')
        e15.destroy()

    for u in os.listdir('./'):
        if not os.path.isfile(u):
            continue
        y = os.path.getsize(u)
        if y < 17:
            continue
        b = open(u, "rb")
        b.seek(32)
        c = b.read(16)
        b.seek(544)
        e = b.read(16)
        b.close()
        if c == b"MARIO SPORTS MIX":
            if i == 0:
                g = Label(a, text='iso extract', font=500, bg='#aaffaa', height=3)
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
        if e == b"MARIO SPORTS MIX":
            f = f + 1
            if f == 1:
                g = Label(a, text='wbfs extract', font=500, bg='#aaffaa', height=3)
                g.grid(row=8, columnspan=20)
            i = i + 1
            if i == 1:
                w1 = u
                b1 = Button(a, text=w1, command=g1, activebackground='#a9ff91', width=30)
                b1.grid(row=11, column=1)
            if i == 2:
                w2 = u
                b2 = Button(a, text=w2, command=g2, activebackground='#a9ff91', width=30)
                b2.grid(row=11, column=0)
            if i == 3:
                w3 = u
                b3 = Button(a, text=w3, command=g3, activebackground='#a9ff91', width=30)
                b3.grid(row=11, column=2)
            if i == 4:
                w4 = u
                b4 = Button(a, text=w4, command=g4, activebackground='#a9ff91', width=30)
                b4.grid(row=12, column=1)
            if i == 5:
                w5 = u
                b5 = Button(a, text=w5, command=g5, activebackground='#a9ff91', width=30)
                b5.grid(row=12, column=0)
            if i == 6:
                w6 = u
                b6 = Button(a, text=w6, command=g6, activebackground='#a9ff91', width=30)
                b6.grid(row=12, column=2)
            if i == 7:
                w7 = u
                b7 = Button(a, text=w7, command=g7, activebackground='#a9ff91', width=30)
                b7.grid(row=13, column=1)
            if i == 8:
                w8 = u
                b8 = Button(a, text=w8, command=g8, activebackground='#a9ff91', width=30)
                b8.grid(row=13, column=0)
            if i == 9:
                w9 = u
                b9 = Button(a, text=w9, command=g9, activebackground='#a9ff91', width=30)
                b9.grid(row=13, column=2)
    for n in os.listdir('./'):
        if not os.path.isdir(n):
            continue
        m = m + 1
        if m == 1:
            g = Label(a, text='iso create', font=500, bg='#aaffaa', height=3)
            g.grid(row=15, column=0, rowspan=2)
            g = Label(a, text='the process can takes\nup to 5 minutes', font=150, bg='#aaffaa')
            g.grid(row=15, column=1, rowspan=2)
            s = Label(a, text='wbfs create', font=500, bg='#aaffaa', height=3)
            s.grid(row=15, column=2, rowspan=2)
            na = n
            d1 = Button(a, text=na, command=i1, activebackground='#a9ff91', width=30)
            d1.grid(row=17, column=0)
            e1 = Button(a, text=na, command=h1, activebackground='#a9ff91', width=30)
            e1.grid(row=17, column=2)
        if m == 2:
            nb = n
            d2 = Button(a, text=nb, command=i2, activebackground='#a9ff91', width=30)
            d2.grid(row=18, column=0)
            e2 = Button(a, text=nb, command=h2, activebackground='#a9ff91', width=30)
            e2.grid(row=18, column=2)
        if m == 3:
            nc = n
            d3 = Button(a, text=nc, command=i3, activebackground='#a9ff91', width=30)
            d3.grid(row=19, column=0)
            e3 = Button(a, text=nc, command=h3, activebackground='#a9ff91', width=30)
            e3.grid(row=19, column=2)
        if m == 4:
            nd = n
            d4 = Button(a, text=nd, command=i4, activebackground='#a9ff91', width=30)
            d4.grid(row=20, column=0)
            e4 = Button(a, text=nd, command=h4, activebackground='#a9ff91', width=30)
            e4.grid(row=20, column=2)
        if m == 5:
            ne = n
            d5 = Button(a, text=ne, command=i5, activebackground='#a9ff91', width=30)
            d5.grid(row=21, column=0)
            e5 = Button(a, text=ne, command=h5, activebackground='#a9ff91', width=30)
            e5.grid(row=21, column=2)
        if m == 6:
            nf = n
            d6 = Button(a, text=nf, command=i6, activebackground='#a9ff91', width=30)
            d6.grid(row=22, column=0)
            e6 = Button(a, text=nf, command=h6, activebackground='#a9ff91', width=30)
            e6.grid(row=22, column=2)
        if m == 7:
            ng = n
            d7 = Button(a, text=ng, command=i7, activebackground='#a9ff91', width=30)
            d7.grid(row=23, column=0)
            e7 = Button(a, text=ng, command=h7, activebackground='#a9ff91', width=30)
            e7.grid(row=23, column=2)
        if m == 8:
            nh = n
            d8 = Button(a, text=nh, command=i8, activebackground='#a9ff91', width=30)
            d8.grid(row=24, column=0)
            e8 = Button(a, text=nh, command=h8, activebackground='#a9ff91', width=30)
            e8.grid(row=24, column=2)
        if m == 9:
            ni = n
            d9 = Button(a, text=ni, command=i9, activebackground='#a9ff91', width=30)
            d9.grid(row=25, column=0)
            e9 = Button(a, text=ni, command=h9, activebackground='#a9ff91', width=30)
            e9.grid(row=25, column=2)
        if m == 10:
            nj = n
            d10 = Button(a, text=nj, command=i10, activebackground='#a9ff91', width=30)
            d10.grid(row=26, column=0)
            e10 = Button(a, text=nj, command=h10, activebackground='#a9ff91', width=30)
            e10.grid(row=26, column=2)
        if m == 11:
            nk = n
            d11 = Button(a, text=nk, command=i11, activebackground='#a9ff91', width=30)
            d11.grid(row=27, column=0)
            e11 = Button(a, text=nk, command=h11, activebackground='#a9ff91', width=30)
            e11.grid(row=27, column=2)
        if m == 12:
            nl = n
            d12 = Button(a, text=nl, command=i12, activebackground='#a9ff91', width=30)
            d12.grid(row=28, column=0)
            e12 = Button(a, text=nl, command=h12, activebackground='#a9ff91', width=30)
            e12.grid(row=28, column=2)
        if m == 13:
            nm = n
            d13 = Button(a, text=nm, command=i13, activebackground='#a9ff91', width=30)
            d13.grid(row=29, column=0)
            e13 = Button(a, text=nm, command=h13, activebackground='#a9ff91', width=30)
            e13.grid(row=29, column=2)
        if m == 14:
            nn = n
            d14 = Button(a, text=nn, command=i14, activebackground='#a9ff91', width=30)
            d14.grid(row=30, column=0)
            e14 = Button(a, text=nn, command=h14, activebackground='#a9ff91', width=30)
            e14.grid(row=30, column=2)
        if m == 15:
            no = n
            d15 = Button(a, text=no, command=i15, activebackground='#a9ff91', width=30)
            d15.grid(row=31, column=0)
            e15 = Button(a, text=no, command=h15, activebackground='#a9ff91', width=30)
            e15.grid(row=31, column=2)


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
E = Label(a, text='Current working directory is', bg='#aaffaa', width=30)
E.grid(row=0, column=0)
F = Label(a, text=B, bg='#aaffaa', width=30)
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
