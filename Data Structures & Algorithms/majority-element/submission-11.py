class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count_dict = {}

        # for char in nums:
        #     count_dict[char] = count_dict.get(char, 0) + 1

        # return max(count_dict, key=count_dict.get)
        # o(n) space and time

        #---------------------

        # nums.me_sort()
        # #[5,5,1,1,1,5,5]
        # #[1,1,1,5,5,5,5] #for our sample sizes, middle value SHOULD be our majority element

        # return nums[len(nums)//2]
        # o(nlogn) time and o(1) space

        #---------------------

        # voting algorithm next: original solution needed
        #bayers voting algorithm

        # max_ele = None
        # count = 1

        # for i in range(len(nums)):
        #     if nums[i] != max_ele:
        #         count -= 1  

        #         if count == 0:
        #             max_ele = nums[i]
        #             count = 1

        #     else:
        #         count += 1

        # return max_ele

        # o(n) time, o(1) space

        #---------------------

        #divide and conquer, proper merge me_sort style

        def me_sort(num):
            if len(num) < 2:
                return num

            n = len(num)
            mid = n // 2

            left = num[:mid]
            right = num[mid:]

            return merge(me_sort(left), me_sort(right))


        def merge(l1, l2):
            #i know we use pointers
            out = []
            i = 0 
            j = 0

            while i < len(l1) and j < len(l2):
                if l1[i] < l2[j]:
                    out.append(l1[i])
                    i += 1

                else:
                    out.append(l2[j])
                    j += 1

            #just incase one overflows
            out.extend(l1[i:])
            out.extend(l2[j:])

            return out

        arr = me_sort(nums)

        return arr[len(arr)//2]
        print(arr)