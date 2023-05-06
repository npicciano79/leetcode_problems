#2418 sort the people
"""
---given an array of strings names, and an array heights
---that consist of distinct positive integers, both arrays 
---are of length n, for each index i, names[i] and height[i]
---denote the name and heigh of the ith person
---return names sorted in decending order by the peoples heights
"""

class Solution(object):
    def sortPeople(self,names,heights):
        res=[]
        while len(res)!=len(names):
            tempMaxHeight=max(heights)
            res.append(names[heights.index(tempMaxHeight)])
            heights[heights.index(tempMaxHeight)]=float('-inf')
        
        return res
    
names = ["Mary","John","Emma"]
heights = [180,165,170]
solution=Solution()
print(solution.sortPeople(names,heights))