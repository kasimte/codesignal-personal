def firstNotRepeatingCharacter(s):
    '''
    Find and return the first not repeating character in a string.

    If none exists, return "_"
    '''

    # 1. Keep a hash of the counts and an order of unique elements.
    # 2. Then iterate through the string to collect the data.
    # 3. Finally, iterate through the order and return the first
    # element with a count greater than one.

    # 1
    counts = {}
    order = []

    # 2
    for c in s:
        if c in counts:
            counts[c] += 1
        else:
            order.append(c)
            counts[c] = 1

    # 3
    for c in order:
        if counts[c] == 1:
            return c

    return "_"



s = "abacabad"
result = firstNotRepeatingCharacter(s)
print(result)
