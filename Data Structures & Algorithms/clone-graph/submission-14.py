"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        def dfs(node, og_to_clone):
            if node in og_to_clone:
                return og_to_clone[node]

            clone = Node(node.val)
            og_to_clone[node] = clone
            for n in node.neighbors:
                clone.neighbors.append(dfs(n, og_to_clone))
            return clone
        og_to_clone = {}
        dfs(node, og_to_clone)
        return og_to_clone[node]