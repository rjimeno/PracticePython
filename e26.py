#!/usr/bin/env python3

def all_the_same(pid: int, line: list[int]) -> bool:
    """ Returns True if all the elements in list B have value a. """
    return all(pid == line[i] for i in [0, 1, 2])

def player_wins_on_board(pid: int, b: list[list[int]]) -> bool:
    """ Returns true if the board if the board is in a winning configuration
    for the player with 'pid' Returns false if no winner can be chosen (yet)."""
    if (any(all_the_same(pid,b[i]) for i in [0, 1, 2]) or
        any(all_the_same(pid,[b[0][i], b[1][i], b[2][i]]) for i in [0, 1, 2]) or
        all_the_same(pid,[b[0][0], b[1][1], b[2][2]]) or
        all_the_same(pid,[b[0][2], b[1][1], b[2][0]])
        ):
        return True
    return False

def winner_of_board_is(board: list[list[int]]):
    """ Board is a 3-list of 3-lists where items can be
    either the integers 0, 1 or 2."""
    if player_wins_on_board(2, board):
        print("Player two wins!")
    elif player_wins_on_board(1, board):
        print("Player one wins!")
    else:
        print("No player wins!")

winner_is_2 = [
    [2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]
winner_of_board_is(winner_is_2)

winner_is_1 = [
    [1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]
winner_of_board_is(winner_is_1)

winner_is_also_1 = [
    [0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]
winner_of_board_is(winner_is_also_1)

no_winner = [
    [1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]
winner_of_board_is(no_winner)

also_no_winner = [
    [1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]
winner_of_board_is(also_no_winner)
