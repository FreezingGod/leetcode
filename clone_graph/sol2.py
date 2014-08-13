# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

# DFS solution
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node: return node
        dd = {}
        return self.dfs(node, dd)
    def dfs(self, node, dd):
        if not node: return node
        if node.label in dd: return dd[node.label]
        newnode = UndirectedGraphNode(node.label)
        dd[node.label] = newnode
        for n in node.neighbors:
            newnode.neighbors.append(self.dfs(n, dd))
        return newnode
