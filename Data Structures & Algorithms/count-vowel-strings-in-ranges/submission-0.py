class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # [True, False, True, True, True]
        # [1, 0, 2, 3, 4]
        # out = []
        vowels = set(['a', 'e', 'i', 'o', 'u'])

        def vowel_checker(x):
            return (x[0] in vowels) and (x[-1] in vowels)
            

        out = [0] * len(words)
        curr = 0

        for i, word in enumerate(words):
            if vowel_checker(word):
                curr += 1
                out[i] = curr

            else:
                out[i] = out[i - 1]

        print(out)
        ans = []

        for left, right in queries:
            if left == 0:
                ans.append(out[right])

            else:
                ans.append(out[right] - out[left - 1])

        return ans