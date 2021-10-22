import os
import shutil

apps = ['arc.py', 'brsar.pyw', 'bstick.pyw', 'c.py', 'dec.py', 'dump.py', 'hexf.py', 'int.py', 'iso.py', 'isox.py',
        'lh.py', 'map.pyw', 'msm.pyw', 'msmhelp.pyw', 'p.py', 'pack.py', 'png.py', 'rEtUrN-tExT.py', 'sizeC.pyw',
        'slot.py', 't.py', 'tex.py', 'tex3.pyw', 'thp.pyw', 'trib.py', 'vaporwave.py', 'web.pyw', 'x.py', 'yt.pyw']

for file in os.listdir('../../C+icon'):
    if file not in ['launcher.pyw', '.idea', 'venv']:
        shutil.copy2(f'../../C+icon/{file}', file)
        # little edit from the installer : every exe in %PROGRAMFILES% and other in %APPDATA%

with open('./bstick.pyw', 'r+') as bstick:
    data = bstick.read()
    data = data.splitlines()
    new_data = ''
    for line in data:
        if line == '    Popen(("wscript.exe", "C:\\Yosh\\bstick.vbs"))':
            new_data += '''    Popen((f"os.environ['programfiles'].replace('\\', '\\\\')\\\\bstick.exe"))\n'''
        elif line == '    # Popen((sys.executable, "C:\\Yosh\\bstick.pyw"))':
            pass
        else:
            new_data += line + '\n'
    bstick.seek(0)
    bstick.write(new_data)
with open('./msm.pyw', 'r+', encoding="utf-8") as msm:
    data = msm.read()
    data = data.splitlines()
    new_data = ''
    for line in data:
        if line[:38] == '''    Popen(('wscript.exe', f"C:\\Yosh\\''':
            new_data += f"    Popen((f\"os.environ['programfiles'].replace('\\', '\\\\')\\\\{line[38:].split('.')[0]}.exe\"))\n"
        else:
            new_data += line + '\n'
    msm.seek(0)
    msm.write(new_data)

for file in os.listdir('../../C+icon'):
    if file not in ['launcher.pyw', '.idea', 'venv']:
        path = b'C:\\\\Yosh\\\\'
        with open(file, 'r+b') as filoc:
            content = filoc.read()
            ignore = []
            for i in range(len(content) - 9):
                filoc.seek(i)
                if filoc.read(10) != path:
                    continue
                ignore.append(i)
                ignore.append(i + 10)
        if ignore != []:
            with open(file, 'wb') as py:
                i = 0
                py.write(content[:ignore[0]] + bytes(os.environ["APPDATA"].replace('\\', '\\\\'),
                                                     'latin-1') + b'\\\\Yosh\\\\')
                for index in ignore:
                    if i == 1:
                        i = 2
                        offset = index
                    elif i == 2:
                        i = 1
                        py.write(content[offset:index] + bytes(os.environ["APPDATA"].replace('\\', '\\\\'),
                                                               'latin-1') + b'\\\\Yosh\\\\')
                    else:
                        i = 1
                py.write(content[index:])
        print(f'compiling {file}...')
        os.system(f'python -m nuitka --mingw64 "{file}" --windows-icon-from-ico="C:\\Yosh\\msm_stuff\\{os.path.splitext(file)[0]}.ico"')
