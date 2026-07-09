class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []
        path = []
        used = [False] * len(nums)

        def subset(i):
            if len(nums) == len(path):
                out.append(path[:])
                return 

            for j in range(len(nums)):
                if used[j] == True:
                    continue


                used[j] = True
                path.append(nums[j])

                subset(i + 1)

                used[j] = False
                path.pop()


        subset(0)
        return out
