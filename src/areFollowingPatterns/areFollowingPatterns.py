def findFalse(strings, patterns):
    '''
    Checks for pattern one way.
    '''

    '''
    Approach:
    
    1. iterate through strings and store in hash string -> [indexes]
    2. for each key, check patterns and see if all the indexes match
    3. if there is a non-match, return False
    '''

    # 1
    hash = {}

    for i in range(len(strings)):
        str = strings[i]
        # look before you leap
        if str in hash:
            # append to existing array
            hash[str].append(i)
        else:
            # create new array
            hash[str] = [i]

    # 2
    keys = [x for x in list(hash)]

    for key in keys:
        indexes = hash[key]
        
        for i in indexes:
            for j in indexes:
                # 3
                if i != j and patterns[i] != patterns[j]:
                    return False

    return True

def areFollowingPatterns(strings, patterns):
    '''Given an array strings, determine whether it follows the sequence
given in the patterns array. In other words, there should be no i and
j for which strings[i] = strings[j] and patterns[i] ≠ patterns[j] or
for which strings[i] ≠ strings[j] and patterns[i] = patterns[j].
    '''

    # Check both ways
    return (findFalse(strings, patterns) and findFalse(patterns, strings))


# testing
strings = ["cat", "dog", "dog"]
patterns = ["a", "b", "b"]
print(areFollowingPatterns(strings, patterns)) # true


strings = ["cat", "dog", "doggy"]
patterns = ["a", "b", "b"]
print(areFollowingPatterns(strings, patterns)) # false
