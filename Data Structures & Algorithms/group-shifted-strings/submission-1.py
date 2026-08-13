class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        # quite deceptive, but the question looks like we are asked to group strings of the same length
        # fofrward scan through strings, 
        # for each string, store its count as the key, it itself as a value inside the dict
        dict_strings = defaultdict(list)

        for char in strings:
            pattern = []
            for i in range(1, len(char)):
                pattern.append((ord(char[i]) - ord(char[i - 1])) % 26)
            
            dict_strings[tuple(pattern), len(char)].append(char)

        return list(dict_strings.values()) 