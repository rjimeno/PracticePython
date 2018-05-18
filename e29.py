#!/usr/bin/env python3

"""
Tic Tac Toe Game http://www.practicepython.org/exercise/2016/08/03/29-tic-tac-toe-game.html
"""

def four_of_a_kind(obj, objs):
    "True only if the obj is the same as all 3 elements of objs."
    if obj == objs[0]:
        if obj == objs[1]:
            if obj == objs[2]:
                return True
    return False

# This could be nicely improved by checking only the row, column and diagonal that just changed.
def player_wins_on_board(obj, objs):
    "True only of the board configuration grants at least one winner."
    if (four_of_a_kind(obj, objs[0]) or
            four_of_a_kind(obj, objs[1]) or
            four_of_a_kind(obj, objs[2]) or
            four_of_a_kind(obj, [objs[0][0], objs[1][0], objs[2][0]]) or
            four_of_a_kind(obj, [objs[0][1], objs[1][1], objs[2][1]]) or
            four_of_a_kind(obj, [objs[0][2], objs[1][2], objs[2][2]]) or
            four_of_a_kind(obj, [objs[0][0], objs[1][1], objs[2][2]]) or
            four_of_a_kind(obj, [objs[0][2], objs[1][1], objs[2][0]])
       ):
        return True
    return False

def display(board):
    "Produces a visual representation for the board."
    print("")
    print("-------------")
    for row in board:
        print("| " + row[0] + " | " + row[1] + " | " + row[2] + " |")
        print("-------------")
    print("")

D = " XO" # D is an array of char (that should be constant).

def main():
    "Solution to exercise 29."
    available_moves = 9
    player = 1
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    while 0 < available_moves:
        try:
            i = input(
                'Where do you want to put your {} Player {}?\nValues for either'
                'can be 1, 2 or 3 only. <row>, <column>: '.format(D[player], player)
            )
            row = int(i[0].strip()) - 1
            column = int(i[-1].strip()) - 1
            assert(
                0 <= row <= 2 and 0 <= column <= 2
            )
        except (ValueError, AssertionError):
            print("")
            print("There was a problem with the values you gave me.")
            print("")
            continue
        if D[1] != board[row][column] and D[2] != board[row][column]:
            board[row][column] = D[player]
            available_moves -= 1
        else:
            print("")
            print(
                "Row {}, column {} has already been used. you will have"
                "to select a different one!".format(row + 1, column + 1)
            )
            print("")
            display(board)
            print("")
            continue
        display(board)
        if player_wins_on_board(D[1], board):
            print("Player one wins!")
            break
        elif player_wins_on_board(D[2], board):
            print("Player two wins!")
            break
        else:
            pass
        if 1 == player:
            player = 2
        else:
            player = 1

if "__main__" == __name__:
    main()
