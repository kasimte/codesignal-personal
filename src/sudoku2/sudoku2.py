# Inspired and adapted from
# https://github.com/dvitsios/codesignal-my-solutions/blob/master/Sudoku2/sudoku2.py

def row_is_valid(row):
    '''Returns true if row is valid'''
    valid = True
    counts = {}
    
    # loop over array, store counts
    if len(row) < 2:
        return True

    for i in row:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1

    # if max count is above 1, then return false
    if counts[max(counts, key=counts.get)] > 1:
        valid = False

    return valid


def rows_are_valid(grid):
    '''Iterates over rows and checks if each is valid'''
    valid = True

    for row in grid:
        if not row_is_valid([int(x) for x in row if x != "."]):
            valid = False
            break

    # print(valid)
    return valid

def sudoku2(grid):
    rows_valid = rows_are_valid(grid)
    columns_valid = rows_are_valid(list(zip(*grid)))
    box_valid = True

    # outer loop
    for i in range(0,9,3):
        # Take three rows
        sub_matrix = grid[i:i+3]
        for j in range(0,9,3):
            # take the lines for each 3x3 matrix
            temp = [sub_matrix[x][j:j+3] for x in range(3)]
            # unpack and filter
            temp = [int(temp[l][k]) for l in range(3) for k in range(3) if temp[l][k] != "."]
            # check for validity
            if not row_is_valid(temp):
                box_valid = False
                break

    return (rows_valid and columns_valid and box_valid)

# Testing
#

# row = [1,2,3]
# row2 = [0,3,3]
# print(row_is_valid(row))
# print(rows_are_valid([row, row2]))

# grid = [[".",".",".",".","2",".",".","9","."], 
#  [".",".",".",".","6",".",".",".","."], 
#  ["7","1",".",".","7","5",".",".","."], 
#  [".","7",".",".",".",".",".",".","."], 
#  [".",".",".",".","8","3",".",".","."], 
#  [".",".","8",".",".","7",".","6","."], 
#  [".",".",".",".",".","2",".",".","."], 
#  [".","1",".","2",".",".",".",".","."], 
#  [".","2",".",".","3",".",".",".","."]]

# print(sudoku2(
# [[".",".",".",".",".",".",".",".","2"], 
#  [".",".",".",".",".",".","6",".","."], 
#  [".",".","1","4",".",".","8",".","."], 
#  [".",".",".",".",".",".",".",".","."], 
#  [".",".",".",".",".",".",".",".","."], 
#  [".",".",".",".","3",".",".",".","."], 
#  ["5",".","8","6",".",".",".",".","."], 
#  [".","9",".",".",".",".","4",".","."], 
#  [".",".",".",".","5",".",".",".","."]]))

# print(rows_are_valid(grid))
