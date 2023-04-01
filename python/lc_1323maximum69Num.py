#1323 maximum 69 number 
"""
--given a positive integer num consisting of only 6 and 9
--return the max value by changing one 6 to a 9
"""
class Solution(object):
    def maximum69Number(self,num):
        
        #better execution of returns,loop, and list
        num=list(str(num))

        for i,char in enumerate(num):
            if char=='6':
                num[i]='9'
                break
        
        return int(''.join(num))


        """
        n=[i for i in str(num)]
        for j in range(len(n)):
            if n[j]=='6':
                n[j]='9'
                return int(''.join(n))
        
        return num
        """




n=9669
solution=Solution()
print(solution.maximum69Number(n))