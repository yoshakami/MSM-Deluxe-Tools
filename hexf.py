import pyperclip
import struct


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
    return f"copied to clipboard the value below\n{w}\n\n"



print('Welcome ! this app is used to convert any number to hexadecimal float, size fixed to 4 bytes\n')
while True:  # forever
    entry = input("decimal value : ")
    print(hex_float(entry))
