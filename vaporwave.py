import pyperclip
import os

install_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(install_dir, '#language.txt'), 'r', encoding="utf-8") as txt:
    language = txt.read()
    language = [''] + language.splitlines()

start = int(language[1].split(":")[5])
while True:  # forever
    message = ''
    text = input(language[start + 7])
    for letter in text:
        if letter == ' ':
            message += '   '
        else:
            message += letter + ' '
    print(f"{message}\n")
    pyperclip.copy(message)
