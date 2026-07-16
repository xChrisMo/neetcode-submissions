class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        out = []

        while i < len(word1) and j < len(word2):
            out.append(word1[i])
            i += 1

            out.append(word2[j])
            j += 1

        out.extend(word1[i:])
        out.extend(word2[j:])

        return ''.join(out)