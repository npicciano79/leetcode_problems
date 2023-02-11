#213 house robber 2
"""
---you are a professional robber who cannot rob adjacent houses, 
--houses are arranged in a circle, this is the change from houserobber 1
--given an array representing money at each house 
--return the maximum amount that can be robbed without contacting the police
"""

#soution
"""
--initalize rob1 and rob2 as 0
--loop through nums
--set tempMax as maximum of current value(n) plus rob1 value and rob2
--set rob1 to rob2
--set rob2 to tempMax
--return rob2 after loop
"""


class Solution(object):

    def robFunction(self,nums):
        return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]))


    def helper(self,nums):

        rob1=rob2=0

        for n in nums:
            tempMax=max(n+rob1,rob2)
            rob1=rob2
            rob2=tempMax

        return rob2



nums=[1,2,3,1]
solution=Solution()
print(solution.robFunction(nums))