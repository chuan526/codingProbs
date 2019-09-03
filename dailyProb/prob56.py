# Given a collection of intervals, merge all overlapping intervals.

# Example 1:

# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:

# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # write your code here
        intervals = sorted(intervals)
        
        mergedIntervals = []  
        for cur in intervals:
            if len(mergedIntervals) == 0:
                mergedIntervals.append(cur)
            else:
                prev = mergedIntervals[-1]
                if prev[1] >= cur[0]:  
                    prev[1] = max(prev[1], cur[1])
                else:
                    mergedIntervals.append(cur)
                    
        return mergedIntervals
        
        
