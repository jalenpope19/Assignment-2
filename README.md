# Assignment-2

This repository contains a Python implementation of a backtracking algorithm to solve Sudoku puzzles.

Compiling Code

Visual Studio Code is an editor that uses the Microsoft platform's compiler. It supports development operations, such as debugging, task running, and version control.

Executing Code
- Save the file after checking the code for any errors.
- Hit the run button.
- Once the script finishes execution, the original Sudoku board will be followed by the solved Sudoku board.
- The total number of assignments made during solving and the running time in seconds will show after the solved board.

IMPORTANT FACTORS OF SOLVING THE SUDOKU PUZZLES

Variables:

-Each cell in the 9x9 grid represents a variable (81 variables) because they are subject to change when trying to successfully solve the puzzle. 

Domains:

-The domain for each of the variables is a number range between 1 and 9. 

Constraints: 

-The digits in the starting configuration must remain the same.

-Each variable in a row must have a different value between 1 and 9. The variable should only appear 1 time.

-Each variable in a column must have a different value between 1 and 9. The variable should only appear 1 time.

-Each variable in the 3x3 grids within the board must have a different value between 1 and 9. The variable should only appear 1 time.
