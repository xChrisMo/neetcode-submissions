class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0

        for bill in bills:
            if bill == 5:
                fives += 1

            elif bill == 10:
                tens += 1
                if not fives:
                    return False

                fives -= 1

            else:
                change = bill - 5

                if change == 15 and tens > 0 and fives > 0:
                    tens -= 1
                    fives -= 1

                elif change == 15 and fives > 2:
                    fives -= 3

                else:
                    return False

        return True