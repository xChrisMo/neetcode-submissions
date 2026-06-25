class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # bruteforce
        # nums.sort()
        # count = 0
        # n = len(nums)

        # for i in range(n):
        #     curr = 0
        #     for j in range(i, n):
        #         curr += nums[j]
        #         if curr == k:
        #             count += 1
        #             continue

        # return count

        # prefix sum approach
        # use one for loop to add tilll the end, we would get something called a diff
        # we basically want to see how many times from our running sum, we would get a diff already stored up

        prefixMap = {0:1} #meaning we have an empty prefix once

        #so basically, we keep a running sum/
        # total += running sum - prefixMap.get(diff, 0) 
        # but we should update the counts?
        out = 0
        running_sum = 0

        for num in nums:
            # keeps running sum
            running_sum += num

            # this keeps the diff by asking, 
            # 'at anypoint do we have a smaller subarray that sums to what we need to remove before we equal k?

            diff = running_sum - k

            # add if it exists basicallh
            out += prefixMap.get(diff, 0)

            # update the count of that prefix running sum
            prefixMap[running_sum] = prefixMap.get(running_sum, 0) + 1 
            


        return out
        