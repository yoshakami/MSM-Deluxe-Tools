import os
from win10toast import ToastNotifier

with open('C:\\Yosh\\#language.txt', 'r', encoding="utf-8") as txt:
    language = txt.read()
    language = [''] + language.splitlines()

start = int(language[1].split(":")[5])
message = ''
for e in ["C:\\hiberfil.sys", "C:\\pagefile.sys", "C:\\swapfile.sys"]:
    if os.path.exists(e):
        size = os.path.getsize(e)
        if size//1024**3 != 0:
            message += f"{e} - {round(size/1024**3,3)} GB\n"
        else:
            message += f"{e} - {round(size/1024**2,3)} MB\n"

message = message[:-1]  # minus the last character which is '\n' or '0x0A'
toaster = ToastNotifier()
toaster.show_toast(language[start + 8], message, icon_path="C:\\Yosh\\msm_stuff\\gal.ico", duration=5)
