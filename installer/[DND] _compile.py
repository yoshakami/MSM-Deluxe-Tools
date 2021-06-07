import os # this is a drag and drop script, drag any .c file into this script to compile it, -Os optimized for size, -Wall shows all warnings, -o output file
from sys import argv
for i in range(1, len(argv)):
    os.system(f'gcc "{argv[i]}" -Os -Wall -o "{os.path.splitext(argv[i])[0]}.exe"')
os.system('pause')