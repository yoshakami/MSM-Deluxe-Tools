import os
import sys
from subprocess import Popen
script = str(sys.argv[1])
install_dir = os.path.dirname(os.path.abspath(__file__))
Popen(('wscript.exe', os.path.join(install_dir, f"{script}.vbs")))
