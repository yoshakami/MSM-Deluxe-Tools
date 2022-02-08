import os

if ':\\Windows' in os.getcwd():
    os.chdir(os.environ['userprofile'] + '\\Desktop')

with open('C:\\Yosh\\#language.txt', 'r', encoding="utf-8") as txt:
    language = txt.read()
    language = [''] + language.splitlines()

start = int(language[1].split(":")[5])
base_slot = []
extensions = ['.mdl', '.mot', '.brstm']  # extensions of files recognized
first_letter = ['V', 'm', 'c']  # first letter of filenames recognized
double = [2, 3, 14, 15, 17, 18]  # peach, daisy, ninja, white mage, black mage, and shy guy have 2 colour variants
quadruple = [4, 9]  # yoshi and toad have 4 colour variants
charsound = [[], [], [], [], [], [], [], [], [], [], [], [],
             # characters in slot 0 to 11 use the same file name pattern
             ["VOICE_STRM_C12_126_T2_ST_C14.brstm",
              "VOICE_STRM_C12_130_T2_ST_C14.brstm",
              "VOICE_STRM_C12_20_T1_ST_C14.brstm",
              "VOICE_STRM_C12_127_T2_ST_C14.brstm"],
             ["m_sabo_pu1.brstm",  # pycharm auto formatting, I guess it's how the PEP8 wants scripts to look like
              "m_sabo_s_atk1.brstm",
              "m_sabo_ag2.brstm",
              "m_sabo_id1.brstm"],
             ["VOICE_STRM_C14_251_YES.brstm",
              "VOICE_STRM_C14_246_YES.brstm",
              "VOICE_STRM_C14_256_YES.brstm",
              "VOICE_STRM_C14_252_YES.brstm"],
             ["VOICE_STRM_C15_226_STRM_C14.brstm",
              "VOICE_STRM_C15_170_WIN.brstm",
              "VOICE_STRM_C15_210_STRM_C14.brstm",
              "VOICE_STRM_C15_218_STRM_C14.brstm"],
             ["VOICE_C16_ACTION_S1.brstm",
              "VOICE_C16_ACTION_M1.brstm",
              "VOICE_C16_ACTION_L3.brstm",
              "VOICE_C16_ACTION_M3.brstm"],
             ["VOICE_C17_87_VO_ST_C14.brstm",
              "VOICE_C17_58_STRM_C14.brstm",
              "VOICE_C17_55_STRM_C14.brstm",
              "VOICE_C17_52_STRM_C14.brstm"], []]

for i in range(12):
    charsound[i] = [f"VOICE_STRM_C{str(i).zfill(2)}_00.brstm", f"VOICE_STRM_C{str(i).zfill(2)}_01.brstm",
                    f"VOICE_STRM_C{str(i).zfill(2)}_02.brstm", f"VOICE_STRM_C{str(i).zfill(2)}_03.brstm"]


def unbreakable_int_input(a, b):
    value = '99'
    while not value.isdigit() or value == '99':
        try:
            while int(value) < a or int(value) > b:
                print(f'\n{language[start + 15]}')
                value = input(language[start + 16])
        except ValueError or OverflowError:
            value = '99'
            continue
    return int(value)


for file in os.listdir('./'):
    if not os.path.isfile(file):
        continue
    if os.path.splitext(file)[-1] in extensions and file[0] in first_letter:
        base_slot.append(file)

new_slot = []
if base_slot != []:
    max = source = 0
    for i in range(19):
        count = 0
        for file in base_slot:
            if file[:3] == f'c{str(i).zfill(2)}' or file in charsound[i]:
                count += 1
        if count > max:
            max = count
            source = i
    for name in base_slot:
        if name[1:3] == str(source).zfill(2) or name in charsound[source]:
            new_slot.append(name)  # list.remove isn't working fine in a loop apparently so I used list.append instead
    print(language[start + 17])
    for filename in new_slot:
        print(f'-{filename}')
    print()
    for z in range(19):  # list of characters id from 0 to 18
        print(language[start + 18 + z])
    print()
    print(language[start + 37])
    dest = input(language[start + 16])  # asks the user to enter a valid integer between 0 and 17
    if not dest.isdigit():
        dest = unbreakable_int_input(0, 18)  # else it triggers the unbreakable function while it's not valid.

    dest = int(dest)
    if dest < 0 or dest > 18:  # can't combine with the if above because int() would throw ValueError
        dest = unbreakable_int_input(0, 18)

    n = color = 0
    if dest in double:
        n = 2
    if dest == 16:  # Slime has 3 colour variants
        n = 3
    if dest in quadruple:
        n = 4

    if n != 0:
        print('\n')
        for j in range(n):
            print(f'{j} = {language[start + 38]} {j}')
        print()
        color = input(language[start + 39])
        if not color.isdigit():
            color = unbreakable_int_input(0, n - 1)
        if int(color) < 0 or int(color) > n - 1:
            color = unbreakable_int_input(0, n - 1)
    asked = False
    for file in new_slot:
        if file[-3:] == "mdl":
            if dest == 18:
                # print('yes')
                new_mdl = f'c{str(dest).zfill(2)}{file[3]}1{str(color)}.mdl'
            else:
                new_mdl = f'c{str(dest).zfill(2)}{file[3]}{str(color).zfill(2)}.mdl'
            if os.path.exists(new_mdl) and new_mdl != file:
                if not asked:
                    input(language[start + 40])  # Press enter to overwrite...
                    asked = True
                os.remove(new_mdl)
            os.rename(file, new_mdl)
        elif file[-3:] == "mot":  # the script already verified only mdl and mot files are in this list
            new_mot = f'c{str(dest).zfill(2)}{file[3:]}'
            if os.path.exists(new_mot) and new_mot != file:
                if not asked:
                    input(language[start + 40])  # Press enter to overwrite...
                    asked = True
                os.remove(new_mot)
            os.rename(file, new_mot)
        elif file[-5:] == "brstm" and dest != 18:  # the script already verified only mdl and mot files are in this list
            # if number < 12 and files[:13] == 'VOICE_STRM_C' and files[13:15] not in ['12', '14', '15']:
            #   new_brstm = f'VOICE_STRM_C{str(number).zfill(2)}{file[15:]}'
            new_brstm = file  # default value because it's defined in a if, but it should never be file except if source == dest
            for j in range(4):
                if charsound[source][j] == file:
                    new_brstm = charsound[dest][j]

            if os.path.exists(new_brstm) and new_brstm != file:
                if not asked:
                    input(language[start + 40])  # Press enter to overwrite...
                    asked = True
                os.remove(new_brstm)
            os.rename(file, new_brstm)
