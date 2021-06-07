import pyperclip
import struct

hexl = ["0", "1", "2", "3", "4", "5", '6', '7', '8', '9', 'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F']

with open('#language.txt', 'r') as txt:
    language = txt.read()
    language = [''] + language.splitlines()

print(language[81] + '\n')
while True:  # forever
    nospace = ''
    entry = input(language[82])
    for letter in entry:
        if letter in hexl:
            nospace += letter
    nospace = '0' * (8 - len(nospace)) + nospace[:8]  # add zeros to always make the value length to 8
    number = struct.unpack('!f', bytes.fromhex(nospace))[0]
    print(f"{language[83]}\n{number}\n\n")
    pyperclip.copy(number)  # copy converted integer to clipboard
