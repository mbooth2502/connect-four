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

    # Check for diagonal win (top-left to bottom-right)
    for i in range(len(grid) - winning_length + 1):
        for j in range(len(grid[0]) - winning_length + 1):
            if all(grid[i+k][j+k] == player for k in range(winning_length)):
                return True

    # Check for diagonal win (top-right to bottom-left)
    for i in range(len(grid) - winning_length + 1):
        for j in range(winning_length-1, len(grid[0])):
            if all(grid[i+k][j-k] == player for k in range(winning_length)):
                return True

    return False
