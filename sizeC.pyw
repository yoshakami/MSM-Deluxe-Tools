import os
from win10toast import ToastNotifier

install_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(install_dir, '#language.txt'), 'r', encoding="utf-8") as txt:
    language = txt.read()
    language = [''] + language.splitlines()

start = int(language[1].split(":")[5])
message = ''
for e in ["C:/hiberfil.sys", "C:/pagefile.sys", "C:/swapfile.sys"]:
    if os.path.exists(e):
        size = os.path.getsize(e)
        if size//1024**3 != 0:
            message += f"{e} - {round(size/1024**3,3)} GB\n"
        else:
            message += f"{e} - {round(size/1024**2,3)} MB\n"
msm_stuff = os.path.join('msm_stuff', 'sizeC.ico')
ico = os.path.join(install_dir, msm_stuff)
message = message[:-1]  # minus the last character which is '\n' or '0x0A'
toaster = ToastNotifier()
toaster.show_toast(language[start + 8], message, icon_path=ico, duration=5)
