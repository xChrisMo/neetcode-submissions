class NumArray:
    def __init__(self, nums: List[int]):
        #prefix sum would be an array, so new value would be last val + latest num
        # we need to have that boundary checker
        last_val = 0
        self.prefix_arr = [0]

        for num in nums:
            last_val += num
            self.prefix_arr.append(last_val)
        print(self.prefix_arr)

        #[0, -2, -2, 1, -4, -2, -3]


    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_arr[right + 1] - self.prefix_arr[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)