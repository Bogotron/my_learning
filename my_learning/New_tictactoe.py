field = [" ", " ", " ", " ", " ", " ", " ", " ", " ",]

def start_game():
    starter = ''
    while not (starter == "Y" or starter == "N"):
        starter = input('You want to play? Y or N: ').upper()
        if starter == 'Y':
            return True
        elif starter == 'N':
            return False

def side_choice():
    marker = ""
    while marker != "X" and marker != "O":
        marker = input('Player one please choise side X or O: ').upper()
        if marker == "X":
            return ("X", "O")
        elif marker == "O":
            return ("O", "X")

def turn(player_choise):
    turn_number = 0
    while turn_number < 9:
        try:
            marker = int(input('Enter your field position 1-9: '))
            if field[marker] == " ":
                field[marker] = player_choise[turn_number%2]
                print("Next player")
                print(field[0] + field[1] + field[2])
                print(field[3] + field[4] + field[5])
                print(field[6] + field[7] + field[8])
                turn_number += 1
        except ValueError and IndexError:
            print("Enter your field position please!")               


def victory_check(field, marker):
    return (marker in (field[0] and field[1] and field [2]) or 
            marker in (field[3] and field[4] and field [5]) or
            marker in (field[6] and field[7] and field [8]) or 
            marker in (field[0] and field[3] and field [6]) or
            marker in (field[1] and field[4] and field [7]) or
            marker in (field[2] and field[5] and field [8]) or
            marker in (field[0] and field[4] and field [8]) or
            marker in (field[2] and field[4] and field [6])
            )

def game_field():
    pass


#MAIN GAME

if start_game() == True:
    side_choice()
    turn()