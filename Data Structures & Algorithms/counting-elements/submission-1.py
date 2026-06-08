class Solution:
    def countElements(self, arr: List[int]) -> int:
        set_arr = set(arr)
        count = 0

        for char in arr:
            if char + 1 in set_arr:
                count += 1

        return count