#637
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root: #들어오는 root의 값이 None일때
            return []
        
        result=[]
        queue=deque([root])

        while queue:
            level_numof_nodes=len(queue)
            current_level=[]
            level_sum=[]

            for _ in range(level_numof_nodes):
                node=queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
                level_sum.append(node.val)
            
            result.append((sum(level_sum))    /    (len(level_sum)))
             
        return result