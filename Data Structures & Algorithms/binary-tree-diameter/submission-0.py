# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxVal = 0
        
        def dfs(root):
            nonlocal maxVal
            if root:
                l = dfs(root.left)
                r = dfs(root.right)
                maxVal = max(maxVal, l+r)
                return max(l, r) + 1
            
            return 0

        dfs(root)

        return maxVal