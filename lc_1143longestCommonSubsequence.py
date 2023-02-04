#1143 longest common subsequence 
"""
---given 2 strings, text1 and test2, return the length of the 
---longest common subsequence, return 0 if none
"""

class Solution(object):
    def longestCommonSubsequence(self,text1,text2):
        dp=[[0 for j in range(len(text2)+1)]for i in range(len(text1)+1)]
        
        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                if text1[i]==text2[j]:
                    dp=[i][j]=1+dp[i+1][j+1]
                else:
                    dp[i][j]=max(dp[i][j+1],dp[i+1][j])
        return dp[0][0]
        


text1='abcde'
text2='ace'
solution=Solution()
print(solution.longestCommonSubsequence(text1,text2))