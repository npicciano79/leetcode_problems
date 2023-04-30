#2367 number of arithmetic triplets
"""
---given a 0-indexed array strictly increasing integers nums
---and positive integer diff, a triplet (i,j,k) is an arithmetic triplet if 
--- i<j<k and nums[j]-nums[i]==diff and nums[k]-nums[j]==diff
---return the number of unique arithmetic triplets
"""

class Solution(object):
    def arithmeticTriplets(self,nums,diff):
        tripletCounter=0

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j]-nums[i]==diff:
                    for k in range(j+1,len(nums)):
                        if nums[k]-nums[j]==diff:
                            tripletCounter+=1
        return tripletCounter

nums=[0,1,4,6,7,10]  
diff=3
solution=Solution()
print(solution.arithmeticTriplets(nums,diff))