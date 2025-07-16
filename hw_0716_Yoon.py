class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p==None and q==None:
            return True
        if q ==None or p==None:
            return False
        if p.val!=q.val:
            return False
        if p.val==q.val:
            return True
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
