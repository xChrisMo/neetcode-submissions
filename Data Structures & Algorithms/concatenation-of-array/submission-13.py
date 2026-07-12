class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # resay: double the array
        # constraint: none really 

        # 1st, copy nums into another array (arr), return nums + arr (O1 time, O(2n) {ultimately becomes O(n)} time)

        # arr = nums

        # return nums + arr

        # 2nd, use an array of size 2n, use an index

        out = [0] * (2 * len(nums))

        for i in range(len(out)):
            ind = i % len(nums)
            out[i] = nums[ind]

        return out