#2553 separate the digits in an array
"""
---given an array of positive integers nums
---return an array ans that consists of the digits of each integer
---in nums after separating them in the same order they appear
"""
"""
Runtime: 52ms beats 93.26%  Memory: 13.7mb beats 64.42%

"""



class Solution(object):
    def separateDigits(self,nums):
        ans=[]
        for num in nums[::-1]:
            while num:
                tempVal=num%10
                ans.append(tempVal)
                num=(num-tempVal)//10
        
        return reversed(ans)

nums=[13,25,83,77]
solution=Solution()
print(solution.separateDigits(nums))