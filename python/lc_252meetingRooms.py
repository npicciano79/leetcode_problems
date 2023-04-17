#252 meeting rooms
"""
---Given an array of meeting time intervals where intervals[i]=[start,end]
---determine if a person could attend all meetings
"""

class Solution(object):
    def canAttendMeetings(self,intervals):
        length=len(intervals)

        for i in range(length):
            for j in range(i+1,length):
                tempSetJ=set(range(intervals[j][0],intervals[j][1]))
                tempSetI=set(range(intervals[i][0],intervals[i][1]))

                if not tempSetI.isdisjoint(tempSetJ):
                    return False
        return True


intervals=[[0,30],[5,10],[15,20]]
intervals2=[[7,10],[2,4]]

solution=Solution()
print(solution.canAttendMeetings(intervals2))

