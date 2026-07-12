class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix_arr = []
        running_sum = 0

        for num in nums:
            running_sum += num
            self.prefix_arr.append(running_sum)

        # [-2, 0, 3, -5, 2, -1]
        # running_sum = -3
        # [-2, -2, 1, -4, -2, -3]

    def sumRange(self, left: int, right: int) -> int:
        if left < 1:
            return self.prefix_arr[right]

        return self.prefix_arr[right] - self.prefix_arr[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)