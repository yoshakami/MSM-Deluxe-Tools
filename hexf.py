import pyperclip
import struct

with open('#language.txt', 'r') as txt:
    language = txt.read()
    language = [''] + language.splitlines()


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
    return f"{language[83]}\n{w}\n\n"



print(language[94] + '\n')
while True:  # forever
    entry = input(language[95])
    print(hex_float(entry))
