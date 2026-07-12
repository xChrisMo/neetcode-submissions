class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # since values are between -1000 to 1000. we can do a bucket sort...
        n = len(nums)

        # so we count all nums first
        # and then we empty it into a list
        # from behind we also empty the list!

        dict_nums = {}

        for num in nums:
            dict_nums[num] = dict_nums.get(num, 0) + 1

        # {1:1, 2:2, 3:3}
        # we can make a bucket of size of len(nums)
        # buckets = [[] for i in range(n + 1)], so we make o to n 
        # then for each num, count in dict_nums.items(), buckets[count].append(num)

        # make an out, from behind empty the buckets! if len(out) == k: return 

        buckets = [[] for i in range(n + 1)]

        for num, count in dict_nums.items():
            buckets[count].append(num)

        out = []

        for i in range(len(buckets) - 1, -1, -1):
            for val in buckets[i]:
                if len(out) < k:
                # i need to empty each bucket list
                    out.append(val)

        return out
