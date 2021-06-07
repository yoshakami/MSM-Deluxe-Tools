import pyperclip

with open('#language.txt', 'r') as txt:
    language = txt.read()
    language = [''] + language.splitlines()

while True:  # forever
    message = ''
    text = input(language[163])
    i = 1
    for letter in text:
        if not letter.isalpha():  # if it's not in the alphabet
            message += letter
            continue
        if i == 1:
            i = 0
            message += letter.upper()
        else:
            i = 1
            message += letter.lower()
    print(f"{message}\n")
    pyperclip.copy(message)
