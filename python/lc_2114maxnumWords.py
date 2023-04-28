#2114 maximum number of words in sentence 
"""
---a sentence is a list of words separated by a single space
---given an array of strings, sentences where each sentences[i]
---represents a single sentence, return the maximum number of words that appear 
---in a single sentence
"""

class Solution(object):
    def mostWordsFound(self,sentences):
        wordCount=0
        for s in sentences:
            tempCount=0
            for word in s.split(' '):
                tempCount+=1
                wordCount=max(wordCount, tempCount)

        return wordCount
    
sentences=["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
solution=Solution()
print(solution.mostWordsFound(sentences))