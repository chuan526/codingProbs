# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

# This is case sensitive, for example "Aa" is not considered a palindrome here.

# Note:
# Assume the length of given string will not exceed 1,010.

# Example:

# Input:
# "abccccdd"

# Output:
# 7

# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_cnt = {}
        for c in s: 
            if c not in char_cnt: char_cnt[c] = 0 
            char_cnt[c] += 1 
        res = 0
        has_odd = False 
        for c, cnt in char_cnt.items():
            res += cnt // 2 
            if not has_odd and cnt%2 != 0: has_odd = True 
        return res * 2 + 1 if has_odd else res * 2 
