'''https://app.codesignal.com/interview-practice/task/XP2Wn9pwZW6hvqH67

Note: Your solution should have O(n) time complexity, where n is the
number of elements in l, and O(1) additional space complexity, since
this is what you would be asked to accomplish in an interview.

Given a linked list l, reverse its nodes k at a time and return the
modified list. k is a positive integer that is less than or equal to
the length of l. If the number of nodes in the linked list is not a
multiple of k, then the nodes that are left out at the end should
remain as-is.

You may not alter the values in the nodes - only the nodes themselves
can be changed.

Example

For l = [1, 2, 3, 4, 5] and k = 2, the output should be
reverseNodesInKGroups(l, k) = [2, 1, 4, 3, 5];
For l = [1, 2, 3, 4, 5] and k = 1, the output should be
reverseNodesInKGroups(l, k) = [1, 2, 3, 4, 5];
For l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] and k = 3, the output should be
reverseNodesInKGroups(l, k) = [3, 2, 1, 6, 5, 4, 9, 8, 7, 10, 11].
Input/Output

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer l

A singly linked list of integers.

Guaranteed constraints:
1 ≤ list size ≤ 104,
-109 ≤ element value ≤ 109.

[input] integer k

The size of the groups of nodes that need to be reversed.

Guaranteed constraints:
1 ≤ k ≤ l size.

[output] linkedlist.integer

The initial list, with reversed groups of k elements.

'''

# This works
def reverseNodesInKGroups(l, k):
    '''Given a linked list l, reverse its nodes k at a time and return
the modified list. k is a positive integer that is less than or equal
to the length of l. If the number of nodes in the linked list is not a
multiple of k, then the nodes that are left out at the end should
remain as-is.
    '''

    '''Approach:

    1. If the list is empty, simply return it.

    2. Iterate through the list to find its length. If the list is
    shorter than k, simply return the list.

    3. Create three temporary nodes, current, previous, and next. Swap
    them in place for n iterations. At the end:

    previous: the head of the k chunk list
    current: the tail
    next: current.next

    4. Recursively call the function to return the list.
    '''

    # 1
    if not l:
        return l

    # 2
    c = l
    n = k

    # Decrease until either n is 0 or the list is empty
    while c and n:
        c = c.next
        n -= 1 

    # If the latter, return the list
    if n:
        return l

    current = l
    previous = None
    next = None
    n = k

    # 3
    while current and n:
        next = current.next
        current.next = prev
        prev = current
        current = next
        n -= 1

    # 4
    if next:
        l.next = reverseNodesInKGroups(next, k)

    return previous
