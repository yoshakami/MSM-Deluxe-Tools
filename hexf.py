import pyperclip, struct


def hex_float(number):
    number = number.replace(',', '.')  # replaces coma with dots
    value = 0
    w = hex(struct.unpack('<I', struct.pack('<f', float(number)))[0])[2:]
    while len(w) < 8:  # add zeros to always make the value length to 8
        value += 1
    w = '0' * value + w
    pyperclip.copy(w)  # copy hex float number to clipboard
    return f"copied to clipboard the below value\n{w}\n\n"


while True: # forever
    entry = input("decimal value : ")
    print(hex_float(entry))
