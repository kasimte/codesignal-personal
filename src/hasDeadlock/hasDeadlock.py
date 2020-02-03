def hasDeadlockHash(hash):
    '''This approach reduces the graph by finding terminal nodes and
    removing them. Terminal nodes can be found by empty arrays, or
    ones that don't point anywhere.

    It calls itself recursively, while repeatedly removing terminal
    nodes and creating new terminal nodes until the graph is gone.
    '''
    if len(hash) == 0:
        return False

    empty_key = None
    for i, edges in hash.items():
        if edges == []:
            empty_key = i
            break

    if empty_key == None:
        return True
    
    for i, edges in hash.items():
        if empty_key in edges:
            edges.remove(empty_key)

    # del modifies the has in place
    del hash[empty_key] 

    return hasDeadlockHash(hash)

def hasDeadlock(connections):
    '''
    connections is 2d graph
    return True if cycle is found
    '''

    '''
    This is a naive implementation.

    1. Convert to hash indexed by node index
    2. Call recurisve hasDeadlockHash.
    '''

    hash = {}
    for i, edges in enumerate(connections):
        hash[i] = edges

    return hasDeadlockHash(hash)
