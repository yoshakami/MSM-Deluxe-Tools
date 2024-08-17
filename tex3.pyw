import os
from win10toast import ToastNotifier

if ':\\Windows' in os.getcwd():
    os.chdir(os.environ['userprofile'] + '\\Desktop')
    
install_dir = os.path.dirname(os.path.abspath(__file__))
    
with open(os.path.join(install_dir, '#language.txt'), 'r', encoding="utf-8") as txt:
    language = txt.read()
    language = [''] + language.splitlines()

hashtag = int(language[1].split(":")[3])
count_tex = count_files = 0
for element in os.listdir('./'):
    cursor = 0
    if os.path.isfile(element):  # check if it's not a directory
        size = os.path.getsize(element) - 17  # max size to look at into the file, cursor never exceeds the file size
        try:
            with open(element, 'r+b') as file:
                if file.read(4) in [b'U\xaa8-', b'bres', b'TEX0']:  # if it's an arc, brres, or a tex0
                    count_files += 1  # will be displayed on the notification
                    while cursor < size:
                        file.seek(cursor)
                        if file.read(4) == b'TEX0':  # texture magic
                            count_tex += 1  # counts the number of textures found
                            file.seek(cursor + 11)  # 11 byte after the texture magic is the texture version
                            file.write(b'\x03')
                        cursor += 16  # texture headers are always starting at an offset multiple of 16

        except PermissionError:
            continue
msm_stuff = os.path.join('msm_stuff', 'tex3.ico')
ico = os.path.join(install_dir, msm_stuff)
toaster = ToastNotifier()
toaster.show_toast(language[hashtag + 5].replace("#", str(count_tex)), language[hashtag + 6].replace("#", str(count_files)), icon_path=ico, duration=5)
