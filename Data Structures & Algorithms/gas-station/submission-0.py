class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # n stations

        # index at gas == amount of gas at that station
        # index at cost == cost to travel from station index to station index + 1

        if sum(gas) < sum(cost):
            return -1

        total = 0
        start = 0

        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                start = i + 1

        return start