# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def pathSumNode(root, sum,previous):
            if root is None:
                return
            previous.append(root.val)
            if root.left is None and root.right is None :
                if sum==root.val:
                    out.append(copy.deepcopy(previous))
                previous.pop()
                return
            pathSumNode(root.left,sum-root.val,previous)
            pathSumNode(root.right,sum-root.val,previous)
            previous.pop()
            
        out=list()
        tmp = list()
        pathSumNode( root, sum,tmp)
        return out
        
                
