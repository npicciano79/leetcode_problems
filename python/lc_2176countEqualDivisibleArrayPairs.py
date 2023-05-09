#2176 Count equal and divisible pairs in an array
"""
---given a 0-indexed array nums of length n and an 
---integer k, return the number of pairs (i,j)  where 
--- 0<=i<j<n, such that nums[i]==nums[j] and i*j is 
---divisible by k
"""

class Solution(object):
    def countPairs(self,nums,k):


        count,n=0,len(nums)

        for i in range(n):
            for j in range(i+1,n):
                if nums[i]==nums[j] and (j*i)%k==0:
                    count+=1
        
        return count

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