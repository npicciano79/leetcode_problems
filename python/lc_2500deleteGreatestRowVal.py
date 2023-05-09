#2500 Deleted greatest value in each row
"""
---given an mxn matrix grid consiting of positive integers 
---perform operations until grid is empty 
---delete elemetn with greatest value for each row
---add max value of deleted elements to the answer
---return the answer
"""
class Solution(object):
    def deleteGreatestValue(self,grid):
        ans=0
        rowLen=len(grid[0])

        while rowLen:
            tempMax=0
            for row in grid:
                row.sort()
                tempMax=max(tempMax,row[-1])
                row[-1]=0
            ans+=tempMax
            rowLen-=1
        return ans
    
grid=[[1,2,4],[3,3,1]]
solution=Solution()
print(solution.deleteGreatestValue(grid))