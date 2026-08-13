class Solution:
    def reverse(self, x: int) -> int:
        # check if pos or neg
        # do the reversal
        # check if sign * reversal within range
        sign = 1

        if x < 0:
            sign *= -1

        sanitised = abs(x)                                                                                   
        copy = sanitised
        reversed_num = 0

        while copy > 0:
            reversed_num = (reversed_num * 10) + (copy % 10)
            copy //= 10

        reversed_num *= sign

        if (-2 ** 31) < reversed_num < (2 ** 31 - 1):
            return reversed_num

        return 0