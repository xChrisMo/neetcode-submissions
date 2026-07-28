from heapq import heappush, heappop, heapify

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # tasks, each task is uppercase. given integer n also! 
        # we have to someway separate identical tasks by n !

        # we have to somehow count and make sure we put different elements before next ??
        # how can we even do this ?


        # time starts at 0
        # count all elements,
        # use a counter and a queue
        # add the current time + n and  -1 of the count for that element..

        # [A, A, A, B, C]
        # [-2]   []
        # time


        # q = [(count, timediff)]
        
        q = deque()
        count_tasks = Counter(tasks)
        t = 0
        max_heap = [-val for val in count_tasks.values()]

        heapify(max_heap)
        # print(max_heap)
        

        while q or max_heap:
            # while we hav either the max heap or the queue not empty
            # we keep working on the time
            t += 1
            if max_heap:
                count = 1 + heappop(max_heap)

                # if the count is not 0, add the count - 1, to say we used it, 
                # we used it, and tjhsis is its next allowed usage
                if count != 0:
                    q.append([count, n + t])

            # what is next ? cos at some point we exhaust the max_heap, 
            # we would have to work on the queue! 

            # if queue and if q[0][1] == t:
            # we push that point back into the heap to be redone 
            if q and q[0][1] == t:
                heappush(max_heap, q.popleft()[0])

        return t