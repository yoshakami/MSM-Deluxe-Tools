import os

for element in os.listdir('./'):
    cursor = 0
    if os.path.isfile(element):  # check if it's not a directory
        size = os.path.getsize(element) - 17  # max size to look at into the file, cursor never exceeds the file size
        with open(element, 'r+b') as file:
            if file.read(4) in [b'U\xaa8-', b'bres', b'TEX0']:  # if it's an arc, brres, or a tex0
                while cursor < size:
                    file.seek(cursor)
                    if file.read(4) == b'TEX0':  # texture magic
                        file.seek(cursor + 11)  # 11 byte after the texture magic is the texture version
                        file.write(b'\x03')
                    cursor += 16  # texture headers are always starting at an offset multiple of 16
