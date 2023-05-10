#2108 find first palindromic string in array 
"""
---given an array of strings words, return the first palindromic string 
---in the array. if no such strings, return an empty string

"""

class Solution(object):
    def firstPalindrome(self,words):

        #solution 1-uses reverse slice 
        for word in words:
            if word==word[::-1]:
                return word
        
        return ""
    

    

words=["abc","car","ada","racecar","cool"]
solution=Solution()
print(solution.firstPalindrome(words))