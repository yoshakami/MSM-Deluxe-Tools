import os

for lh_file in os.listdir('./'):
    if os.path.isfile(lh_file):
        if os.path.getsize(lh_file) >4:
            with open(lh_file, 'rb') as check_lh_file:
                if check_lh_file.read(1) == b'@':
                    os.system(f'n "{lh_file}" -x')  # n.exe extracts the file
