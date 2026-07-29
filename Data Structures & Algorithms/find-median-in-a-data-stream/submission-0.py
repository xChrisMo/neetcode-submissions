class MedianFinder:
    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        self.nums.sort()
        n = len(self.nums)

        if n % 2 == 1:
            return self.nums[n// 2]

        else: 
            return (self.nums[ n // 2 - 1] + self.nums[n // 2]) / 2
"""

use a max heap
use a min heap

"""