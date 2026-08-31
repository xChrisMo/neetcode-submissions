# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        """
        1. check base conditions
        2. res = recursively divide AND conquer
        3. add up the res's, return that !

        time complexity: worst case - No ships, we look in entire ship, o(ROWS x COLS) OR o(Area of Rectangle)
        space complexity: no extra space, o(1)
        """

        # base conditions
        
        # 1. if inverted, that is, bottomLeftx > toprighty or topLeftx < bottomRighty, return 0

        if topRight.x < bottomLeft.x or topRight.y < bottomLeft.y:
            return 0

        # 2. if noship at position. if Sea.hasShips(topRight, bottomLeft) is False, return 0
        # it only recursively breaks if ship still exists 
        if not sea.hasShips(topRight, bottomLeft):
            return 0

        # 3. if ship at POINT. if Sea.hasShips(topRight, bottomLeft) and all 4 points converge, return 1
        # jackpot
        if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
            return 1

        # get the mid, use that as a reference point for topleft, topright, bottomleft, bottomright
        mid_y = (topRight.y + bottomLeft.y) // 2
        mid_x = (topRight.x + bottomLeft.x) // 2


        Lefttop = self.countShips(sea, Point(mid_x, topRight.y), Point(bottomLeft.x, mid_y + 1)) 
        Righttop = self.countShips(sea, Point(topRight.x, topRight.y), Point(mid_x + 1, mid_y + 1))

        Leftbottom = self.countShips(sea, Point(mid_x, mid_y), Point(bottomLeft.x, bottomLeft.y))
        Rightbottom = self.countShips(sea, Point(topRight.x, mid_y), Point(mid_x + 1, bottomLeft.y))

        return Lefttop + Righttop + Leftbottom + Rightbottom