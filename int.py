import pyperclip
import struct
hexl = ["0", "1", "2", "3", "4", "5", '6', '7', '8', '9', 'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F']
print("Hi there ! This script converts any hexadecimal values like '7F FF  ffa0' into a decimal integer value, size free\n")
while True: #forever
    nospace = ''
    entry = input("\nhex values : ")
    for letter in entry:
        if letter in hexl:
            nospace += letter
    nospace = '0x' + nospace
    try:
        number = str(int(nospace, 16))
    except ValueError as error:
        print(error)
        continue
    print(f'copied to clipboard the value below\n{number}\n')
    pyperclip.copy(number)
