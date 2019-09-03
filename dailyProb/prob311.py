# Given two sparse matrices A and B, return the result of AB.

# You may assume that A's column number is equal to B's row number.

# Example:

# Input:

# A = [
#   [ 1, 0, 0],
#   [-1, 0, 3]
# ]

# B = [
#   [ 7, 0, 0 ],
#   [ 0, 0, 0 ],
#   [ 0, 0, 1 ]
# ]

# Output:

#      |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
# AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
#                   | 0 0 1 |

class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        la,lb,lb0 = len(A), len(B), len(B[0])
        res = [[0]*lb0 for _ in range(la)] 
        
        for i in range(la):
            for j in range(lb0):
                for k in range(lb):
                    if A[i][k] and B[k][j]:
                        res[i][j] += A[i][k] * B[k][j]
        return res 
