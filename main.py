import morse_code
import re

input_string = input()

isMorse = False

if input_string[0] in ('-', '.'):
    isMorse = True

res = ""
if isMorse:
    words = re.split('   |  / ', input_string)
    for word in words:
        letters = word.split(' ')
        for letter in letters:
            if letter not in morse_code.morse_to_letters.keys():
                print(f'"{letter}" is not a morse letter')
                exit()
            res += morse_code.morse_to_letters[letter]
        res += ' '
    res = res[:-1]
else:
    words = re.split(' ', input_string)
    for word in words:
        letters = list(word)
        for letter in letters:
            if letter not in morse_code.letters_to_morse.keys():
                print(f'"{letter}" this is not a letter')
                exit()
            res += morse_code.letters_to_morse[letter] + ' '
        res += ' / '
    res = res[:-3]

print(res)