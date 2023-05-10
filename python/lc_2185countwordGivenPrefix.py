#2185 count words with a given prefix
"""
---given an array of strings words and a string perf
---return the number of string in words that contain perf as a prefix

"""

class Solution(object):
    def prefixCount(self,words,pref):
        count=0
        words.sort()
        prefixLength=len(pref)

        for word in words:
            if word.startswith(pref):
                count+=1
        
        return count

words = ["pay","attention","practice","attend"]
pref='at'
solution=Solution()
print(solution.prefixCount(words,pref))
