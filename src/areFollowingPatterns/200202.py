def convertArray(array):
    hash = {}
    for i, a in enumerate(array):
        if a not in hash:
            hash[a] = i
    return [hash[a] for a in array]


def areFollowingPatterns(strings, patterns):
    '''Given an array strings, determine whether it follows the sequence
given in the patterns array. In other words, there should be no i and
j for which strings[i] = strings[j] and patterns[i] ≠ patterns[j] or
for which strings[i] ≠ strings[j] and patterns[i] = patterns[j].
    '''

    # convert array to numbers
    return convertArray(strings) == convertArray(patterns)

# testing
strings = ["cat", "dog", "dog"]
patterns = ["a", "b", "b"]
print(areFollowingPatterns(strings, patterns)) # true


strings = ["cat", "dog", "doggy"]
patterns = ["a", "b", "b"]
print(areFollowingPatterns(strings, patterns)) # false
