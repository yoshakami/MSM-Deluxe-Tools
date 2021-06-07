import pyperclip
import struct

with open('#language.txt', 'r') as txt:
    language = txt.read()
    language = [''] + language.splitlines()

hexl = ["0", "1", "2", "3", "4", "5", '6', '7', '8', '9', 'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F']
print(language[96] + "\n")
while True: #forever
    nospace = ''
    entry = input("\n" + language[97])
    for letter in entry:
        if letter in hexl:
            nospace += letter
    nospace = '0x' + nospace
    try:
        number = str(int(nospace, 16))
    except ValueError as error:
        print(error)
        continue
    print(f'{language[83]}\n{number}\n')
    pyperclip.copy(number)
