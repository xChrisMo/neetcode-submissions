class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        #[1,1,1,0,0,0,1,1,1,1,0]

        #if i == 0: count += 1, if count > k, shift left until we remove 0
        count = 0
        l = 0
        max_cons = float('-inf')

        for r in range(len(nums)):
            if nums[r] == 0:
                count += 1

            while count > k:
                if nums[l] == 0:
                    count -= 1
                l += 1


            max_cons = max(max_cons, (r - l + 1))

        return max_cons