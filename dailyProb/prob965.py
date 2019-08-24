# A binary tree is univalued if every node in the tree has the same value.

# Return true if and only if the given tree is univalued.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        def helper(n: TreeNode) -> bool:
            if not n: 
                return True
            return n.val == root.val and helper(n.left) and helper(n.right)
        return helper(root)
