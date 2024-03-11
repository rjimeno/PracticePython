#!/usr/bin/env python3

def display(board):
    print("")
    print("-------------")
    for b in board:
        print("| " + b[0] + " | " + b[1] + " | " + b[2] + " |")
        print("-------------")
    print("")

def main():
    game = [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]

    available_moves = 9 
    player = 1
    while 0 < available_moves:
        try:
            i = input(f"Where do you want to put your {D[player]} Player {player}?"
                    "\nValues for either can be 1, 2 or 3 only. <row>, <column>: ")
            row = int(i[0].strip()) - 1
            column = int(i[-1].strip()) - 1
            assert 0 <= row <= 2 and 0 <= column <= 2 # Would trigger "index out of range" exception.
        except (ValueError, IndexError, AssertionError):
            print("")
            print("Please check your input. There was a problem with the values you gave me.")
            print("")
            continue
        if D[1] != game[row][column] and D[2] != game[row][column]:
            game[row][column] = D[player]
            available_moves -= 1
        else:
            print("")
            print(f"Row {row + 1}, column {column + 1} has already been used. you will have to select a different one!")
            print("")
            display(game)
            print("")
            continue
        display(game)
        if 1 == player:
            player = 2
        else:
            player = 1

D = " XO" # D is an array of char (that should be constant).
PLAYERS=(1, 2)
if __name__ == "__main__":
    main()