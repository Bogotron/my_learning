field = [" ", " ", " ", " ", " ", " ", " ", " ", " ",]
turn_number = 1
win = False

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

def turn(field, marker, turn_number):
    field_cell = None
    if " " in field:
        while field_cell not in range(0,9,1):
            field_cell = int(input('Enter your field position 1-9: ')) - 1
            field[field_cell] = marker[turn_number%2]

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


while turn_number != 10 or win == True:
    turn(field, ("O", "X"), turn_number)
    if victory_check(field, 'X') == True:
        win = True
        print('X IS WINNER!!!')
        break
    print(field)
    print(turn_number)
    print(win)
    turn_number += 1

#MAIN GAME

'''
def turn(player_choise):
    turn_number = 0
    win = None
    while " " in field:
        try:
            marker_allocation = int(input('Enter your field position 1-9: ')) - 1
            if field[marker_allocation] == " ":
                field[marker_allocation] = player_choise[turn_number%2] # define who turn now O or X
                if victory_check(field, field[marker_allocation]) == True:
                    print(field[marker_allocation], "WINNER!!!")
                    win = True
                    break
                print('debug: ', victory_check(field, field[marker_allocation]))
                print("Next player", field[marker_allocation]) # Move to game field
                print(field[0] + field[1] + field[2]) # Move to game field
                print(field[3] + field[4] + field[5]) # Move to game field
                print(field[6] + field[7] + field[8]) # Move to game field
                turn_number += 1
        except ValueError and IndexError:
            print("Enter your field position please!")
'''