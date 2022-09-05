# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def fun(root):
    if root is None:
        return
    if root.left and root.left.left is None and root.left.right is None:
        fun.leftSum+=root.left.val
    fun(root.left)
    fun(root.right)
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        fun.leftSum=0
        fun(root)
        return fun.leftSum
        