# Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

# You may return any answer array that satisfies this condition.

 

# Example 1:

# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        l, r = 0, len(A)-1 
        while l <= r: 
            if A[r]%2==0 and A[l]%2==1:
                A[l],A[r] = A[r], A[l]
                l += 1 
                r -= 1 
            elif A[r]%2 == 1: 
                r -= 1                  
            elif A[l]%2 ==0:
                l += 1                 
        return A   
