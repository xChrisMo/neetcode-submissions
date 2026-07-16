class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count_nums = defaultdict(int)

        for num in nums:
            count_nums[num] += 1

            if len(count_nums) < 3: # this is what makes us o(1)!
                continue 

            count_new_nums = defaultdict(int)
            for num, count in count_nums.items():
                if count > 1:
                    count_new_nums[num] = count - 1

            count_nums = count_new_nums

        res = []
        for num in count_nums:
            if nums.count(num) > len(nums) // 3:
                res.append(num)

        return res
            