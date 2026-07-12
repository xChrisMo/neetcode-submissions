from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we want to encode each number to its count of characters
        # do we only have lower english letters? yes

        # off the bat, i think we want to encode each unqiye value as a key to a dict
        # the str themselves as a value!

        dict_values = defaultdict(list) # maps value of chars to str

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1

            dict_values[tuple(count)].append(word)


        return list(dict_values.values())