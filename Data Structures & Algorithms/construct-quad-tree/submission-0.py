"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)

        if n == 1:
            return Node(grid[0][0], True)
        
        h = n//2
        tl = self.construct([x[:h] for x in grid[:h]])
        tr = self.construct([x[h:] for x in grid[:h]])
        bl = self.construct([x[:h] for x in grid[h:]])
        br = self.construct([x[h:] for x in grid[h:]])

        if (tl.val == tr.val == bl.val == br.val) and tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf:
            return Node(tl.val, True)

        return Node(False, False, tl, tr, bl, br)