class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # forward scan approaches
        # [[],[],[],[],[],[],[]]

        # {
        # 1:3
        # 2:2
        # 3:1
        # }

        # [[],[3],[2],[1],[],[],[]]
        count_dict = {}
        frew = len(nums) + 1
        buckets = [[] for i in range(frew)]
        
        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1

        # print(count_dict)
        for val, freq in count_dict.items():
            buckets[freq].append(val)

        print(buckets)
        out = []
        for i in range(len(buckets) - 1, 0, -1):
            for val in buckets[i]:
                out.append(val)
                if len(out) == k:
                    return out

        return out