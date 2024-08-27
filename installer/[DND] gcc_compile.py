import os # this is a drag and drop script, drag any .c file into this script to compile it, -Os optimized for size, -Wall shows all warnings, -o output file
from sys import argv
for i in range(1, len(argv)):
    os.system(f'gcc "{argv[i]}" -o "{os.path.splitext(argv[i])[0]}.exe" -Os -s -ffunction-sections -fdata-sections -Wl,--gc-sections')
os.system('pause')
