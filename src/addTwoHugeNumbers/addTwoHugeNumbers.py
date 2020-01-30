# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def arrayFrom(l):
    '''Returns array of integers from a linked list'''
    array = []
    while l != None:
        array.append(int(l.value))
        l = l.next
    return array

def addTwoHugeNumbers(a, b):
    '''Adds two huge numbers which are contained in two linked lists

    Approach:
    1. Convert everything to arrays for easy processing
    2. Summation via iteration through the arrays.
    3. Conversion back to linked list for return
    '''
    
    # 1
    a_array = arrayFrom(a)[::-1] # reverse the arrays for easy processing
    b_array = arrayFrom(b)[::-1]
    
    max_length = max([len(a_array), len(b_array)])
    
    result = []
    carry = 0

    # 2
    for i in range(max_length):
        a_value = 0
        b_value = 0

        # look before you leap
        # https://docs.python.org/3/glossary.html#term-lbyl
        if i < len(a_array):
            a_value = a_array[i]
        if i < len(b_array):
            b_value = b_array[i]

        sum = a_value + b_value + carry
        if sum < 10000:
            carry = 0
            result.insert(0, sum)
        else:
            result.insert(0, sum - 10000)
            # I initially got mixed up here, thinking the carry was
            # sum - 10000, but actually it has to truncate the last 4
            # digits.
            carry = int(sum/10000)

    if carry > 0:
        result.insert(0, carry)

    # 3
    #
    # This whole third portion is just converting result back into a
    # linked list and could be processed into a helper function.
    if len(result) > 0:
        list = ListNode(result[0])
    else:
        return None
    
    previousNode = list
    for r in range(1, len(result)):
        node = ListNode(result[r])
        previousNode.next = node
        previousNode = node
        
    return list
