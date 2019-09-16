# Return the root node of a binary search tree that matches the given preorder traversal.

# (Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

 

# Example 1:

# Input: [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        cntr = [0] 
        return self.dfs(preorder, cntr)
        
    
    def dfs(self, nums, cntr, bound=float('inf')): 
        if cntr[0] >= len(nums) or nums[cntr[0]] > bound:
            return         
        n = TreeNode(nums[cntr[0]])
        cntr[0] += 1 
        n.left = self.dfs(nums, cntr, n.val)
        n.right = self.dfs(nums, cntr, bound)
        return n 
    
