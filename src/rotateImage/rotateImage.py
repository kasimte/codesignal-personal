# https://app.codesignal.com/interview-practice/task/5A8jwLGcEpTPyyjTB

# Note: Try to solve this task in-place (with O(1) additional memory),
# since this is what you'll be asked to do during an interview.

# You are given an n x n 2D matrix that represents an image. Rotate
# the image by 90 degrees (clockwise).


def rotateImage(a):
    '''
    Rotate an image, represented as a square matrix, clockwise.
    '''

    # Input:
    # a = [[1, 2, 3],
    #      [4, 5, 6],
    #      [7, 8, 9]]

    # Output:
    # rotateImage(a) =
    # [[7, 4, 1],
    #  [8, 5, 2],
    #  [9, 6, 3]]

    # Approach (Naive):
    # 1. Create blank result array.
    # 2. Loop through columns and for each column create a new array
    # 3. Append the array to the new matrix

    # 1
    result = []
    length = len(a)

    # 2
    for column_index in range(length):
        new_row = []
        for row_index in range(length):
            # insert element in new row
            new_row.insert(0, a[row_index][column_index])
        result.append(new_row)

    return result

# testing

# a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]

# print(rotateImage(a))
