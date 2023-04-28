#1929 concatenation of arrays
"""
---given an array of ints nums, of length n, create an array ans
---of length 2n, where ans[i]=nums[i] and ans[i+n]=nums[i]
---ans is the concatenation of 2 nums arrays
"""

class Solution(object):
    def getConcatenation(self,nums):

        
        ans=[]
        for i in range(2):
            for num in nums:
                ans.append(num)

        return ans




nums=[1,2,1]
solution=Solution()
print(solution.getConcatenation(nums))