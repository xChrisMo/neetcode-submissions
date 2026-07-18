class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_l = 0
        l = 0
        n = len(s)
        seen = set()

        for r in range(n):

            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])
            max_l = max(max_l, r - l + 1)

        return max_l