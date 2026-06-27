class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        count_ones = 0

        for val in s:
            if val == '1':
                count_ones += 1

        if count_ones == len(s):
            return count_ones - 1

        if count_ones == 0:
            return len(s) - 1

        count_zeros = 0

        for i in range(len(s)-1):
            char = s[i]
            if char == '0':
                count_zeros += 1

            if char == '1': 
                count_ones -= 1

            max_score = max(max_score, count_ones + count_zeros)


        return max_score