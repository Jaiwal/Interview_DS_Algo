
#leetcode 515. Find Largest Value in Each Tree Row
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        q=[]
        q.append(root)
        res=[]

        while q:
            level_size=len(q)
            #this will compare so far found max value
            current_level_max=-float('inf')
            for _ in range(level_size):
                node=q.pop(0)
                current_level_max=max(current_level_max,node.val)
                
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            #after completing one level, just add to res
            res.append(current_level_max)

        return res
