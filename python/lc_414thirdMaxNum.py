#414 third maximum number
"""
---given an array of integers nums, 
---return the third distinct maximum number in array
---if third maximum does not exist,return maximum
"""

class Solution(object):
    def thirdMax(self,nums):
        numsSet=sorted(set(nums))

        if len(numsSet)>=3:
            answer=numsSet[-3]
        else:
            answer=numsSet[-1]
    
        return answer

nums=[3,2,1]
solution=Solution()
print(solution.thirdMax(nums))