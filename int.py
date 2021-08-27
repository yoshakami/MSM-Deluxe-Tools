import pyperclip
import struct

with open('C:\\Yosh\\#language.txt', 'r', encoding="utf-8") as txt:
    language = txt.read()
    language = [''] + language.splitlines()

start = int(language[1].split(":")[5])
hexl = ["0", "1", "2", "3", "4", "5", '6', '7', '8', '9', 'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F']
print(language[start + 5] + "\n")  # see the line below
# Hi there ! This script converts any hexadecimal values like '7F FF  ffa0' into a decimal integer value, size free
while True: #forever
    nospace = ''
    entry = input("\n" + language[start + 6])   # hex values :
    for letter in entry:
        if letter in hexl:
            nospace += letter
    nospace = '0x' + nospace
    try:
        number = str(int(nospace, 16))
    except ValueError as error:
        print(error)
        continue
    print(f'{language[start + 2]}\n{number}\n')  # copied to clipboard
    pyperclip.copy(number)
