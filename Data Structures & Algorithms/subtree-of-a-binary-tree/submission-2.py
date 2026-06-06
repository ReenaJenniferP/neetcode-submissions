# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, root, subroot):
        if not root or not subroot:
            return root == subroot

        return root.val == subroot.val and self.isSameTree(root.right, subroot.right) and self.isSameTree(root.left, subroot.left) 

    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if not subroot:
            return True
        
        if not root:
            return False

        return self.isSameTree(root, subroot) or self.isSubtree(root.right, subroot) or self.isSubtree(root.left, subroot)
