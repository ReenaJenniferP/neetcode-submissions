# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, root, subroot):
        if not root and not subroot:
            return True
        
        if not root or not subroot:
            return False

        return root.val == subroot.val and self.isSameTree(root.right, subroot.right) and self.isSameTree(root.left, subroot.left) 

    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if not root or not subroot:
            return False
        if self.isSameTree(root, subroot):
            return True
        else:
            return self.isSubtree(root.right, subroot) or self.isSubtree(root.left, subroot)
