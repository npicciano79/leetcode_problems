#70 climbing stairs
"""
--climbing a staircase takes n steps to reach the top
--each time you can climb 1 or 2 steps, how many distinct ways can you climb the top
--problem models a fibonacci sequence used with memoization 

"""

class Solution(object):
    def climbStairs(self,n,memo={}):
        if n in memo:
            return memo[n]
        if n<=2:
            return n
        
        memo[n]=self.climbStairs(n-1,memo)+self.climbStairs(n-2,memo)

        return memo[n]



n=3
solution=Solution()
print(solution.climbStairs(n))