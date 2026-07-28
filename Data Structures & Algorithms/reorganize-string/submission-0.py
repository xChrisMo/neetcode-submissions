        # [y, x, a]
        # [].      [(-1, 'y')]

        # while max_heap or len(q) > 0:
        #     cnt, letter = heappop(max_heap)
        #     cnt += 1

        #     if cnt > 0:
        #         q.append((cnt, letter))
            
        #     out.append(letter)
            
        #     while q:
        #         cnt, letter = q.popleft()
        #         cnt += 1

        #         # maybe i can rework this logic to be somewhat circular ?
        #         if out[-1] != 'letter':
        #             out.append(letter)

        #         if cnt > 0:
        #             heappush(max_heap, (cnt, letter))

from heapq import heappop, heappush, heapify
from collections import deque

class Solution:
    def reorganizeString(self, s: str) -> str:
        # adjacent not the same
        # count all words
        # add to a max heap
        # so youd have
        # y:-2, x:-1, a:-1

        # so when we use one y, we add it to the q, and reduce its count, we surface another letter
        # basically, use a queue to add intermitently
        # if nothing in queue and current == last_index
        # return 

        # if former is the same as next and queue is empty, return ''

        # else, return ''.join(out)

        out = []

        dict_s = {}

        for ch in s:
            dict_s[ch] = dict_s.get(ch, 0) + 1

        max_heap = []

        for letter, val in dict_s.items():
            heappush(max_heap, (-val, letter))  

        out = []
        q = deque()
        prev = None


        # out = ['y', 'x', 'a']
        #                           ['y':-1]
        # 

        while max_heap or prev:
            # 1. If heap is empty but q has stuff, we're stuck -> return ""
            if prev and not max_heap:
                return ''
            
            # 2. Pop from heap, add to result, decrement count
            cnt, letter = heappop(max_heap)
            out.append(letter)
            cnt += 1

            # 3. If q has a character, it is now "safe" to use -> move it back to heap
            if prev:
                heappush(max_heap, prev)
                prev = None
            
            # 4. If current character still has count > 0, put it into q
            if cnt < 0:
                prev = (cnt, letter)
        
        return ''.join(out)
