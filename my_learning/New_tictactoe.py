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
            print(marker[0], "will turn first")
            return ("X", "O")
        elif marker == "O":
            print(marker[0], "will turn first")
            return ("O", "X")
        
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


def turn(player_choise):
    turn_number = 0
    while " " in field:
        try:
            marker_allocation = int(input('Enter your field position 1-9: '))
            if field[marker_allocation] == " ":
                field[marker_allocation] = player_choise[turn_number%2] # define who turn now O or X
                if victory_check(field, field[marker_allocation]) == True:
                    print(field[marker_allocation], "WINNER!!!")
                    break
                print('debug: ', victory_check(field, field[marker_allocation]))
                print("Next player", field[marker_allocation]) # Move to game field
                print(field[0] + field[1] + field[2]) # Move to game field
                print(field[3] + field[4] + field[5]) # Move to game field
                print(field[6] + field[7] + field[8]) # Move to game field
                turn_number += 1
        except ValueError and IndexError:
            print("Enter your field position please!")



def game_field():
    pass

def another_game():
    pass
#MAIN GAME

turn(("O", "X"))

'''
while start_game() == True:
    players = side_choice()
    while victory_check(field, players[0]) == False or victory_check(field, players[1]) == False:
        turn(players)
'''