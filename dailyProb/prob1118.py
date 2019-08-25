# Given a year Y and a month M, return how many days there are in that month.

 

# Example 1:

# Input: Y = 1992, M = 7
# Output: 31
# Example 2:

# Input: Y = 2000, M = 2
# Output: 29
# Example 3:

# Input: Y = 1900, M = 2
# Output: 28

class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:
        if M in {1,3,5,7,8,10,12}:
            return 31 
        elif M == 2:
            if Y%4 == 0 and Y%100 != 0:
                return 29
            elif Y%100 == 0 and Y%400 ==0:
                return 29 
            else:
                return 28
        else:
            return 30 
