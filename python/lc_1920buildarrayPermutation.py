#1920 Build array from permutation
"""
---Given a zero based permutation nums build an array ans
---of the same length, where ans[i]=nums[nums[i]]
"""

class Solution(object):
    def buildArray(self,nums):
        ans=[]
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
            print(ans)
        return ans 

nums=[1,2,1]
solution=Solution()
print(solution.buildArray(nums))