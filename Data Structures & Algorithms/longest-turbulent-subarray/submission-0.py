class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l = 0
        r = 1
        prev = None
        n = len(arr)
        max_t = 1

        while r < n:
            # descending
            if arr[r - 1] > arr[r] and prev != '>':
                max_t = max(max_t, r - l + 1)
                r += 1
                prev = '>'

            # ascending
            elif arr[r - 1] < arr[r] and prev != '<':
                max_t = max(max_t, r - l + 1)
                r += 1
                prev = '<'

            else:
                r = r + 1 if arr[r] == arr[r - 1] else r
                l = r - 1
                prev = ''

        return max_t