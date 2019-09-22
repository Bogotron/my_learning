field = [" ", " ", " ", " ", " ", " ", " ", " ", " ",]
turn_number = 0
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
    

def victory_check(field, marker, turn_number):
    side = marker[turn_number%2]
    return ((side == field[0] == field[1] == field [2]) or 
            (side == field[3] == field[4] == field [5]) or
            (side == field[6] == field[7] == field [8]) or
            (side == field[0] == field[3] == field [6]) or
            (side == field[1] == field[4] == field [7]) or
            (side == field[2] == field[5] == field [8]) or
            (side == field[0] == field[4] == field [8]) or
            (side == field[6] == field[4] == field [2]))

def field_printer(field):
    print("\n")
    print(field[6], field[7], field[8], sep= "|")
    print("_____")
    print(field[3], field[4], field[5], sep= "|")
    print("_____")
    print(field[0], field[1], field[2], sep= "|")


#MAIN GAME

while True:
    if start_game() == True:
        player = side_choice()
        while victory_check(field, player, turn_number) != True and turn_number < 10:
            turn(field, player, turn_number)
            field_printer(field)
            turn_number += 1
    else:
        break
    break


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