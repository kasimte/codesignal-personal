# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l, k):
    '''
    Given a singly linked list of integers l and an integer k, remove
    all elements from list l that have a value equal to k.
    '''

    '''
    Approach:
    1. Check edge case if list is completely empty.
    2. Check edge case for list starting with integer to be removed.
    3. Iterate through the list and skip nodes that equal k
    '''

    # 1
    if l == None: return None

    # 2
    while l.value == k:
        if l.next != None:
            l = l.next
        else:
            return None

    # 3
    thisNode = l
    nextNode = l.next
    
    while nextNode != None:
        if nextNode.value == k:
            thisNode.next = nextNode.next
            nextNode = thisNode.next
        else:
            thisNode = nextNode
            nextNode = nextNode.next
    return l

