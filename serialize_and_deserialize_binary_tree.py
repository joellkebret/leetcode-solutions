# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []

        if not root: return ""
        tree = deque([root])

        while tree:
            node = tree.popleft()

            if not node:
                res.append("#")
                continue
            
            res.append(str(node.val))

            # We dont need to check for each because its verified in the condition above
            tree.append(node.left)
            tree.append(node.right)
        
        return ",".join(res)

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # No data
        if not data: return None

        # Get the values of the tree 
        values = data.split(',') # use our comma delimeter
        root = TreeNode(values[0]) # set our root for our bfs

        q = deque([root])
        i = 1

        while q:
            node = q.popleft()

            if node == "#":
                continue

            left = values[i]
            right = values[i+1]
            i+=2

            if left != "#":
                node.left = TreeNode(int(left))
                q.append(node.left)
            
            if right != "#":
                node.right = TreeNode(int(right))
                q.append(node.right)        
        return root 
            
            



        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
