import heapq
from collections import deque,Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        ABC-A---A
        A:3 B:1 C:1

        '''
        countTasks= Counter(tasks)
        maxHeap=[-cnt for cnt in countTasks.values()]
        print(maxHeap)
        queue= deque()
        heapq.heapify(maxHeap)
        time=0

        while maxHeap or queue:
            time+=1
            if maxHeap:
                val=1+heapq.heappop(maxHeap)
                if val:
                    queue.append([val,time+n])
            
            if queue and queue[0][1]==time:
                cnt,time=queue.popleft()
                heapq.heappush(maxHeap,cnt)
        return time


        

        