The k-digit number N is an Armstrong number if and only if the k-th power of each digit sums to N.

# Given a positive integer N, return true if and only if it is an Armstrong number.

 

# Example 1:

# Input: 153
# Output: true
# Explanation: 
# 153 is a 3-digit number, and 153 = 1^3 + 5^3 + 3^3.
# Example 2:

# Input: 123
# Output: false
# Explanation: 
# 123 is a 3-digit number, and 123 != 1^3 + 2^3 + 3^3 = 36.


class Solution:
    def isArmstrong(self, N: int) -> bool:
        n_p = N
        digits = [] 
        while n_p > 0:
            digits.append(n_p%10)
            n_p //= 10 
        return N == sum([d**len(digits) for d in digits])
