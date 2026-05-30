class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        # count_ones = 0
        # count_zeros = 0

        # for char in s:
        #     if char == '0':
        #         count_zeros += 1

        #     else:
        #         count_ones += 1

        # out = []
        # while count_ones > 1:
        #     out.append('1')
        #     count_ones -= 1

        # for i in range(count_zeros):
        #     out.append('0')
    
        # out.append('1')
        # print(out)

        # return ''.join(out)
        
        count = 0

        for char in s:
            if char == '1':
                count += 1

        return (count - 1) * '1' + (len(s) - count) * '0' + '1'