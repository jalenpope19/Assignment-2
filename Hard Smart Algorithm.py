import time

assignments = 0
start_time = None

def solve(bo):
    global assignments
    global start_time

    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            assignments += 1

            if solve(bo):
                return True

            bo[row][col] = 0

    return False

def valid(bo, num, pos):
    # Check the row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check the column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check the box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

def find_empty(bo):
    min_legal_values = 10  # Initialize with a value greater than maximum possible legal values
    min_legal_pos = None

    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                legal_values = get_legal_values(bo, i, j)
                if len(legal_values) < min_legal_values:
                    min_legal_values = len(legal_values)
                    min_legal_pos = (i, j)

    return min_legal_pos

def get_legal_values(bo, row, col):
    legal_values = set(range(1, 10))
    
    for i in range(9):
        legal_values.discard(bo[row][i])
        legal_values.discard(bo[i][col])

    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            legal_values.discard(bo[i][j])

    return legal_values

# Sudoku board
board = [[7, 0, 0, 0, 0, 0, 0, 0, 0],
    [6, 0, 0, 4, 1, 0, 2, 5, 0],
    [0, 1, 3, 0, 9, 5, 0, 0, 0],
    [8, 6, 0, 0, 0, 0, 0, 0, 0],
    [3, 0, 1, 0, 0, 0, 4, 0, 5],
    [0, 0, 0, 0, 0, 0, 0, 8, 6],
    [0, 0, 0, 8, 4, 0, 5, 3, 0],
    [0, 4, 2, 0, 3, 6, 0, 0, 7],
    [0, 0, 0, 0, 0, 0, 0, 0, 9]]

# Display the original Sudoku board
print_board(board)

# Start running time
start_time = time.time()

# Solve the puzzle
solve(board)

# Calculate running time
end_time = time.time()
running_time = end_time - start_time

# Display results
print("_________________________")
print_board(board)
print("Total assignments:", assignments)
print("Running time:", running_time, "seconds")
