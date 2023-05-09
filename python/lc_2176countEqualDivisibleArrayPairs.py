#2176 Count equal and divisible pairs in an array
"""
---given a 0-indexed array nums of length n and an 
---integer k, return the number of pairs (i,j)  where 
--- 0<=i<j<n, such that nums[i]==nums[j] and i*j is 
---divisible by k
"""

class Solution(object):
    def countPairs(self,nums,k):

        #solution fails for larger array lengths 
        """
        nums.sort()
        combinations=0
        for i in range(len(nums)-1):
            j=i+1
            if nums[i]==nums[j]:
                if (i*j)%k==0:
                    combinations+=1
                    j+=1
                else:
                    continue
        
        return combinations
        """


nums=[3,1,2,2,2,1,3]
k=2
solution=Solution()
print(solution.countPairs(nums,k))