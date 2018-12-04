#98. Validate Binary Search Tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def isBST(self, root,min_val,max_val):
        if root is None:
            return True
        if root.val<=min_val or root.val>=max_val:
            return False
        return self.isBST(root.left,min_val,min(max_val,root.val)) and   self.isBST(root.right,max(min_val,root.val),max_val)

    def isValidBST(self, root):

        
        return self.isBST(root,-sys.maxint,sys.maxint)
