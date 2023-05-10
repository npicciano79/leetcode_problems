#1827 minimum operation to make array increasing
"""
---given an integer array nums, in one operation an element can be incremented 
---by 1.  Return the minimum number of operations needed to make nums strictly increasing
---For example, if nums = [1,2,3], you can choose to increment nums[1] to make nums = [1,3,3].

"""

class Solution(object):
    def minOperations(self,nums):
        count=0
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                count+=(nums[i-1]-nums[i]+1)
                nums[i]+=nums[i-1]-nums[i]
        
        return count

nums = [1,5,2,4,1]
solution=Solution()
print(solution.minOperations(nums))