class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count_dict = {}

        # for char in nums:
        #     count_dict[char] = count_dict.get(char, 0) + 1

        # return max(count_dict, key=count_dict.get)
        # O(n) space and time

        nums.sort()
        #[5,5,1,1,1,5,5]
        #[1,1,1,5,5,5,5] #for our sample sizes, middle value SHOULD be our majority element

        return nums[len(nums)//2]