#2574 left right sum differences
"""
---Given a 0-indexed array nums, find a 0-indexed array answer
---where answer.length == nums.length and answer[i] = |leftSum[i] - rightSum[i]|
"""

class Solution(object):
    def leftRightDifference(self,nums):
        """
        ans=[]
        numsLength=len(nums)

        for i in range(0,numsLength):
            leftSum=sum(nums[0:i])
            rightSum=sum(nums[i+1:])
            ans.append(abs(leftSum-rightSum))

        return ans
        """

        #more efficient solution
        #calculates inital sum of all elements then 
        #removes elements from sum during itteration
        ans=[]
        for idx,num in enumerate(nums):
            if idx==0:
                ans.append(sum(nums))
            else:
                ans.append(ans[idx-1]-num-nums[idx-1])

        return [abs(x) for x in ans]

    
nums=[10,4,8,3]
solution=Solution()
print(solution.leftRightDifference(nums))