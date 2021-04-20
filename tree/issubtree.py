# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        # case s is null, t is defined so no need to check if null
        if s is None:
            return False
        if self.sameTree(s,t):
            return True
        return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
    
    def sameTree(self, s, t)->bool:
        if t is None and s is None:
            return True
        if t is None or s is None:
            return False
        return s.val == t.val and self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
    
        
        
        
        
