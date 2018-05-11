#!/usr/bin/env python3

def fourOfAkind(a, B):
    if a == B[0]:
        if a == B[1]:
            if a == B[2]:
                return True

def playerWinsOnBoard(a, b):
    if (fourOfAkind(a,b[0]) or
        fourOfAkind(a,b[1]) or
        fourOfAkind(a,b[2]) or
        fourOfAkind(a,[b[0][0], b[1][0], b[2][0]]) or
        fourOfAkind(a,[b[0][1], b[1][1], b[2][1]]) or
        fourOfAkind(a,[b[0][2], b[1][2], b[2][2]]) or
        fourOfAkind(a,[b[0][0], b[1][1], b[2][2]]) or
        fourOfAkind(a,[b[0][2], b[1][1], b[2][0]])
        ):
        return True
    return False

def winnerOfBoardIs(board):
    # Board is a 3-list of 3-lists where items can be either the integers 0, 1 or 2.
    if playerWinsOnBoard(2, board):
        print("Player two wins!")
    elif playerWinsOnBoard(1, board):
        print("Player one wins!")
    else:
        print("No player wins!")

winner_is_2 = [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]
winnerOfBoardIs(winner_is_2)

winner_is_1 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]
winnerOfBoardIs(winner_is_1)

winner_is_also_1 = [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]
winnerOfBoardIs(winner_is_also_1)

no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]
winnerOfBoardIs(no_winner)

also_no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]
winnerOfBoardIs(also_no_winner)
