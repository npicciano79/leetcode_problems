#2160 minimum sum of 4 digit numbers after spliting digits
"""
---you are given a positive integer num consisting of exactly 4 digits 
---split num into 2 digits num1 and num2, return minimum possible sum of
---num1 and num2
"""
class Solution(object):
    def minimumSum(self,num):
        index=0
        digit=[0]*4

        while num>0:
            
            digit[index]=num%10
            num=(num-digit[index])/10
            index+=1
            print(digit)
        digit.sort()

        return int(digit[0]*10+digit[2]+digit[1]*10+digit[3])
    




num=2932
solution=Solution()
print(solution.minimumSum(num))