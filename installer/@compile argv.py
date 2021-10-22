import os
import sys

os.system(f'python -m nuitka --mingw64 "{sys.argv[1]}" --windows-icon-from-ico="{sys.argv[2]}"')
os.system('pause')