# Given an n-ary tree, return the postorder traversal of its nodes' values.

# For example, given a 3-ary tree:

          n
          
     n    n    n  
     
   n n n   
   
# Return its postorder traversal as: [5,6,3,2,4,1].

 
# Note:

# Recursive solution is trivial, could you do it iteratively?

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = [] 
        def helper(n: 'Node', res: List[int]) -> List[int]:
            if not n:
                return
            for c in n.children:
                helper(c, res)
            res.append(n.val)    
        helper(root, res)
        return res 
