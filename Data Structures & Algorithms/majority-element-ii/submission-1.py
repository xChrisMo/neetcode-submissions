class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        print(sorted(nums))
        #[2, 2, 2, 2, 2, 3, 5, 5, 5, 5]
        n = len(nums)
        target = n // 3

        # bruteforce, use dict, if count > target, add to out
        
        out = set()
        nums_dict = {}

        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1
            
            if nums_dict[num] > target:
                out.add(num)
        
        return list(out)

        # optimise from 2 O(n)?

        # o(1) counting ??