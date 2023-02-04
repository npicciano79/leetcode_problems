#given a string, s, return the longest palindromic string
"""
--itterates through length of string
--sets left,right pointers checking for even/odd string lengths
--check if pointers are in bounds and string vals at pointers match
--if so, sets resLen to the maximum length of matching characters 
--sets res to palindromic string
--returns res when points are out of bounds
"""

class Solution(object):
    def longestPalindrome(self,s):
        res=''
        resLen=0

        for i in range(len(s)):
            #odd length
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if(r-l+1)>resLen:
                    res=s[l:r+l]
                    resLen=r-l+1
                l-=1
                r+=1
            #even length
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>resLen:
                    res=s[l:r+1]
                    resLen=r-l+1
                l-=1
                r+=1
        return res

s='babad'
solution=Solution()
print(solution.longestPalindrome(s))