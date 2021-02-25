import pyperclip

while True:  # forever
    message = ''
    text = input('text= ')
    for letter in text:
        if letter == ' ':
            message += '   '
        else:
            message += letter + ' '
    print(f"{message}\n")
    pyperclip.copy(message)
