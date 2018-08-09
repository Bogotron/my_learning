# AZBUKA MORZE
import string

def morze_word(word):
    alphabet = []
    morze_alphabet = ['*-', '-***', '-*-*', '-**', '*', '**-*', '--*', '****', '**', '*---', '-*-', '*-**', '--',
                      '-*', '---', '*--*', '--*-', '*-*', '***', '-', '**-', '***-', '*--', '-**-', '-*--', '--**']
    for letter in string.ascii_uppercase:
        alphabet.append(letter)
    morze_dict = dict(zip(alphabet, morze_alphabet))

    code_phrase = []
    for letter in word:
        if letter.upper() in string.ascii_uppercase:
            key = letter.upper()
            code_phrase.append(morze_dict[key])
        else:
            break
    print(code_phrase)

def morze_phrase(*args):
    morze_list = list(map(morze_word, args))
    return morze_list

morze_phrase('Hello', 'world')

'Надо добавить обработку пробела для функции morze_word'