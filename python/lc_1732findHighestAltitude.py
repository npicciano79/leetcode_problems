#1732 find the highest altitude 
"""
---given an integer array gain of length n where gain[i] is 
---the net gain in the altitude between points i and i+1
---return the highest altitude of a point
"""

class Solution(object):
    def largestAltitude(self,gain):
        alt=[0]*(len(gain)+1)
        for i in range(1,len(gain)+1):
            alt[i]=alt[i-1]+gain[i-1]
        
        return max(alt)




        """
        alt=[]
        alt.append(0)

        count=0
        for g in gain:
            alt.append(g+alt[count])
            count+=1

        return max(alt)
        """


gain=[-5,1,5,0,-7]
solution=Solution()
print(solution.largestAltitude(gain))