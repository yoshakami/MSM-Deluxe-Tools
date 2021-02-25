import os

extensions = ['.mdl', '.bin', '.cmp']  # extensions of compressed files recognized
for cfile in os.listdir('./'):
    if not os.path.isfile(cfile):
        continue
    ismodel = iscmp = False
    size = cursor = os.path.getsize(cfile)
    if size > 8:
        if size < 2222:  # if the size is very little, don't trigger the while, it's definitely not a mdl file
            cursor = -3333
        cursor -= 8  # cursor = size - 8
        with open(cfile, 'rb') as mdl_check:
            if mdl_check.read(4) not in [b'U\xaa8-', b'bres', b'\x00 \xaf0']:
                continue
            if mdl_check.read(1) == b'\x00':
                iscmp = True
            if not iscmp:  # if it's not a cmp, check whether it is a mdl or else a bin.
                while cursor > size - 2222:
                    cursor -= 1
                    mdl_check.seek(cursor)
                    data = mdl_check.read(7)
                    if data == b'\x06body_h':  # all mdl does have this text before their end (a mdl0 named body_h)
                        ismodel = True
                        break
    if '_' in cfile:
        shortname = cfile.rsplit('_', 1)[0]  # if there is a _ in the file name, everything after is just the extension
    elif '.' in cfile:
        shortname = os.path.splitext(cfile)[0]  # if there is a . in the file name
    else:
        shortname = cfile  # else compressed file name will be the file name + its right extension
    for i in range(3):
        if f"{shortname}{extensions[i]}" != cfile:  # don't delete the file the script will compress!
            os.system(f'del "{shortname}{extensions[i]}"')  # delete the mdl, cmp, or bin file with the same name as the
    if ismodel:                                             # future compressed file if it exists  ( == overwrite )
        os.system(f'n "{cfile}" -lh -o "{shortname}.mdl"')  # create a compressed file with mdl extension
    elif iscmp:
        os.system(f'n "{cfile}" -lh -o "{shortname}.cmp"')
    else:
        os.system(f'n "{cfile}" -lh -o "{shortname}.bin"')
