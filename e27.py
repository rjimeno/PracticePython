#!/usr/bin/env python3

def display(board):
    print("")
    print("-------------")
    for r in range(0, len(board)):
        print("| " + board[r][0] + " | " + board[r][1] + " | " + board[r][2] + " |")
        print("-------------")
    print("")

D = " XO" # D is an array of char (that should be constant).
 
PLAYERS=(1, 2)

game = [[" ", " ", " "],
	[" ", " ", " "],
	[" ", " ", " "]]

available_moves = 9 
player = 1
while 0 < available_moves:
    try:
        i = input("Where do you want to put your {} Player {}?\nValues for either can be 1, 2 or 3 only. <row>, <column>: ".format(D[player], player))
        row = int(i[0].strip()) - 1
        column = int(i[-1].strip()) - 1
        assert(0 <= row <= 2 and 0 <= column <= 2) # Would trigger "index out of range" exception.
    except:
        print("")
        print("There was a problem with the values you gave me.")
        print("")
        continue
    if D[1] != game[row][column] and D[2] != game[row][column]:
        game[row][column] = D[player]
        available_moves -= 1
    else:
        print("")
        print("Row {}, column {} has already been used. you will have to select a different one!".format(row + 1, column + 1))
        print("")
        display(game)
        print("")
        continue
    display(game)
    if 1 == player:
        player = 2
    else:
        player = 1
