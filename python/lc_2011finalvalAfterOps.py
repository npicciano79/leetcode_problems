#2011 Final value after performing operations
"""
---given operations --X, ++X as an array and initial value of 0
---return value after performing operations
"""

class Solution(object):
    def finalValueAfterOperation(self,operations):
        intitial=0
        for j in operations:
            if '+' in j:
                intitial+=1
            else:
                intitial-=1
        
        return intitial
    

operations=["--X","++X",'X++']
solution=Solution()
print(solution.finalValueAfterOperation(operations))