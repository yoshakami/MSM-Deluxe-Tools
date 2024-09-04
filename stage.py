import os
if ':\\Windows' in os.getcwd():
    os.chdir(os.environ['userprofile'] + '\\Desktop')

install_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(install_dir, '#language.txt'), 'r', encoding="utf-8") as txt:
    language = txt.read()
    language = [''] + language.splitlines()

start = int(language[1].split(":")[33])
hashtag = int(language[1].split(":")[3])

if not os.path.exists("./stage"):
    input(language[start + 12]+ "\n" + language[start + 1])
    exit()
os.chdir("./stage")
count = 0
for file in os.listdir('./'):
    if not os.path.isfile(file) or os.path.splitext(file)[-1] != ".bin":
        continue
    size = os.path.getsize(file)
    arn = b''
    fog = b''
    lgt = b''
    i = 0
    arn_bool = False
    lgt_bool = False
    fog_bool = False
    with open(file, 'rb') as brres:
        for i in range(0, size, 16):
            brres.seek(i)
            b4 = brres.read(4)
            if not any([arn_bool, lgt_bool, fog_bool]) and b4 == b'@ARN':
                arn_bool = True
                arn = b4 + brres.read(12)
            elif arn_bool:
                if b4 == b'@LGT':
                    arn_bool = False
                    lgt_bool = True
                    lgt = b4 + brres.read(12)
                else:
                    arn += b4 + brres.read(12)
            elif lgt_bool:
                if b4 == b'@FOG':
                    lgt_bool = False
                    fog_bool = True
                    fog = b4 + brres.read(12)
                else:
                    lgt += b4 + brres.read(12)
            elif fog_bool:
                b2 = brres.read(2)
                if b4 + b2 == b'\x00\x00\x00\x02\x23\x30':
                    fog_bool = False
                    break
                else:
                    fog += b4 + b2 + brres.read(10)
    try:
        os.makedirs(f"./external/{file.split('_')[0]}")
    except FileExistsError:
        pass
    if fog == b'' or arn == b'' or lgt == b'':
        if file[:3] == "s39":
            with open(f"./external/{file.split('_')[0]}/arrange.arn", 'wb') as bin:
                bin.write(arn)
            with open(f"./external/{file.split('_')[0]}/stage{file[1:3]}.lgt", 'wb') as bin:
                bin.write(lgt)
            count += 2
            continue
        print(f"problem with {file} : {arn[:4]} {lgt[:4]} {fog[:4]}")
    with open(f"./external/{file.split('_')[0]}/arrange.arn", 'wb') as bin:
        bin.write(arn)
    with open(f"./external/{file.split('_')[0]}/stage{file[1:3]}.lgt", 'wb') as bin:
        bin.write(lgt)
    with open(f"./external/{file.split('_')[0]}/stage{file[1:3]}.fog", 'wb') as bin:
        bin.write(fog)
    count += 3
print(f"{language[hashtag + 12].rsplit('#', 1)[0].replace('#', count)}{os.getcwd()}/external/")
                