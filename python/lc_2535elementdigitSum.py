#2535 difference between element sum and digit sum of array 
"""
---given a positive integer array, nums
---return the difference between the element sum 
---and the digit sum of the array
"""

class Solution(object):
    def differenceofSum(self,nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        digitArray=[]
        for num in nums:
            while num>0:
                tempNum=num%10
                digitArray.append(tempNum) 
                num=(num-tempNum)//10
        
        return abs(sum(nums)-sum(digitArray))
    

nums=[1,15,6,3]
solution=Solution()
print(solution.differenceofSum(nums))