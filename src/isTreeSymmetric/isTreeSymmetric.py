#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def equalTrees(f, s):
    '''
    Returns true if two trees are equal. False, otherwise.
    '''

    if f is None and s is None:
        return True

    if f is None:
        return False

    if s is None:
        return False

    v = (f.value == s.value)
    l = equalTrees(f.left, s.right)
    r = equalTrees(f.right, s.left)

    return v and l and r
    
def isTreeSymmetric(t):
    '''Given a binary tree t, determine whether it is symmetric around its
    center, i.e. each side mirrors the other.
    '''
    if t is None:
        return True
    if t.left is None and t.right is None:
        return True
    return equalTrees(t.left, t.right)

# Log:
# - I got mixed up initially about it being a mirror and not identity.
