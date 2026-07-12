class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s, t
        # if s[scrambled] == t[scrambled]: return True
        # return False

        # ONLY english letters ? are there caps we need to worry about ? 
        # always be same length (we should check this too)

        # off the bat, if length is different, we say no
        if len(s) != len(t):
            return False

        # 1. Getting all chars in S and T in dict, equating the dict to one another
        # 2. sorting both s, and t.
        # 3. counting the ord of characters... very similar to dict really
        
        # list that counts occurence of all 26 characters, checks if it is the same with both
        
        def ord_converter(s: str) -> List[int]:
            out = [0] * 26

            for char in s:
                out[ord(char) - ord('a')] += 1

            return out

        return ord_converter(s) == ord_converter(t)