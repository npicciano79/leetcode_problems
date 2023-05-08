#1464 Maximum product of 2 elements in an array
"""
---Given the array of integers nums, 
---you will choose 2 different indices i and j of that array
---return the maximum value of nums[i]-1 * nums[j]-1
"""


class Solution(object):
    def maxProduct(self,nums):
        maxVal=0
        max1=0
        max2=0

        for num in nums:
            if num>max1:
                max1,max2=num,max1
            elif num>max2:
                max2=num
        return (max1-1)*(max2-1)
    
        

nums=[3,4,5,2]
solution=Solution()
print(solution.maxProduct(nums))