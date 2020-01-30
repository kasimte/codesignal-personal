def hash_from(solution):
    '''Returns a hash decoder basedo on the array of arrays solution'''
    
    temp = {}
    for keyvalue in solution:
        temp[keyvalue[0]] = keyvalue[1]
    return temp

def is_valid(string):
    '''Returns true if this is a valid number string'''

    '''
    Approach:
    
    1. Return false if the length of the string is greater than 1 and the first char is "0"
    2. Return true otherwise
    '''

    # 1
    if len(string) > 1 and string[0] == "0":
        return False

    # 2
    return True

def digit_string_from(string, hash):
    '''Returns the digit string based on letter string and the hash decoder.'''
    return ''.join([hash[x] for x in string])

# hash = hashFrom(solution)
# print(hash)

def isCryptSolution(crypt, solution):
    '''Returns a boolean that says whether the solution is correct for this crypt'''

    '''
    Approach:

    1. Convert the solution into a hash.
    2. Convert the crypt array into strings of numbers based on the hash.
    3. Check if there are any prefixed zeros in the String, but a single Zero is okay.
    4. Return a boolean based on the arithmetic operation.
    '''

    # 1
    hash = hash_from(solution)

    # 2
    digit_strings = [digit_string_from(x, hash) for x in crypt]
    
    # 3
    for s in digit_strings:
        if not is_valid(s):
            return False

    integers = [int(x) for x in digit_strings]
    
    return (integers[0] + integers[1] == integers[2])


# testing

crypt = ["SEND", "MORE", "MONEY"]
solution = [['O', '0'],
            ['M', '1'],
            ['Y', '2'],
            ['E', '5'],
            ['N', '6'],
            ['D', '7'],
            ['R', '8'],
            ['S', '9']]
print(isCryptSolution(crypt, solution))
