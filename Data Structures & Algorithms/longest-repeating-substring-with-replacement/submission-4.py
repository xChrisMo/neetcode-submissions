class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict_s = {}
        l = 0
        max_r = 0
        longest = 0

        for r in range(len(s)):
            dict_s[s[r]] = dict_s.get(s[r], 0) + 1
            max_r = max(max_r, dict_s[s[r]])

            while (r - l + 1) - max_r > k:
                dict_s[s[l]] -= 1
                l += 1
            
            longest = max(longest, (r - l + 1))

        return longest 