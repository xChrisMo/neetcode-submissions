from collections import deque
from heapq import heappop, heappush

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # i can count how many times each uppercase task appears
        # ['X','X','Y','Y'], n = 2
        # X:2, Y:2
        # X, _, _, Y, _, _
        # so we somehow have to make the Y come insdie one of X's idle moments because we are minimizing
        # i can use a t...

        # so when any character is used, i can remove 1 count, and then add n  to it
        # so like in our example, X -= 1 would be 1, and then adding 2 means the next accepted usage would be AFTER 3

        # we would have a t initialised to 0
        # we add all tasks to like a hashmap[task]=count
        # make a maxheap so we get the most frequent first
        # when we pop, we add it to the q
        # adding its time to n + 1
        # q = [] (t + n + 1, remaining_count)
        # when all is popped we return t

        # [(-2, y)]
        # [(2 + 1 + 2, count(1), x)], t = 2
        # 

        max_heap = [] # count, task
        dict_tasks = {}

        for task in tasks:
            dict_tasks[task] = dict_tasks.get(task, 0) + 1

        for task, count in dict_tasks.items():
            heappush(max_heap, [-count, task])

        t = 0

        q = deque() # next_time, remainig count, task 
        while max_heap or q:
            while q and t >= q[0][0]:
                _, remaining, task = q.popleft()
                heappush(max_heap, [remaining, task])

            if max_heap:
                count, task = heappop(max_heap)
                count += 1

                if count < 0:
                    q.append([t + n + 1, count, task])

            t += 1

        return t