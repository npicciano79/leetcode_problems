#55 jumpgame 
""""
---given an integer array nums, positioned at the array first index
---each element in array represents the max jump lenght at that position 
--return true if you can reach last index or false
"""

class Solution(object):
    def canJump(self,nums):
        dp=[False]*len(nums)
        dp[0]=True

        cur=0
        for maxVal in range(1,len(nums)):
            while cur<maxVal:
                if dp[cur]==True and nums[cur]+cur>=maxVal:
                    dp[maxVal]=True
                    break 
                cur+=1
        
        return dp[-1]



nums=[3,2,1,0,4]
solution=Solution()
print(solution.canJump(nums))