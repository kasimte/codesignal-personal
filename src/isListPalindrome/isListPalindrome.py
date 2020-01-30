# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def isListPalindrome(l):
    '''Returns true if linked list l contains a palindrome
    
    Approach:
    
    1. Convert to array
    2. Use array palindrome reverse check
    '''
    
    
    array = []
    
    while l != None:
        array.append(l.value)
        l = l.next
        
    return array == array[::-1]

# Notes:
#
# I thought calling array.reverse would work, but apparently that
# reverses the array in place:
#
# array.reverse()
# Reverse the order of the items in the array.
