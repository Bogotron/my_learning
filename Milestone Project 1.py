# Milestone Project 1

#import clear display function

# Player choice
def welcome():
    while True:
        welcome_str = input('Are you ready to play? Yes or No? ')
        if welcome_str.lower() == 'yes':
            break
        elif welcome_str.lower() == 'no':
            print('Bye bye :)')
            break
        else:
            print('Please enter "yes" or "no"')

def player_choice():
    while True:
        player_1 = input('Please enter "X" or "O" to choice your side [type "Q" to exit]: ')
        if player_1.upper() == "X":
            print('Player 1 is "X"')
        elif player_1.upper() == "O":
            print('Player 1 is "O"')
        elif player_1.upper() == "Q":
            break

# Board display function
def display_board():
    board_line1 = '    |      |     '
    board_line2 = '    |      |     '
    board_line3 = '    |      |     '
    board_line_bottom = '-----------------'
    board_raer = '    |      |     '

    print(board_raer)
    print(board_line1)
    print(board_raer)
    print(board_line_bottom)
    print(board_raer)
    print(board_line2)
    print(board_raer)
    print(board_line_bottom)
    print(board_raer)
    print(board_line3)
    print(board_raer)

display_board()
