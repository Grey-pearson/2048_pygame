import random

"""
start game - to initiolize
add new 2 - add two to board
move right - need function to search full board and check if tile with value of 2+ just +1 in arr
    and clear old tile to be 0
move left - reverse function to create duplicate board but in reverse and then run move right,
    then flip copy flipped values to og board in correct order somehow
move up - check if arr -1 (above it) has same int tile and increasing the value while resetting first 
    arrs tile
move down - use reverse arr function to flip board, do move up function and then flip it back 

need function to print board as a block instead in one line, idk how lolz, 
maybe loop printing each line?
"""

size = 4


# inizilize game and create board
def start_game():
    board = []
    for i in range(size):
        board.append([0] * size)

    for i in range(9):
        add_2(board)


"""
    for row in board:
        for tile in row:
            print(row)"""


# prints board in a square instead of as a single line
def print_game(board):
    for tile in board:
        print(tile)


# adds 2 tile to a random free tile
def add_2(board):

    r = random.randint(0, size - 1)
    c = random.randint(0, size - 1)

    while board[r][c] != 0:
        r = random.randint(0, size - 1)
        c = random.randint(0, size - 1)

    board[r][c] = 2


# condense_right to move all 2+ tiles right and compare each right neighbor to see if they can combine
def condense_right(board):
    print("right")


# def move_right() # to move all tiles right


start_game()
