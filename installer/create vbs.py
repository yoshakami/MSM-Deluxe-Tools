import os

apps = ['arc.py', 'brsar.pyw', 'bstick.pyw', 'c.py', 'dec.py', 'dump.py', 'hexf.py', 'int.py', 'iso.py', 'isox.py', 'lh.py',
        'map.pyw', 'msm.pyw', 'msmhelp.pyw', 'msmshortcuts.pyw', 'p.py', 'pack.pyw', 'png.py', 'rEtUrN-tExT.py',
        't.py', 'tex.py', 'tex3.pyw', 'thp.pyw', 'trib.py', 'vaporwave.py', 'web.pyw', 'x.py']

for software in apps:
    i = 1
    if software[-1] == 'w':
        i = 0
    with open(f"{os.path.splitext(software)[0]}.vbs", 'w') as vbs:
        vbs.write(f'CreateObject("Wscript.Shell").Run "{os.path.splitext(software)[0]}.lnk", {i}, False')