# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        # 1st method using string to compare print preorder
        sTree = helper(s)
        tTree = helper(t)
        if tTree in sTree:
            return True
        return False
# must be outside of class to call. otherwise need to be inside isSubtree function
def helper(root):
        if root is None:
            return "Null"
            
        return "$" + str(root.val) + ' ' + helper(root.left) + ' ' + helper(root.right)
            
        
        # 2nd method using recursive
#     def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
#         # case s is null, t is defined so no need to check if null
#         if s is None:
#             return False
#         if self.sameTree(s,t):
#             return True
#         return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
    
#     def sameTree(self, s, t)->bool:
#         if t is None and s is None:
#             return True
#         if t is None or s is None:
#             return False
#         return s.val == t.val and self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
    
        
        
        
        
