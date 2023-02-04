#300 longest increasing subsequence
"""
--given an integer array, nums, return the length of the longest strictly increasing subsequence


"""

class Solution(object):
    def lengthofLIS(self,nums):
        dp=[1]*len(nums)

        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)



nums=[10,9,2,5,3,7,101,18]
solution=Solution()
print(solution.lengthofLIS(nums))