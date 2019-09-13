# Milestone Project 1

#import clear display function

# Player choice
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
   string_1 = {'S1_С1':'_', 'S1_С2':'_', 'S1_С3':'_'}
   string_2 = {'S2_С1':'_', 'S2_С2':'_', 'S2_С3':'_'}
   string_3 = {'S3_С1':'_', 'S3_С2':'_', 'S3_С3':'_'}

   print(string_1.values())
   print(string_2.values())
   print(string_3.values())

display_board()
