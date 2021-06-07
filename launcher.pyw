import sys
from subprocess import Popen
script = str(sys.argv[1])
Popen(('wscript.exe', f"C:\\Yosh\\{script}.vbs"))