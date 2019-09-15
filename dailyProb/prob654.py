# Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

# The root is the maximum number in the array.
# The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
# The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
# Construct the maximum tree by the given array and output the root node of this tree.

# Example 1:
# Input: [3,2,1,6,0,5]
# Output: return the tree root node representing the following tree:

#       6
#     /   \
#    3     5
#     \    / 
#      2  0   
#        \
#         1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        
        return self.buildTree(nums)
        
        
    
    def buildTree(self, nums): 
        if not nums:
            return 
        max_val = nums[0]
        max_index = 0 
        for i, val in enumerate(nums): 
            if val > max_val:
                max_index = i 
                max_val = val 
        n = TreeNode(max_val)
        n.left = self.buildTree(nums[:max_index])
        n.right = self.buildTree(nums[max_index+1:])
        return n 
