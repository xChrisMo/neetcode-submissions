class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use the size of length as the max count...
        # loop through each num, count and fill
        # from reverse, add into an 'out'

        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        dict_nums = {}

        for num in nums:
            dict_nums[num] = dict_nums.get(num, 0) + 1


        for num, count in dict_nums.items():
            buckets[count].append(num)

        out = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                if len(out) < k:
                    out.append(num)

        return out