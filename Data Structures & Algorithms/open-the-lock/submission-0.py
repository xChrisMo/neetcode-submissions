from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)

        if '0000' in visited: return -1

        q = deque()
        # specify start and at a 1
        q.append(['0000', 0])
        visited.add('0000')

        def move(curr) -> List[str]:
            out = []

            for i in range(4):
                # we need to force move 0000 into 1000 and into 0001
                digit = str((int(curr[i]) + 1) % 10)
                out.append(curr[:i] + digit + curr[i+1:])
                digit = str(((int(curr[i]) - 1) + 10) % 10)
                out.append(curr[:i] + digit + curr[i+1:])

            return out

        while q:
            curr, time = q.popleft()

            # terminal
            if curr == target:
                return time

            # check the nexts, 
            for next in move(curr):
                if next not in visited:
                    visited.add(next)
                    q.append((next, time + 1))

        
        return - 1