import os
import random
if os.path.exists('./files'):
    os.chdir('./files')
if os.path.exists('./gmkparam'):
    os.chdir('./gmkparam')

count = [1]

def randomize():
    files = os.listdir('./')
    random.shuffle(files)
    print(files)
    while not files[0].startswith('gp'):
        files.remove(files[0])
    with open(files[0], 'rb') as first_gmk:
        gmk1 = first_gmk.read()
    print(f'Writing {files[0]} in ', end='')

    for gmk in files:
        if not gmk.startswith('gp'):
            continue
        count[0] += 1
        print(f'{gmk}\nWriting {gmk} in ', end='')
        with open(gmk, 'rb') as gmk_file:
            gmk2 = gmk_file.read()
        with open(gmk, 'wb') as random_gmk:
            random_gmk.write(gmk1)
        gmk1 = gmk2
    print(f'{files[0]}\n')
    with open(files[0], 'wb') as first_gmk:
        first_gmk.write(gmk1)

if ':\\Windows' in os.getcwd():
    os.chdir(os.environ['userprofile'] + '\\Desktop')

install_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(install_dir, '#language.txt'), 'r', encoding="utf-8") as txt:
    language = txt.read()
    language = [''] + language.splitlines()

start = int(language[1].split(":")[33])
hashtag = int(language[1].split(":")[3])

input(language[hashtag + 14].replace('#', os.getcwd()) + '\n' + language[start + 4])
randomize()
input(language[hashtag + 15] + "\n" + language[start + 1])