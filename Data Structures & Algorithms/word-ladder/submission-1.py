from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj_list = defaultdict(list)

        if endWord not in wordList:
            return 0

        wordList.append(beginWord)
        start = None

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j + 1:]
                adj_list[pattern].append(word)

                if word == beginWord:
                    start = pattern

        print(adj_list)
        print(pattern)

        # we want to do a bfs from begin word, keep checking for the target
        # we dont want it circular really
        # so we start from beginWord, go into its neighbors till we find target
        q = deque()
        q.append([beginWord, 1])
        seen = set([beginWord])

        while q:
            word, count = q.popleft()

            if word == endWord:
                return count

            # else we explore its neighbours
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j + 1:]

                for new_word in adj_list[pattern]:
                    if new_word not in seen:
                        seen.add(new_word)
                        q.append([new_word, count + 1])
        return 0
        # o(n^2 * m)

        # where n is for each word, how we loop through the word inside wordlist, and then inside the word, and then m for each word
        # same thing for space, as we store that much pattern. basically we store each word into multiple patterns, as many times as...
