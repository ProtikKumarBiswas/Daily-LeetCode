
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

import numpy as np
class Solution:
    def isLeaf(self, X):
        if type(X) == int:
            return True
        return (X==X[0][0]).all()

    def construct(self, grid: List[List[int]]) -> 'Node':
        grid = np.array(grid)
 
        if self.isLeaf(grid):
            return Node(grid[0][0], True, None, None, None, None)
        
        mid = int(grid.shape[0]/2)
        #Top Left
        if self.isLeaf(grid[:mid, :mid]):
            topLeft = Node(grid[0][0], True, None, None, None, None)
        else:
            topLeft = self.construct(grid[:mid, :mid])
            
        #Top Right
        if self.isLeaf(grid[:mid, mid:]):
            topRight = Node(grid[0][mid], True, None, None, None, None)
        else:
            topRight = self.construct(grid[:mid, mid:])
            
        #Bottom Left
        if self.isLeaf(grid[mid:, :mid]):
            botLeft = Node(grid[mid][0], True, None, None, None, None) 
        else:
            botLeft = self.construct(grid[mid:, :mid])
            
        #Bottom Right
        if self.isLeaf(grid[mid:, mid:]):
            botRight = Node(grid[mid][mid], True, None, None, None, None)
        else:
            botRight = self.construct(grid[mid:, mid:])
            
        root = Node(False, False, topLeft, topRight, botLeft, botRight)
        
        return root
 
