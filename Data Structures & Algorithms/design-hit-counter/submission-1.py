# counts hit in past 300seconds
# accept timestamp, monotonically increasing
# hit, adds timestamps
# gethits, in within.a 300second range, return no timestamps

#[1, 2, 3, 300, 301]
# so use queue. if [-1] - [0] >= 300: popleft

from collections import deque

class HitCounter:
    def __init__(self):
        self.q = deque()

    def hit(self, timestamp: int) -> None:
        self.q.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.q and timestamp - self.q[0] >= 300:
            self.q.popleft()

        return len(self.q)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
