def is_valid(array):
    '''
    Returns true if array is valid.
    Assumes array is of length 9 and "." describes empty space.
    '''
    numbers = set(array)
    numbers.remove(".")
    temp = []
    for a in array:
        if a is not ".":
            temp.append(a)
    # length of numbers should be the same as that of array with "." removed
    return len(numbers) == len(temp)

def is_valid(rows):
    print(rows)
    for r in rows:
        if is_valid(r) == False:
            return False
    return True
    
def sudoku2(grid):
    '''
    Output true or false depending on whether the board is valid or not.

    Validity requires checks on:
    - rows
    - columns
    - 3x3 grids
    '''
    rows_valid = is_valid(grid)
    return rows_valid
    # columns_valid = is_valid(list(zip(*grid)))
    # return rows_valid and columns_valid
    

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
# print(sudoku2(grid)) # false

print(sudoku2([[".",".",".",".",".",".",".",".","2"], 
 [".",".",".",".",".",".","6",".","."], 
 [".",".","1","4",".",".","8",".","."], 
 [".",".",".",".",".",".",".",".","."], 
 [".",".",".",".",".",".",".",".","."], 
 [".",".",".",".","3",".",".",".","."], 
 ["5",".","8","6",".",".",".",".","."], 
 [".","9",".",".",".",".","4",".","."], 
 [".",".",".",".","5",".",".",".","."]])) # true

# print(rows_are_valid(grid))
