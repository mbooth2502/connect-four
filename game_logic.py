# Game Logic
# Mason Booth 2024/06/11


# grid size limits
GRID_MIN = 5
GRID_MAX = 10

# winning row limits
WINNING_MIN = 2
WINNING_MAX = 5


# check users config. parameters meet pre-limits
# returns true if all values within limits
# returns false with an error message, otherwise
def is_valid_config(row_count, column_count, winning_length):
    # Check grid size is greater than min but lower than max
    if (row_count < GRID_MIN or row_count > GRID_MAX or
        column_count < GRID_MIN or column_count > GRID_MAX):
        print(f"Grid size must be between {GRID_MIN}x{GRID_MIN} and {GRID_MAX}x{GRID_MAX}. Please try again.")
        return False
    
    # check winning length is greater than min but lower than max
    if winning_length < WINNING_MIN or winning_length > WINNING_MAX:
        print(f"Winning row length must be between {WINNING_MIN} and {WINNING_MAX}. Please try again.")
        return False
    
    return True


# method to check if a player has won after each move
# returns false unless player has a row of winning_length in ANY direction
def check_win(grid, player, winning_length):
    # Check for horizontal win
    for row in grid:
        for i in range(len(row) - winning_length + 1):
            if all(cell == player for cell in row[i:i+winning_length]):
                return True

    # Check for vertical win
    for col in range(len(grid[0])):
        for i in range(len(grid) - winning_length + 1):
            if all(grid[i+k][col] == player for k in range(winning_length)):
                return True

    # Check for diagonal win (top left to bottom right)
    for i in range(len(grid) - winning_length + 1):
        for j in range(len(grid[0]) - winning_length + 1):
            if all(grid[i+k][j+k] == player for k in range(winning_length)):
                return True

    # Check for diagonal win (top right to bottom left)
    for i in range(len(grid) - winning_length + 1):
        for j in range(winning_length-1, len(grid[0])):
            if all(grid[i+k][j-k] == player for k in range(winning_length)):
                return True

    return False
