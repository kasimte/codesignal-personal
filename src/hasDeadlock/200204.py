def hasDeadlock(graph):
    '''
    Returns true if there is a cycle in this graph.
    '''
    return any(containsCycle(graph, x, [False]*len(graph)) for x in range(len(graph)))

def containsCycle(graph, node, path):
    '''
    Returns true if there is a cycle based on node and path in this graph.
    '''
    path[node] = True
    for edge in graph[node]:
        if path[edge] or containsCycle(graph, edge, path.copy()):
            return True
    return False

graph = [[1,2,3], [2,3], [3], []]
print(hasDeadlock(graph))
