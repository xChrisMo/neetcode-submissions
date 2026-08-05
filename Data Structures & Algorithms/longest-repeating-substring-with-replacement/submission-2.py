class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_dict = {}
        l = 0
        n = len(s)
        max_r = 0
        res = 0

        for r in range(len(s)):
            count_dict[s[r]] = count_dict.get(s[r], 0) + 1
            max_r = max(max_r, count_dict[s[r]])

            while (r - l + 1) - max_r > k:
                count_dict[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res