import pyperclip

with open('C:\\Yosh\\#language.txt', 'r', encoding="utf-8") as txt:
    language = txt.read()
    language = [''] + language.splitlines()

start = int(language[1].split(":")[3])
while True:  # forever
    message = ''
    text = input(language[start + 7])
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
