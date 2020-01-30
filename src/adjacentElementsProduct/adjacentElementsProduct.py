def adjacentElementsProduct(inputArray):
    '''Returns the max product of adjacent elements from an array

    Approach:

    1. Default the max to the first product.
    2. Iterate through all other possibilities, checking for a higher product.
    '''

    # 1
    max = inputArray[0] * inputArray[1]

    # 2
    for i in range(len(inputArray)-1):
        product = inputArray[i] * inputArray[i+1]
        if product > max:
            max = product

    return max
