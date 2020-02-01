# https://app.codesignal.com/interview-practice/task/TG4tEMPnAc3PnzRCs

#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def hasPathWithGivenSum(t, s):
    '''
    Approach:

    - Tranverse through all possibilities of the tree.
    - If a match is found, then return true.
    - If not, then return false.
    '''

    tree = t
    sum = s

    if tree == None:
        return False

    left = tree.left
    right = tree.right

    if left is not None and right is not None:
        return (hasPathWithGivenSum(left, s - tree.value) or hasPathWithGivenSum(right, s - tree.value))

    if left is not None:
        return hasPathWithGivenSum(left, s - tree.value)
    if right is not None:
        return hasPathWithGivenSum(right, s - tree.value)

    return s == tree.value

