# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        res = None 
        count = 0

        def dfs(node):
            nonlocal res, count
            
            if not node or res is not None:
                return
            
            dfs(node.left)
            count +=1
            if count == k:
                res = node.val
            
            dfs(node.right)
        
        dfs(root)
        return res
