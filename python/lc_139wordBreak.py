#139 word break
"""
---given a string(s) and a dictionary of strings wordDict, return true if s can be 
--segmented in a space seperated sequence of one or more dictionary words

"""

class Solution(object):
    def wordBreak(self,s, wordDict):
        
        dp=[False]*(len(s)+1)
        dp[(len(s))]=True

        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                if i+len(w)<=len(s) and s[i:i+len(w)]==w:
                    dp[i]=dp[i+len(w)]
                if dp[i]:
                    break
        return dp[0]
        


s='leetcode'
wordDict=['leet','code']
solution=Solution()
print(solution.wordBreak(s,wordDict))