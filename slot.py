import os

if ':\\Windows' in os.getcwd():
    os.chdir(os.environ['userprofile'] + '\\Desktop')

with open('C:\\Yosh\\#language.txt', 'r', encoding="utf-8") as txt:
    language = txt.read()
    language = [''] + language.splitlines()

start = int(language[1].split(":")[5])
base_slot = []
extensions = ['.mdl', '.mot']  # extensions of compressed files recognized
double = [2, 3, 14, 15, 17]  # peach, daisy, ninja, white mage, and black mage have 2 colour variants
quadruple = [4, 9]  # yoshi and toad have 4 colour variants


def unbreakable_int_input(a, b):
    value = '18'
    while not value.isdigit() or value == '18':
        try:
            while int(value) < a or int(value) > b:
                print(f'\n{language[start + 15]}')
                value = input(language[start + 16])
        except ValueError or OverflowError:
            value = '18'
            continue
    return int(value)


for file in os.listdir('./'):
    if not os.path.isfile(file):
        continue
    if os.path.splitext(file)[-1] in extensions and file[0] == 'c':
        base_slot.append(file)

new_slot = []
if base_slot != []:
    max = index = 0
    for i in range(18):
        count = 0
        for file in base_slot:
            if file[:3] == f'c{str(i).zfill(2)}':
                count += 1
        if count > max:
            max = count
            index = i
    for name in base_slot:
        if int(name[1:3]) == index:
            new_slot.append(name)  # list.remove isn't working fine in a loop apparently so I used list.append instead
    print(language[start + 17])
    for filename in new_slot:
        print(f'-{filename}')
    print()
    for z in range(18):  # list of characters id from 0 to 17
        print(language[start + 18 + z])
    print()
    print(language[start + 36])
    number = input(language[start + 16])  # asks the user to enter a valid integer between 0 and 17
    if not number.isdigit():
        number = unbreakable_int_input(0, 17)  # else it triggers the unbreakable function while it's not valid.

    number = int(number)
    if number < 0 or number > 17:  # can't combine with the if above because int() would throw ValueError
        number = unbreakable_int_input(0, 17)

    n = color = 0
    if number in double:
        n = 2
    if number == 16:  # Slime has 3 colour variants
        n = 3
    if number in quadruple:
        n = 4

    if n != 0:
        print('\n')
        for j in range(n):
            print(f'{j} = {language[start + 37]} {j}')
        print()
        color = input(language[start + 38])
        if not color.isdigit():
            color = unbreakable_int_input(0, n - 1)
        if int(color) < 0 or int(color) > n - 1:
            color = unbreakable_int_input(0, n - 1)
    asked = False
    for files in new_slot:
        if files[-3:] == "mdl":
            new_mdl = f'c{str(number).zfill(2)}{files[3]}{str(color).zfill(2)}.mdl'
            if os.path.exists(new_mdl) and new_mdl != files:
                if not asked:
                    input(language[start + 39])  # Press enter to overwrite...
                    asked = True
                os.remove(new_mdl)
            os.rename(files, new_mdl)
        else:  # the script already verified only mdl and mot files are in this list
            new_mot = f'c{str(number).zfill(2)}{files[3:]}'
            if os.path.exists(new_mot) and new_mot != files:
                if not asked:
                    input(language[start + 39])  # Press enter to overwrite...
                    asked = True
                os.remove(new_mot)
            os.rename(files, new_mot)
