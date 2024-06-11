
import numpy as np 

# size of the grid 
ROW_COUNT = 0 
COLUMN_COUNT = 0 
# grid size limits
GRID_MIN = 5
GRID_MAX = 10

# length of row needed to win game 
WINNING_LENGTH = 0
# winning row limits
WINNING_MIN = 2
WINNING_MAX = 5


# min and max config. sizes for user
def initial_message():
    print("\nGrid Size Limits")
    print("Minimum Size: 5x5, Maximum Size: 10x10")
    print("\nWinning Length Limits")
    print("Minimum Length: 2, Maximum Length: 5\n")



# allow player(s) to configure game's: 
# - grid size 
# - winning row length 
def configure_game(): 
    global ROW_COUNT, COLUMN_COUNT, WINNING_LENGTH  

    while True:
        # Take player's inputs
        ROW_COUNT = int(input("Enter the number of rows for the grid: ")) 
        COLUMN_COUNT = int(input("Enter the number of columns for the grid: ")) 
        WINNING_LENGTH = int(input("Enter the winning length for a row: ")) 

        # Check if the grid size is within limits
        if ROW_COUNT < GRID_MIN or ROW_COUNT > GRID_MAX or COLUMN_COUNT < GRID_MIN or COLUMN_COUNT > GRID_MAX:
            print(f"Grid size must be between {GRID_MIN}x{GRID_MIN} and {GRID_MAX}x{GRID_MAX}. Please try again.")
            print(" ")
            continue
        
        # Check if the winning row length is within limits
        if WINNING_LENGTH < WINNING_MIN or WINNING_LENGTH > WINNING_MAX:
            print(f"Winning row length must be between {WINNING_MIN} and {WINNING_MAX}. Please try again.")
            print(" ")
            continue
        
        # If both conditions are met, break out of the loop
        break

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




# check if chosen position for piece is valid  
def is_valid_place(grid, col):  
    # returns true (valid) if col is: 
    # - between 0 and COLUMN_COUNT  
    # - has not already been selected  
    
    return col >= 0 and col < COLUMN_COUNT and grid[0][col] == 0  

 
# place a piece at given co-ordinates  
def place_piece(grid, column, row, piece):   

    grid[column][row] = piece  


# get the next open row in the column to place the piece 
def get_next_open_row(grid, col): 

    # iterate through each row to check for lowest valid row position
    # ROW_COUNT - 1 indexes the range at 0, and steps of -1 move upwards in the grid
    for r in range(ROW_COUNT-1, -1, -1): 

        if grid[r][col] == 0: 
            # returns the valid position
            return r 

    return None  # returns None if the column is full 




# main loop
if __name__ == "__main__": 

    # indicate min and max selections for user
    initial_message()

    grid, winning_length = initialise_new_game() 

    print(" ")
    print("Initial Game Grid:")
    print_board(grid) 


    # Variable to keep track of the current player (1 or 2) 
    current_player = 1 

    # Game loop 
    while True: 
        # Player selects a column to place their piece 
        print(" ")
        column_input = int(input(f"Player {current_player}, choose a column to place your piece (1-{COLUMN_COUNT}): ")) 

        # correct column_input
        column = column_input - 1


        # Check if the selected column is valid 
        if is_valid_place(grid, column): 

            # Get the next open row in the selected column 
            row = get_next_open_row(grid, column) 

            # Place the player's piece in the grid 
            place_piece(grid, row, column, current_player) 

            # Print the updated grid 
            print(" ")
            print_board(grid) 

            # Check for win condition (not implemented in this example) 

            # Switch to the next player 
            current_player = 2 if current_player == 1 else 1 
        else: 
            print("Invalid column. Please choose a valid column.") 