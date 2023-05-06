#lc 2372 largest local values in a matrix
"""
---given an nxn integer matrix grid
---generate an integer matrix maxLocal of size (n-2)x(n-2) such that
---maxLocal[i][j] is equal to the largest value of the 3x3 matrix in grid
---centerd about row i+1 and j+1
---contiguous 3x3 matrix in grid
"""

class Solution(object):
    def largestLocal(self,grid):

        maxtrixLength=len(grid)
        local=[]

        for row in range(maxtrixLength-2):
            local.append([])
            for col in range(maxtrixLength-2):
                row_one=max(grid[row][col:col+3])
                row_two=max(grid[row+1][col:col+3])
                row_three=max(grid[row+2][col:col+3])
                local_max=max(row_two,row_two,row_three)
                local[row].append(local_max)
        return local
            


grid=[[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
solution=Solution()
print(solution.largestLocal(grid))