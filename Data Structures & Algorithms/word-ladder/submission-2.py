class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        adj_list = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                adj_list[pattern].append(word)

        res = 1
        q = deque()

        q.append(beginWord)
        
        visited = set()
        visited.add(beginWord)

        while q:
            for _ in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return res

                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j + 1:]

                    for simialr_word in adj_list[pattern]:
                        if simialr_word not in visited:
                            q.append(simialr_word)
                            visited.add(simialr_word)

            res += 1

        return 0