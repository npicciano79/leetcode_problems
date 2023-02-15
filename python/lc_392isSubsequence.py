#392 is subsequence
"""
--given 2 strings s and t, return true if s is a subsequence 
--return false if otherwise 
"""

class Solution(object):
    def isSubsequence(self,s,t):
        i,j=0,0

        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i+=1
            j+=1
        
        return True if i==len(s) else False 

s='abc'
t='ahbgdc'
solution=Solution()
print(solution.isSubsequence(s,t))