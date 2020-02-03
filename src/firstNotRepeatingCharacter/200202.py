def firstNotRepeatingCharacter(s):
    '''Fill in code here.'''

    order = []
    counts = {}
    
    # iterate over the string
    for c in s:
        if c not in counts:
            counts[c] = 1
            order.append(c)            
        else:
            counts[c] += 1

    for c in order:
        if counts[c] == 1:
            return c

    return "_"

print(firstNotRepeatingCharacter("abacabad")) # c
print(firstNotRepeatingCharacter("abacabadc")) # d
print(firstNotRepeatingCharacter("dabacabadc")) # _
