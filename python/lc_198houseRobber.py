"""
--198 House Robber
--you are a professional robber, adjacent houses cannot be robbed
--given integer array (nums), representing amount of money at each house
--return the max amount of money that can be robbed without 
--alerting the police
"""

#dynamic programing solution 
class Solution(object):
    def rob(self,nums):
        
        if not nums:
            return 0
        
        #create maxRobAmount and initialize values
        N=len(nums)
        maxRobAmount=[0 for _ in range(N+1)]

        maxRobAmount[N],maxRobAmount[N-1]=0,nums[N-1]
        
        for i in range(N-2,-1,-1):
            maxRobAmount[i]=max(maxRobAmount[i+1],maxRobAmount[i+2]+nums[i])
        
        return maxRobAmount[0]







nums=[2,7,9,3,1]
solution=Solution()
print(solution.rob(nums))