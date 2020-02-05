def numericalArray(array):
    hash = {}
    value = 1
    for string in array:
        if string not in hash:
            hash[string] = value
            value += 1
    array = [hash[string] for string in array]
    return array

def areFollowingPatterns(strings, patterns):
    '''Given an array strings, determine whether it follows the sequence
given in the patterns array. In other words, there should be no i and
j for which strings[i] = strings[j] and patterns[i] ≠ patterns[j] or
for which strings[i] ≠ strings[j] and patterns[i] = patterns[j].
    '''
        
    return numericalArray(strings) == numericalArray(patterns)
    
# testing
strings = ["cat", "dog", "dog"]
patterns = ["a", "b", "b"]
print(areFollowingPatterns(strings, patterns)) # true

strings = ["cat", "dog", "doggy"]
patterns = ["a", "b", "b"] # should be ["a", "b", "c"] to match
print(areFollowingPatterns(strings, patterns)) # false

strings = ["dog", "cat", "dog"]
patterns = ["b", "a", "b"]
print(areFollowingPatterns(strings, patterns)) # true


