import os

if ':\\Windows' in os.getcwd():
    os.chdir(os.environ['userprofile'] + '\\Desktop')
    
install_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(install_dir, '#language.txt'), 'r', encoding="utf-8") as txt:
    language = txt.read()
    language = [''] + language.splitlines()
    
for lh_file in os.listdir('./'):
    if os.path.isfile(lh_file):
        if os.path.getsize(lh_file) > 4:
            try:
                with open(lh_file, 'rb') as check_lh_file:
                    if check_lh_file.read(1) in [b'@', b'\x10', b'\x11', b'\x81', b'\x82', b'$', b'(', b'0', b'P']:  # lh @, old lz \x10, lz77 \x11, diff8 \x81, diff16 \x82, huff4 $, huff8 (, runlength 0, lrc P
                        os.system(f'n "{lh_file}" -x')  # n.exe extracts the file

            except PermissionError as error:
                print(error)
                continue
