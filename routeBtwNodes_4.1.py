"""
4.1: Route between Nodes
Given a directed graph, design an algo to find out
whether there is a route between two nodes.
"""

def routeBtwNodes(graph, s, d, visited=None):
    """Returns True if there is a route between s and d, False otherwise."""
    if visited is None:
        visited = set()
    
    if s == d:
        return True
    if s not in graph:
        return False

    visited.add(s)
    
    for neighbor in graph[s]:
        if neighbor not in visited:
            if routeBtwNodes(graph, neighbor, d, visited):
                return True
    
    return False

adjacencyList = {
    1: [3],
    2: [1, 3, 4],
    3: [6],
    4: [6],
    5: [1, 4],
    6: [7],
    7: [3]
}
s = 5
d = 2
print(routeBtwNodes(adjacencyList, s, d))
