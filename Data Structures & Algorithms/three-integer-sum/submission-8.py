class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # we should sort
        # then from each index, we do two pointer

        # if i + 1 < nums and it is same as i, continue
        nums.sort()
        out = []

        for i in range(len(nums)):

            # first on the left, 
            if i > 0 and nums[i - 1] == nums[i]:
                continue 
        
            # set i, j 
            j = i + 1
            k = len(nums) - 1

            # while j < k
            while j < k:
                # running_sum = nums[i] + j + k 
                running_sum = nums[i] + nums[j] + nums[k]

                # if running_sum == 0:
                if running_sum == 0:
                    # out.append ([i, j, k])
                    out.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while j < k and nums[j - 1] == nums[j]:
                        j += 1

                    while j < k and nums[k + 1] == nums[k]:
                        k -= 1
                
                elif running_sum > 0:
                    # if running_sum > 0: k -= 1
                    k -= 1 #removing from rihgt, sorted property
                
                else:
                    # if running_sum < 0: j += 1
                    j += 1

                # then checking for duplicates now

                

        return out