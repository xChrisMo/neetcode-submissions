class Solution:
    def encode(self, strs: List[str]) -> str:
        # since it can be any character, we should append the len of word in strs before strs itself
        out = []

        for char in strs:
            val = len(char)
            out.append(str(val) + '#' + char)

        return ''.join(out) 
        # '15#Hello5#World'

    def decode(self, s: str) -> List[str]:
        # we use like a check to check if it is a num, we make a list, append for _ in range times and then join the list to an out out
        
        # '25#Hello5#World'

        # while s[r].isdigit:
        # l += 1
        # dist = int(s[r:l])

        # out.append(s[i+l:dist])
        out = []

        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
                # this never breaks out ?? how man !??

            dist = int(s[i:j]) # start from i to j + 1, excluding j + 1, meaning j ??

            # so now we start from l + 2? skipping where l stopped (l + 1) and also the '#', (l + 2)!
            word = s[j + 1: dist + j + 1] # start from our new j, but move only dist amount!
            i = j + 1 + dist
            
            out.append(word)
        return out