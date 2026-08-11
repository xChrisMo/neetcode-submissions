class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)

        def condition(m):
            count = 1
            split = 0

            for n in nums:
                split += n
                if split > m:
                    count += 1
                    split = n
                    if count > k:
                        return False

            return True

        while l < r:
            m = l + (r - l) // 2

            if condition(m):
                r = m

            else:
                l = m + 1


        return l