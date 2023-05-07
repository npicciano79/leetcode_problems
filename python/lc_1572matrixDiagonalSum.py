#1572 Martix Diagonal Sum
"""
---given a square matrix mat, return the sum of the diagonals
"""

class Solution(object):
    def diagonalSum(self,mat):
        n=len(mat)-1
        counter=0
        matSum=0
        for row in mat:
            #matSum+=row[0+counter]+row[n-counter]
            
            
            leftVal=row[0+counter]
            rightVal=row[n-counter]
            matSum+=(leftVal+rightVal)
            #matSum+=(row[0+counter]+row[n-counter])
            counter+=1
        if n%2==0:
            middle=mat[n//2][n//2]
        else:
            middle=0
        return matSum-middle


mat=[[1,2,3],[4,5,6],[7,8,9]]
solution=Solution()
print(solution.diagonalSum(mat))