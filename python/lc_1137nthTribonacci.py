#1137 N-th Tribonacci number
"""
--The tribonacci sequence T(n) is defined as 
--T(0)=0, T(1)=1, T(2)=1 and T(n+3)=T(n)+T(n+1)+T(n+2)
--Given n, return the value of T(n)
"""

class Solution(object):
    def tribonacci(self,n):
        dp=[0]*(n+1)
        if len(dp)==2:
            return 1
        elif len(dp)<2:
            return 0
        else:
            dp[1]=dp[2]=1
        
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
        
        return dp[-1]

n=5
solution=Solution()
print(solution.tribonacci(n))