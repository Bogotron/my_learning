# AZBUKA MORZE
import string

def morze(word):
    alphabet = []
    morze_alphabet = ['*-', '-***', '-*-*', '-**', '*', '**-*', '--*', '****', '**', '*---', '-*-', '*-**', '--',
                      '-*', '---', '*--*', '--*-', '*-*', '***', '-', '**-', '***-', '*--', '-**-', '-*--', '--**']
    return_phrase = []
    for letter in string.ascii_uppercase:
        alphabet.append(letter)
    morze_dict = dict(zip(alphabet, morze_alphabet))

    key_values = []
    for letter in word.upper():
        key_values.append(letter)

    print(key_values)
    for key in key_values:
        

morze('hello')
