class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # sort all

        # so use a for looop
        # use another for lioop inside
        # use k, l 
        
        # check for duplicates
        # running_sum
        
        out = []
        nums.sort()
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i - 1] == nums[i]:
                continue 

            for j in range(i + 1, n):
                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue 
                    
                k = j + 1
                l = n - 1

                while k < l:
                    running_sum = nums[i] + nums[j] + nums[k] + nums[l]

                    if running_sum == target:
                        out.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1

                        while k < l and nums[k] == nums[k - 1]:
                            k += 1

                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1

                    elif running_sum > target:
                        l -= 1

                    else:
                        k += 1

        return out