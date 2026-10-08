class Solution:
    def countSeniors(self, details: List[str]) -> int:
        elderly = 0

        for detail in details:
            if int(detail[11:13]) > 60:
                elderly += 1

        return elderly