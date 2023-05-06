#2418 sort the people
"""
---given an array of strings names, and an array heights
---that consist of distinct positive integers, both arrays 
---are of length n, for each index i, names[i] and height[i]
---denote the name and heigh of the ith person
---return names sorted in decending order by the peoples heights
"""

"""
---original solution: runtime: 607ms beats 14% memory 13.9 beats 95%
---updated solution : runtine 206ms beates 20% memory 13.9 beats 95%
"""

class Solution(object):
    def sortPeople(self,names,heights):
        while heights:
            heightMaxIndex=heights.index(max(heights))
            #pop previous max from heights
            heights.pop(heightMaxIndex)
            #heights[heightMaxIndex]=float('-inf')
            #print(heightMaxIndex)
            names.append(names.pop(heightMaxIndex))
            #print(names)
            
        return names

        """
        res=[]
        while len(res)!=len(names):
            tempMaxHeight=max(heights)
            res.append(names[heights.index(tempMaxHeight)])
            heights[heights.index(tempMaxHeight)]=float('-inf')
        
        return res
        """
    
names = ["Mary","John","Emma"]
heights = [180,165,170]
solution=Solution()
print(solution.sortPeople(names,heights))