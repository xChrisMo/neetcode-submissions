class Solution:

    def encode(self, strs: List[str]) -> str:
        # when we encode, we add the len, a # and then the string
        out = []

        for word in strs:
            out.append(str(len(word))+'#'+word)

        return ''.join(out)

    def decode(self, s: str) -> List[str]:
        # first .split()
        # first index is len, move 2 indexs, then count value, append it to s
        out = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1

            # 
            length = int(s[i:j])
            out.append(s[j + 1: j + 1 + length])
            i = j + 1 + length

        return out