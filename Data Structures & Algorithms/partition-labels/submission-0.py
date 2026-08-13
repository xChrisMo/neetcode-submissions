class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # since we want each letter in a narrowed substring, it looks like a dp question
        # and then, after partitioning unique, we add the length of each subset into an output array
        # the key is partitioning into uniques really
        # i am thinking hashmap and dp ? 
        # hashmap and sliding window.. ? 

        # hashmap + sliding window looks like:
        
        # we build a hashmap
        # we count number of uniquem using len dictionary
        # at any point in the sliding widonw we know we have succcessfully covered the count of a right, our right = right + 1, so we can restart from there ??
        dict_nums = {}

        for index, num in enumerate(s):
            dict_nums[num] = index

        # print(dict_nums)
        count = 0
        min_end = 0
        out = []

        for right, num in enumerate(s):
            min_end = max(min_end, dict_nums[num])
            count += 1

            if right == min_end:
                out.append(count)
                count = 0

        return out