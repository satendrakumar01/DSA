# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def dfs(node):
            
            
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            post_order.append(node.val)
        post_order = []
        dfs(root)
        return post_order

#         # recursively 
# def postorderTraversal1(self, root):
#     res = []
#     self.dfs(root, res)
#     return res
    
# def dfs(self, root, res):
#     if root:
#         self.dfs(root.left, res)
#         self.dfs(root.right, res)
#         res.append(root.val)

# def postorderTraversal(self, root: TreeNode) -> List[int]:
#         def dfs(node):
#             if not node:
#                 return
#             dfs(node.left)
#             dfs(node.right)
#             post_order.append(node.val)
        
#         post_order = []
#         dfs(root)
#         return post_order