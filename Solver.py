

input1 = input()
puzzle2 = [[],[],[],[],[],[],[],[],[]]
rowcount = 0
for i in input1:
    puzzle2[rowcount].append(int(i))
    if len(puzzle2[rowcount]) >= 9:
        rowcount += 1




puzzle1 = [[0, 0, 2,    7, 0, 9,    3, 8, 0],
           [4, 0, 0,    0, 0, 0,    0, 2, 0],
           [0, 0, 0,    0, 0, 1,    0, 0, 0],

           [0, 0, 0,    0, 8, 0,    0, 0, 0],
           [0, 0, 4,    3, 0, 2,    9, 0, 0],
           [0, 5, 0,    0, 0, 0,    0, 0, 6],

           [6, 0, 0,    8, 0, 7,    0, 0, 9],
           [0, 0, 0,    0, 4, 0,    8, 0, 0],
           [0, 0, 7,    0, 1, 0,    0, 0, 0]]


puzzle_def = [[0, 0, 0,    0, 0, 0,    0, 0, 0],
           [0, 0, 0,    0, 0, 0,    0, 0, 0],
           [0, 0, 0,    0, 0, 0,    0, 0, 0],

           [0, 0, 0,    0, 0, 0,    0, 0, 0],
           [0, 0, 0,    0, 0, 0,    0, 0, 0],
           [0, 0, 0,    0, 0, 0,    0, 0, 0],

           [0, 0, 0,    0, 0, 0,    0, 0, 0],
           [0, 0, 0,    0, 0, 0,    0, 0, 0],
           [0, 0, 0,    0, 0, 0,    0, 0, 0]]

def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == 0:
                return r, c
    return None, None


def is_valid(puzzle, guess, row, col):

    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    row_start = (row//3) * 3
    col_start = (col//3) * 3
    for r in range(row_start, row_start+3):
        for c in range(col_start, col_start+3):
            if puzzle[r][c] == guess:
                return False

    return True


def solve_sudoku(puzzle):
    row, col = find_next_empty(puzzle)

    if row is None:
        return True

    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess

            if solve_sudoku(puzzle):
                return True
        puzzle[row][col] = 0
    return False


print(solve_sudoku(puzzle2))
for i in range(9): 
    print(puzzle2[i])
