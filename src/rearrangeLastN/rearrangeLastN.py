'''
https://app.codesignal.com/interview-practice/task/5vcioHMkhGqkaQQYt

Note: Try to solve this task in O(list size) time using O(1) additional space, since this is what you'll be asked during an interview.

Given a singly linked list of integers l and a non-negative integer n, move the last n list nodes to the beginning of the linked list.

Example

For l = [1, 2, 3, 4, 5] and n = 3, the output should be
rearrangeLastN(l, n) = [3, 4, 5, 1, 2];
For l = [1, 2, 3, 4, 5, 6, 7] and n = 1, the output should be
rearrangeLastN(l, n) = [7, 1, 2, 3, 4, 5, 6].

Input/Output

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer l

A singly linked list of integers.

Guaranteed constraints:
0 ≤ list size ≤ 105,
-1000 ≤ element value ≤ 1000.

[input] integer n

A non-negative integer.

Guaranteed constraints:
0 ≤ n ≤ list size.

[output] linkedlist.integer

Return l with the n last elements moved to the beginning.
'''


# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def rearrangeLastN(l, n):
    '''
    Given a singly linked list of integers l and a non-negative integer n, move the last n list nodes to the beginning of the linked list.
    '''
    
    '''
    Approach:

    1. Edge case: n == 0, just return the list.
    2. Establish nodes for start, end, and previous (one before start).
    3. Edge case: If n is the length of the list, return the list.
    4. Iterate through the list until we find the end, updating start, end, and previous.
    5. Clean up by setting the next node for end and previous.
    '''

    # 1
    if n == 0:
        return l

    # 2
    start = l # this will be what we return
    end = l # this will be connected to l, the original linked list, before the return
    previous = l # this tracks the node right before the start of the final list, to be disconnected
    count = 1

    while count < n:
        end = end.next
        count += 1

    # 3
    if end.next == None:
        return l

    # 4
    while end.next is not None:
        if end.next is not None:
            end = end.next
            previous = start
            start = start.next
        
    # 5
    end.next = l
    previous.next = None
    return start
    
'''
Log: Solved in 12 minutes on first try.
'''
