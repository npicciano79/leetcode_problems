#2652 sum multiples
"""
---given a positive integer n, find the sum of all integers
---in range [1,n] inclusive, that are divisible by [3,5,7]

"""

class Solution(object):
    def sumOfMultiples(self,n):
        vals=[3,5,7]
        sumVal=0
        for i in range(1,n+1):
            for j in vals:
                if i%j==0:
                    sumVal+=i
                    break
        return sumVal




n=7
solution=Solution()
print(solution.sumOfMultiples(n))