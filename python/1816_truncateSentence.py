#1816 truncate Sentences
"""
---given sentence, a list of words seperated by a single space, and integer k
---return truncated s, to only contain k words
"""

class Solution(object):
    def truncateSentence(self,s,k):

        return " ".join([i for i in s.split(' ')[:k]])
    

k=4
s="Hello how are you Contestant"
solution=Solution()
print(solution.truncateSentence(s,k))