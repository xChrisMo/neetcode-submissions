
# use a heap.
# if id not in leaderboard, add id with score
# elif id in leaderboad, add score to old score

# top k
# returns sum of top[::k]

#use dict and queue
# 5, 6, 10, 20
# 
from heapq import heappush, heappop

class Leaderboard:

    def __init__(self):
        #use dict 
        #use queue
        self.board = {} #we can store id, (score, position in queue?) 

    def addScore(self, playerId: int, score: int) -> None:
        # add score to dict if id,
        # else dict[id] == score
        self.board[playerId] = self.board.get(playerId, 0) + score

    def top(self, K: int) -> int:
        #sum([:k])
        q = []
        for score in self.board.values():
            heappush(q, score)
            if len(q) > K:
                heappop(q)

        return sum(q)


    def reset(self, playerId: int) -> None:
        #delete from dict
        if playerId in self.board:
            del self.board[playerId]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
