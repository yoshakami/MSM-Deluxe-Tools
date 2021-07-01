import pyperclip
import struct

hexl = ["0", "1", "2", "3", "4", "5", '6', '7', '8', '9', 'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F']

with open('C:\\Yosh\\#language.txt', 'r', encoding="utf-8") as txt:
    language = txt.read()
    language = [''] + language.splitlines()

start = int(language[1].split(":")[3])
print(language[start] + '\n')
# Welcome ! this app is used to convert hexadecimal float values to decimal float
while True:  # forever
    nospace = ''
    entry = input(language[start + 1])  # hex-float :
    for letter in entry:
        if letter in hexl:
            nospace += letter
    nospace = '0' * (8 - len(nospace)) + nospace[:8]  # add zeros to always make the value length to 8
    number = struct.unpack('!f', bytes.fromhex(nospace))[0]
    print(f"{language[start + 2]}\n{number}\n\n")  # copied to clipboard the value below
    pyperclip.copy(number)  # copy converted integer to clipboard
