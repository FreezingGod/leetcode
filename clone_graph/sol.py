# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node: return node
        visited = set()
        allnodes = set()
        dorig = {}
        dretn = {}
        allnodes.add(node.label)
        dorig[node.label] = node
        while visited != allnodes:
            diff = allnodes-visited
            for n in diff:
                newnode = UndirectedGraphNode(n)
                dretn[n] = newnode
                visited.add(n)
                for i in dorig[n].neighbors:
                    allnodes.add(i.label)
                    dorig[i.label] = i
        for k, n in dorig.items():
            for i in n.neighbors:
                dretn[k].neighbors.append(dretn[i.label])
        return dretn[node.label]
