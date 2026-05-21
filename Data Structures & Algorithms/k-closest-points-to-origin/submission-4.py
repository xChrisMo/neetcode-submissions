class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def euclidean_dist(point):
            out = (point[0] ** 2) + (point[1] ** 2) 
            return out

        
        for i in range(len(points)):
            points[i] = [euclidean_dist(points[i]), points[i]]

        print(points)

        points.sort(key=lambda x:x[0])

        out = []

        for i in range(k):
            out.append(points[i][1])

        return out