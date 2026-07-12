class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # we want the longest prefix shared by ALL in the string
        # would we get a case where there is a '' in strs ?
        # if none, return ''

        # i want to do a vertical scan without making it o(n^2)..
        # we are trying to do the longest common length from 0

        for i in range(len(strs[0])):
            for j in range(1, len(strs)): # starting from the ones we havent seen
                if i == len(strs[j]) or strs[0][i] != strs[j][i]: # loop through all other strings in strs...
                        return strs[0][:i]

        return strs[0]

         