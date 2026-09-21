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
        # if the shape is inverted
        # if not ship actually
        # if there actually is a point !

        if topRight.x < bottomLeft.x or topRight.y < bottomLeft.y:
            return 0

        if not sea.hasShips(topRight, bottomLeft):
            return 0
            
        if topRight.y == bottomLeft.y and topRight.x == bottomLeft.x:
            return 1

        # topLeft
        # bottomLeft
        # topRight
        # bottomRight

        mid_x = (topRight.x + bottomLeft.x) // 2
        mid_y = (topRight.y + bottomLeft.y) // 2

        topLeftQuadrant = self.countShips(sea, Point(mid_x, topRight.y), Point(bottomLeft.x, mid_y + 1))
        bottomLeftQuadrant = self.countShips(sea, Point(mid_x, mid_y), Point(bottomLeft.x, bottomLeft.y))

        bottomRightQuadrant = self.countShips(sea, Point(topRight.x, mid_y), Point(mid_x + 1, bottomLeft.y))
        topRightQuadrant = self.countShips(sea, Point(topRight.x, topRight.y), Point(mid_x + 1, mid_y + 1))

        return topLeftQuadrant + bottomLeftQuadrant + bottomRightQuadrant + topRightQuadrant