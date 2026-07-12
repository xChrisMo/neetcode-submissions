class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums
        # if more than once == True
        # else: False

        # sorted ? empty array ? 
        # my assumptions, one element - True, 

        # 1st thought: check if len(set(nums)) == len(nums): return False. return Treu
        # 2nd: use a hash table, if seen, return True, else: False
        # 3rd: a double loop from each val, to check if it exists somehwere else!

        dict_nums = {}

        for num in nums:
            if num in dict_nums:
                return True
            
            dict_nums[num] = dict_nums.get(num, 0) + 1

        return False