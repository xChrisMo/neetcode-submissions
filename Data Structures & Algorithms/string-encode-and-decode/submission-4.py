class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for string in strs:
            res += str(len(string)) + '#' + string
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            lengthcount = i # start of length
            while s[lengthcount] != "#":
                lengthcount += 1 # keep adding until we see #, stopping on the #
            print(lengthcount)
            
            length = int(s[i:lengthcount]) # from i up to (exluding) the length count
            
            start = lengthcount+1
            end = start + length # end on the next number
            res.append(s[start:end])

            i = end
        return res
