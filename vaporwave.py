import pyperclip

with open('#language.txt', 'r') as txt:
    language = txt.read()
    language = [''] + language.splitlines()

while True:  # forever
    message = ''
    text = input(language[163])
    for letter in text:
        if letter == ' ':
            message += '   '
        else:
            message += letter + ' '
    print(f"{message}\n")
    pyperclip.copy(message)
