import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, arg1: int, arg2: int=None):
        if arg2 is None:
            return round((math.pi * arg1 * arg1), 2)

        else:
            return arg1 * arg2

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
