class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        #1,2,3,6
        #1,4,5,9
        seats.sort()
        students.sort()

        diff = 0

        for i in range(len(seats)):
            diff += abs(seats[i] - students[i])

        return diff