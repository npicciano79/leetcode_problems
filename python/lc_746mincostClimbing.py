#746 minimum cost climbing stairs
"""
--given and interger array cost where cost[i] is the cost of hte ith
--step on a staircase, once you pay the cost, climb to step 1 or 2
--return mimum cost to climb stairs 
"""

class Solution(object):
    def minCostClimbingStairs(self,cost):
        cost.append(0)

        for i in range(len(cost)-2,-1,-1):
            if i+2>=len(cost):
                secondValue=0
            else:
                secondValue=cost[i+2]
            cost[i]=min(cost[i]+cost[i+1],cost[i]+secondValue)
        
        return min(cost[0],cost[1])


cost=[10,15,20]
solution=Solution()
print(solution.minCostClimbingStairs(cost))