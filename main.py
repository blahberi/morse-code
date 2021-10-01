import morse_code
import re

input_string = input()

isMorse = False

if input_string.split(' ')[0] in morse_code.morse_to_letters.keys():
    isMorse = True

res = ""
if isMorse:
    words = re.split('   |  / ', input_string)
    for word in words:
        letters = word.split(' ')
        for letter in letters:
            res += morse_code.morse_to_letters[letter]
        res += ' '
    res = res[:-1]
else:
    words = re.split(' ', input_string)
    for word in words:
        letters = list(word)
        for letter in letters:
            res += morse_code.letters_to_morse[letter] + ' '
        res += ' / '
    res = res[:-3]

print(res)