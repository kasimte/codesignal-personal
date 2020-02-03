'''https://app.codesignal.com/interview-practice/task/6rE3maCQwrZS3Mm2H

Note: Your solution should have O(l1.length + l2.length) time
complexity, since this is what you will be asked to accomplish in an
interview.

Given two singly linked lists sorted in non-decreasing order, your
task is to merge them. In other words, return a singly linked list,
also sorted in non-decreasing order, that contains the elements from
both original lists.

Example

For l1 = [1, 2, 3] and l2 = [4, 5, 6], the output should be
mergeTwoLinkedLists(l1, l2) = [1, 2, 3, 4, 5, 6];
For l1 = [1, 1, 2, 4] and l2 = [0, 3, 5], the output should be
mergeTwoLinkedLists(l1, l2) = [0, 1, 1, 2, 3, 4, 5].
Input/Output

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer l1

A singly linked list of integers.

Guaranteed constraints:
0 ≤ list size ≤ 104,
-109 ≤ element value ≤ 109.

[input] linkedlist.integer l2

A singly linked list of integers.

Guaranteed constraints:
0 ≤ list size ≤ 104,
-109 ≤ element value ≤ 109.

[output] linkedlist.integer

A list that contains elements from both l1 and l2, sorted in non-decreasing order.

'''

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

def mergeTwoLinkedLists(l1, l2):
    '''Given two singly linked lists sorted in non-decreasing order, your
    task is to merge them. In other words, return a singly linked
    list, also sorted in non-decreasing order, that contains the
    elements from both original lists.
    '''

    '''
    Approach:
    '''

    if l1 == None:
        return l2
    if l2 == None:
        return l1

    # start is a pointer so we can easily return at the end
    start = ListNode(None)

    # declare current to track the new list through the traverse
    current = start

    while l1 != None and l2 != None:
        if (l1.value < l2.value):
            # link up the lowest of the next two values
            current.next = l1
            # move current forward
            current = current.next

            if l1.next == None:
                current.next = l2
                break
            l1 = l1.next
        else:
            # mirrored code for the other list
            current.next = l2
            current = current.next

            if l2.next == None:
                current.next = l1
                break
            l2 = l2.next
    return start.next

# Testing

# For l1 = [1, 1, 2, 4] and l2 = [0, 3, 5], the output should be
# mergeTwoLinkedLists(l1, l2) = [0, 1, 1, 2, 3, 4, 5].
