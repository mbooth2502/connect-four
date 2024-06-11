
import numpy as np 

# size of the grid 
ROW_COUNT = 0 
COLUMN_COUNT = 0 

# length of row needed to win game 
WINNING_LENGTH = 0 


# allow player(s) to configure game's: 
# - grid size 
# - winning row length 
def configure_game(): 

    global ROW_COUNT, COLUMN_COUNT, WINNING_LENGTH  

    # take player's inputs
    ROW_COUNT = int(input("Enter the number of rows for the grid: ")) 
    COLUMN_COUNT = int(input("Enter the number of columns for the grid: ")) 

    WINNING_LENGTH = int(input("Enter the winning length for a row: ")) 

    return ROW_COUNT, COLUMN_COUNT, WINNING_LENGTH 


# create initial grid based on size parameters 
# initialise with 0's 
def create_grid(row_count, column_count): 
    board = []

    # Add rows with column_count of zeros
    for _ in range(row_count):
        row = [0] * column_count
        board.append(row)

    return board 


# method to show current board state after each turn
def print_board(board):
    # print row by row to keep board's structure
    for row in board:
        print(row)


# initialise a new game grid 
# cases: first game, game over, game restarted 
def initialise_new_game():   

    # initialize with player's chosen parameters
    row_count, column_count, winning_length = configure_game() 
    grid = create_grid(row_count, column_count) 

    return grid, winning_length 




# main game loop
if __name__ == "__main__": 

    grid, winning_length = initialise_new_game() 
    print_board(grid) 

 
 