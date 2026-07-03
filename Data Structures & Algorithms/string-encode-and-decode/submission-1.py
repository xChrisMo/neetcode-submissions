class Solution:
    def encode(self, strs: List[str]) -> str:
        # out = ''
        # when we add a word to encode, we add a '#' after
        out = []
        for char in strs:
            out.append(str(len(char)))
            out.append('#')
            out.append(char)
        return ''.join(out)

    def decode(self, s: str) -> List[str]:
        # split by '#', for loop, in between '#'s, add element
        # 5#Hello5#World

        out = []
        i = 0 #initial position

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1

            length = int(s[i:j])
            i = j + 1

            out.append(s[i:i + length])

            i = i + length
        return out