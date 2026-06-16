# stream of integeres + window size
# calc + return moving average

# use a fixed data structure of len == size, a deque 
# we eject from front when next is called and size is full
from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.sum = 0
        self.q = deque()

    def next(self, val: int) -> float:
        #add
        self.q.append(val)
       
        #check if overflow, if true, remove left
        if len(self.q) > self.size:
            self.sum -= self.q.popleft()
        
        self.sum += val

        return self.sum / len(self.q)
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
