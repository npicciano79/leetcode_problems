#1232 check if straight line
"""
---given an array of coordiantes where 
---coordinates[i]=[x,y], where [x,y] represents a coordiante of a point 
---determine if these points make a straight line 
"""

class Solution(object):
    def checkStraightLine(self,coordinates):
        #find slope, account for division by 0
        starting_Y=coordinates[1][1]-coordinates[0][1]
        starting_X=coordinates[1][0]-coordinates[0][0]


        starting_Slope=starting_Y/starting_X if starting_X!=0 else 'undef'
        
        #itterate through points 
        for i in range(1,len(coordinates)):
            #itterate through points and calc new slope
            Y_difference=coordinates[i][1]-coordinates[i-1][1]
            X_difference=coordinates[i][0]-coordinates[i-1][0]
            new_Slope=Y_difference/X_difference if X_difference!=0 else 'undef'

            #compare new slope with starting slope 
            if starting_Slope!=new_Slope:
                return False  

        return True


coordinates=[[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
solution=Solution()
print(solution.checkStraightLine(coordinates))