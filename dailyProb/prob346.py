# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

# Example:

# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1
# m.next(10) = (1 + 10) / 2
# m.next(3) = (1 + 10 + 3) / 3
# m.next(5) = (10 + 3 + 5) / 3

from collections import deque 
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.nums = deque()
        self.size = size 
        self.total = 0 

    def next(self, val: int) -> float:
        rm = 0
        if len(self.nums) == self.size:
            rm = self.nums.popleft()
        self.nums.append(val)
        self.total -= rm 
        self.total += val 
        return (self.total)/len(self.nums)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
