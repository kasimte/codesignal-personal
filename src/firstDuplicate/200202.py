def firstDuplicate(a):
    '''
    Return the first duplicate or -1 if it doesn't exist.
    '''
    # establish history
    # iterate over array and store unique history
    # if a duplicate is found, return that

    history = []

    for num in a:
        if num not in history:
            history.append(num)
        else:
            return num
    return -1
    
# a = [2, 1, 3, 5, 3, 2]
