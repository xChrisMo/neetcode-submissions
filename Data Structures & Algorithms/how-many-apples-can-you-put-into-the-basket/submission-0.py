class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        print(weight)
        running_sum = 0
        pick = 0

        for w in weight:
            if running_sum + w > 5000:
                break 

            running_sum += w
            pick += 1

        return pick
