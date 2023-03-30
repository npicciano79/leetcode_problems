#338 counting bits
"""
--given an integer n, return an array of  length n+1
--where ans[i] is the number of 1's in the binary 
--representation 
"""

class Solution(object):
    def countBits(self,n):
        dp=[0]*(n+1)
        offset=1

        for i in range(1,n+1):
            if offset*2==i:
                offset=i
            dp[i]=1+dp[i-offset]
        
        return dp

n=6
solution=Solution()
print(solution.countBits(n))