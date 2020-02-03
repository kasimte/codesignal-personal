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

    '''Approach:

    Iterate through the columns and push on the arrays to the newly
    rotated image.

    So in the above, create the first array in the result [7, 4, 1],
    by iterating through the first column of the input. Continue to
    build the result.
    '''

    retval = []

    for col in range(3):
        temp = []
        for row in a:
            temp.insert(0, row[col])
        retval.append(temp)

    return retval

# testing

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

print(rotateImage(a))
