import os

apps = ['arc.py', 'brsar.pyw', 'bstick.pyw', 'c.py', 'dec.py', 'dump.py', 'hexf.py', 'int.py', 'iso.py', 'isox.py', 'lh.py',
        'map.pyw', 'msm.pyw', 'msmhelp.pyw', 'msmshortcuts.pyw', 'p.py', 'pack.pyw', 'png.py', 'rEtUrN-tExT.py',
        't.py', 'tex.py', 'tex3.pyw', 'thp.pyw', 'trib.py', 'vaporwave.py', 'web.pyw', 'x.py']

for software in apps:
    script = os.path.splitext(software)[0]
    with open(f"{script}.c", 'w') as vbs:
        vbs.write('#include <stdlib.h>\n#define _WIN32_WINNT 0x0500\n#include <windows.h>\n\nint main()\n{\n    ')
        vbs.write('HWND hWnd = GetConsoleWindow();\n    ShowWindow( hWnd, SW_HIDE );\n    ')
        vbs.write(f'system("{script}.vbs");\n    ')
        vbs.write('return 0;\n}')
