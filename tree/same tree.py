# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not q or not p:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
# If one of them do not exist and another exist, we return False.
# If two of them are equal to None, we return True.
# If none of two above condition holds, we look at children and return True only if values of nodes are equal and if True holds for left and right subtrees.

# class Solution:
    # def isSameTree(self, p, q):
    #     if p and not q or q and not p: return False
    #     if not p and not q: return True
    #     return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
