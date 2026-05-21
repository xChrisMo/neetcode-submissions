class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #for loop yo 
        n = len(nums)

        buckets = [[] for i in range(n + 1)]

        count_dict = {} #value, count

        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1

        # {1: 1, 2: 2, 3: 3}

        print(count_dict)
        
        for key, value in count_dict.items():
            buckets[value].append(key)

        print(buckets)
        
        out = []
        for i in range(len(buckets)-1, -1, -1):
            for char in buckets[i]:
                out.append(char)
                if len(out) == k:
                    return out

