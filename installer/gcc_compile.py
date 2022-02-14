import os
from sys import argv

os.chdir("C:\\Users\\yoshi\\AppData\\Local\\Nuitka\\Nuitka\\gcc\\x86_64\\10.2.0-11.0.0-8.0.0-r5\\mingw64\\bin")
for i in range(1, len(argv)):
    os.system(f'gcc "{argv[i]}" -Os -Wall -o "{os.path.splitext(argv[i])[0]}.exe"')
os.system('pause')
