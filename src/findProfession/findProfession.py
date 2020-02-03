# Consider a special family of Engineers and Doctors. This family has the following rules:

# * Everybody has two children.
# * The first child of an Engineer is an Engineer and the second child is a Doctor.
# * The first child of a Doctor is a Doctor and the second child is an Engineer.
# * All generations of Doctors and Engineers start with an Engineer.

# We can represent the situation using this diagram:

#                 E
#            /         \
#           E           D
#         /   \        /  \
#        E     D      D    E
#       / \   / \    / \   / \
#      E   D D   E  D   E E   D

# Given the level and position of a person in the ancestor tree above, find the profession of the person.
# Note: in this tree first child is considered as left child, second - as right.


def findProfession(level, pos):
    '''This is the recursive approach.

    Level 1: E
    Level 2: ED
    Level 3: EDDE
    Level 4: EDDEDEED
    Level 5: EDDEDEEDDEEDEDDE

    Intuition:

    Note the pattern that this family creates. Each level is the
    prefix for the next level. E and D mirror each other, so we can
    determine end points and call this recursively, although
    personally I still find it a bit confusing!

    Since the prefix is always the same for each level, if the
    position is odd, we can recursively simplify the problem by going
    to the next level and halving the position.
    '''

    # Since we start with an Engineer, if there is only one level,
    # return Engineer.
    if level == 1:
        return "Engineer"

    # By problem definition, directly underneath Engineer, is an
    # Engineer and then a Doctor, in that order.
    if level == 2 and pos == 1: return "Engineer"
    if level == 2 and pos == 2: return "Doctor"

    # Further down the tree, we can recursively check based on
    # position.
    
    # If the position is odd, assume we are starting with an Engineer.
    if pos % 2 == 1:
        if findProfession(level-1, (pos+1)/2) == 'Engineer': return 'Engineer'
        else: return 'Doctor'
    else:
        # If the position is even, assume we are starting with a
        # Doctor, which is just reversing the start.
        if findProfession(level-1, pos/2) == 'Engineer': return 'Doctor'
        else: return 'Engineer'

# testing
print(findProfession(3, 3)) # Doctor
print(findProfession(2, 2)) # Doctor
print(findProfession(4, 2)) # Doctor
print(findProfession(8, 100)) # Engineer
