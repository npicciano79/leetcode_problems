#2006 count number pair with absolute difference k
"""
---given an integer array nums and an integer k
---return the numer of pairs (i,j) where 1<j such that
---|nums[i] - nums[j]| == k.
"""

class Solution(object):
    def countKDifference(self,nums,k):
        counter=0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if abs(nums[i]-nums[j])==k:
                    counter+=1

        return counter
    

nums=[1,2,2,1]
k=1
solution=Solution()
print(solution.countKDifference(nums,k))
