# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        def check_node(left,right):
            if(left==None and right==None):
                return True
            if((left==None and right!=None) or (left!=None and right==None)):
                return False
            if(left.val!=right.val):
                return False
            else:
                return check_node(left.left,right.right) and check_node(left.right,right.left)
        if not root:
            return True
        return check_node(root.left,root.right)
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        