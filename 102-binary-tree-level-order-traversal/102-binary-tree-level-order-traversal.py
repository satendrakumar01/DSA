# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        if not root:
            return ans
        tem=[]
        q=deque([None,root])
        while True:
            x=q.pop()
            if x:
                tem.append(x.val)
                if x.left:
                    q.appendleft(x.left)
                if x.right:
                    q.appendleft(x.right)
            else:
                ans.append(tem)
                tem=[]
                if q:
                    q.appendleft(None)
                else:
                    break;
        return ans
        