# AZBUKA MORZE
import string

def morze(word):
    alphabet = []
    morze_alphabet = ['*-', '-***', '-*-*', '-**', '*', '**-*', '--*', '****', '**', '*---', '-*-', '*-**', '--',
                      '-*', '---', '*--*', '--*-', '*-*', '***', '-', '**-', '***-', '*--', '-**-', '-*--', '--**']
    for letter in string.ascii_uppercase:
        alphabet.append(letter)
    morze_dict = dict(zip(alphabet, morze_alphabet))
    print(morze_dict)

    code_phrase = []
    for letter in word:
        code_phrase.append(letter.upper())
    print(code_phrase)
    print(return_phrase)

    return_phrase = []
    
morze('hello')
