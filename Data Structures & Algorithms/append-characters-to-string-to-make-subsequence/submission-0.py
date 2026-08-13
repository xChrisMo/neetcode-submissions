class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # basicaclly we want to find the longest common substring between s and t
        # return t - that really
        # basically we are looking for the LCS of s with t
        # returning t - that.
        # this seems like a greeedy question 

        # while i < len(t):
        # if t[i] == s[i]:
        # count += 1
        # else:
        # i += 1
        # return count - len(t) ? 

        i = j = 0
        count_t = len(t)

        while i < len(s) and j < len(t):
            # if i < len(s):
            #     break 

            if s[i] == t[j]:
                j += 1

            i += 1

        return count_t - j