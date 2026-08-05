class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        out = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                k = j + 1
                l = n - 1

                while k < l:
                    total_sum = nums[i] + nums[j] + nums[k] + nums[l]

                    if total_sum < target:
                        k += 1

                    elif total_sum > target:
                        l -= 1

                    else:
                        out.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1

                        while k < l and nums[k] == nums[k - 1]:
                            k += 1

                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1

        return out