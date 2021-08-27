import sys
import os
for i in range(1, len(sys.argv)):
    os.system(f'python -m nuitka --mingw64 "{sys.argv[i]}"')