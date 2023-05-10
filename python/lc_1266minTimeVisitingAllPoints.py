#1266 minimum time visiting all points
"""
---on a 2d plane there are n point with integer coordinates points[i] = [xi, yi]. 
---Return the minimum time in seconds to visit all the points in the order given by points.
---In 1 second, you can either:
---move vertically by one unit,
---move horizontally by one unit, or
---move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).
---You have to visit the points in the same order as they appear in the array.
---You are allowed to pass through points that appear later in the order, but these do not count as visits.
"""

class Solution(object):
    def minTimeToVisitAllPoints(self,points):

        p=0
        distance=0

        while p<len(points)-1:
            distance+=max(abs(points[p+1][0]-points[p][0]),abs(points[p+1][1]-points[p][1]))
            
            p+=1
        
        return distance



points = [[1,1],[3,4],[-1,0]]
solution=Solution()
print(solution.minTimeToVisitAllPoints(points))