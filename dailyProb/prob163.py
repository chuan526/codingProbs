# Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

# Example:

# Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
# Output: ["2", "4->49", "51->74", "76->99"]

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        start, end = lower, 0 
        res = []
        for n in nums: 
            end = n - 1 
            self.insertRange(res, start, end)
            start = n + 1 
        self.insertRange(res, start, upper)
        return res 
    
    
    def insertRange(self, res: List[str], start: int, end: int) -> None: 
        if start > end:
            return 
        if start == end: 
            res.append(str(start))
        else:
            res.append(str(start) + '->' + str(end))
