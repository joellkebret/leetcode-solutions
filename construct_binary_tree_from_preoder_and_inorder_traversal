# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        
        # Preorder represents the root of every subtre, doesnt tell us what belongs to each subtree
        # Finding the unique node in our inorder tree allows us to determine that everything to the left
        # is that nodes left subtree and everything to the right is the right subtree

        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        # This is the indicator of left and right subtrees
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid+1])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])


        return root
