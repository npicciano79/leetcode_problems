#322 coin change
"""
---given an array of integers, coins, of different denominations and integer amount
---return the fewest number of coins needed to makeup that amount
---runtime: 906ms, memory: 14.1mb
"""

class Solution(object):
    def coinChange(self,coins, amount):
        dp=[amount+1]*(amount+1)
        dp[0]=0

        for a in range(1,amount+1):
            for c in coins:
                #amount of money is larger than the coin 
                #coin can be subtracted from amount 
                if a-c>=0:
                    dp[a]=min(dp[a],1+dp[a-c])
        return dp[amount] if dp[amount]!=amount+1 else -1


coins=[1,2,5]
amount=11
solution=Solution()
print(solution.coinChange(coins, amount))
