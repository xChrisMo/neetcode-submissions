class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count_dict = {}

        # for char in nums:
        #     count_dict[char] = count_dict.get(char, 0) + 1

        # return max(count_dict, key=count_dict.get)
        # o(n) space and time

        #---------------------

        # nums.sort()
        # #[5,5,1,1,1,5,5]
        # #[1,1,1,5,5,5,5] #for our sample sizes, middle value SHOULD be our majority element

        # return nums[len(nums)//2]
        # o(nlogn) time and o(1) space

        #---------------------

        # voting algorithm next: original solution needed
        #bayers voting algorithm

        max_ele = None
        count = 1

        for i in range(len(nums)):
            if nums[i] != max_ele:
                count -= 1  

                if count == 0:
                    max_ele = nums[i]
                    count = 1

            else:
                count += 1

        return max_ele