#62 unique paths
"""
--robot on mxn sized grid in the top left corner grid[0][0]
--robot can only move right and down
--given 2 ints m and n, return the possible # of unique paths to reach bottom right
"""

class Solution(object):
    def uniquePaths(self,m,n):
        dp=[[0 for i in range(n)]for j in range(m)]
        dp[0][0]=1

        for i in range(m):
            for j in range(n):
                if i!=0 and j!=0:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
                else:
                    dp[i][j]=1
        
        return dp[m-1][n-1]



m,n=3,7
solution=Solution()
print(solution.uniquePaths(m,n))