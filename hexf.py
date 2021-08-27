import pyperclip
import struct

with open('C:\\Yosh\\#language.txt', 'r', encoding="utf-8") as txt:
    language = txt.read()
    language = [''] + language.splitlines()

start = int(language[1].split(":")[5])


def hex_float(number):
    try:
        number = number.replace(',', '.')  # replaces coma with dots
        w = hex(struct.unpack('<I', struct.pack('<f', float(number)))[0])[2:]
    except OverflowError as error:
        return error
    except ValueError as error:
        return error
    # add zeros to always make the value length to 8
    w = '0' * (8 - len(w)) + w[:8]
    pyperclip.copy(w)  # copy hex float number to clipboard
    return f"{language[start + 2]}\n{w}\n\n"  # copied to clipboard the value below


# Welcome ! this app is used to convert any number to hexadecimal float, size fixed to 4 bytes
print(language[start + 3] + '\n')
while True:  # forever
    entry = input(language[start + 4])  # decimal value :
    print(hex_float(entry))
