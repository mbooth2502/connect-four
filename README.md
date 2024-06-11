# connect-four

# Cover Note
For the implementation of my Connect Four game, I chose to use Python as my sole programming language.
Python is a language I have vast experience with, particularly when operating with data structures. I recognized the oppurtuinity to utilize arrays in order to format a grid representation of the original game. By using lists to represent columns and arrays to organize them into a grid, I could easily add and remove elements (pieces) from any column, fascilitating smooth column insertions.

Python's array manipulation capabilities allowed me to perform dynamic checks for winning rows in any direction. Using nested loops and array slicing techniques, I could iterate over the grid and examine consecutive elements to determine if they formed a winning row horizontally, vertically, or diagonally.


# Game Choices
In this command line representation of Connect Four, pieces placed in the grid are represented as 1's or 2's, depending on the player's turn. Empty spaces in the grid are represented as 0's (every space when the game is initialised). The use of integers here instead of characters (R and Y) removed the possibility of any type clashes within my code. In a graphical representation of my code, I would have stuck to the typical colours.

To keep games to a reasonable size/complexity, I set limitations for both the grid size (rows and columns) and the winning length. The minimum grid size is equivalent to the maximum winning row length to ensure all games can be won successfully.

Throughout the game there are several prompts to ensure these requirements are made known to the player, allowing for a smooth game playing experience.


# Tests
- Create table too small/large
- Set a winning length too small/large
- Place a piece in an invalid integer column (lower or greater than limit)
- Place a piece in an (invalid) character column


# (Optional section)
Given more time, I would have explored using Pygame to transition my Connect Four game from a command-line interface to a graphical user interface (GUI). Pygame is a popular library for creating applications in Python, offering features for handling graphics and user inputs.

By leveraging Pygame, I would have created a more visually appealing representation of the Connect Four game board, allowing players to make their moves by clicking on the desired column. I could have also taken mouse-driven inputs to show the player's movements above columns when making their decisions.

As mentioned, pieces would have been represnted in their correct colourways to greater distinguish the players.


# Instructions
This game is entirely command-line based and can be ran from the main game file ('connect_four_game.py'), which utilizes various methods from 'game_logic.py'. 

To run 'connect_four_game.py' in VS Code either:
- Ctrl + F5
- (type in the terminal): py connect_four_game.py


Enter row count, column count, winning length.
Then play.
