#2215 find the difference of 2 arrays
"""
---given a 0indexed array nums1 and nums2, return a list
---ans of size 2 where ans[0] is a list of all distinct 
---integers in nums1 which are not present in nums2.
---answer[1] is a list of all distinct integers in nums2 which are not present in nums1.

"""

class Solution(object):
    def findDifference(self,nums1,nums2):
        ans1=[]
        ans2=[]

        ans1=[x for x in nums1 if x not in nums2]
        ans2=[y for y in nums2 if y not in nums1]

        return [set(ans1),set(ans2)]
    
nums1 = [1,2,3]
nums2 = [2,4,6]
solution=Solution()
print(solution.findDifference(nums1,nums2))
        
