import os

extensions = ['.mdl', '.bin', '.cmp']  # extensions of compressed files recognized
for cfile in os.listdir('./'):
    ismodel = iscmp = False
    try:
        if not os.path.isfile(cfile):
            continue
        size = cursor = os.path.getsize(cfile)
        if size < 8:
            continue
        with open(cfile, 'rb') as mdl_check:
            if mdl_check.read(4) not in [b'U\xaa8-', b'bres', b'\x00 \xaf0']:
                continue
            mdl_check.seek(0)
            if mdl_check.read(1) == b'\x00':
                iscmp = True
            if not iscmp:  # if it's not a cmp, check whether it is a mdl or else a bin.
                if b'\x00\x00\x06body_h\x00\x00' in mdl_check.read():
                    ismodel = True

    except PermissionError as error:
        print(error)
        continue

    if '_' in cfile:
        shortname = cfile.rsplit('_', 1)[0]  # if there is a _ in the file name, everything after is just the extension
    elif '.' in cfile:
        shortname = os.path.splitext(cfile)[0]  # if there is a . in the file name
    else:
        shortname = cfile  # else compressed file name will be the file name + its right extension
    if ismodel:                                             # future compressed file if it exists  ( == overwrite )
        os.system(f'n "{cfile}" -lh -o "{shortname}.mdl" -A32')  # create a compressed file with mdl extension
    elif iscmp:
        os.system(f'n "{cfile}" -lh -o "{shortname}.cmp" -A32')
    else:
        os.system(f'n "{cfile}" -lh -o "{shortname}.bin" -A32')
