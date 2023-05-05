#1913maximum product difference between 2 pairs
"""
---given an integer array nums, choosse four distinct indices 
---w,x,y, and z, such that the product difference between the 
---pairs (nums[w],nums[x]) and (nums[y], nums[z]) is maximized
---return the maximum product difference
"""

class Solution(object):
    def maxProductDifference(self,nums):

        #first solution, slow runtime
        """
        secondMin=maxVal=max(nums)
        minVal=min(nums)
        secondMax=0
        if minVal==maxVal:
            return 0
        else:

            for i in range(len(nums)):
                if nums[i]>secondMax and i!=nums.index(maxVal):
                    secondMax=nums[i]
                if nums[i]<secondMin and i!=nums.index(minVal):
                    secondMin=nums[i]

        return maxVal*secondMax-minVal*secondMin
        """


        min1=min2=float('inf')
        max1=max2=float('-inf')

        for n in nums:
            if n<=min1:
                min1,min2=n,min1
            elif n<min2:
                min2=n
            
            if n>max1:
                max1,max2=n,max1
            elif n>max2:
                max2=n
        return max1*max2-min1*min2

nums=[5,6,2,7,4]
solution=Solution()
print(solution.maxProductDifference(nums))