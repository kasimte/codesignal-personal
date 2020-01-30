def firstDuplicate(a):
    counts = {}
    for c in a:
        if c in counts:
            return c
        counts[c] = 1
    return -1

# a = [2, 1, 3, 5, 3, 2]
