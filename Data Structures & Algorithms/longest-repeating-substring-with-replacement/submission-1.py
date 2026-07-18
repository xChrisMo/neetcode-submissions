class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # add each right letter to a dict, 
        # as you add the letter, 
        # if window length - dict[s[r]] >= k, dict[[s[l]]] -= 1, l += 1!
        # return max_l

        max_l = 0

        dict_s = dict()
        l = 0
        n = len(s)
        max_f = 0

        for r in range(n):

            # add to dict
            dict_s[s[r]] = dict_s.get(s[r], 0) + 1
            max_f = max(max_f, dict_s[s[r]])

            # compare maxl!
            while (r - l + 1) - max_f > k:
                dict_s[s[l]] = dict_s.get(s[l], 0) - 1 
                l += 1
            
            
            max_l = max(max_l , r - l + 1)


        return max_l