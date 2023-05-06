#1534 count good triplets
"""
---given an array of integers arr and 3 integers 
---a,b,c.  You need to find the number of good triplets. 
---a triplet (arr[i], arr[j], arr[k]) is good if the following 
---conditions are true:
0 <= i < j < k < arr.length
|arr[i] - arr[j]| <= a
|arr[j] - arr[k]| <= b
|arr[i] - arr[k]| <= c
---return the number of good triplets
"""

"""
---runtime 321ms, beats 80.18% memory: 22.2mb beats 7.21%

"""

class Solution(object):
    def countGoodTriplets(self,arr,a,b,c):
        ans=[]
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if abs(arr[i]-arr[j])<=a:
                    for k in range(j+1,len(arr)):
                        if abs(arr[j]-arr[k])<=b:
                            if abs(arr[i]-arr[k])<=c:
                                ans.append((arr[i],arr[j],arr[k]))
                        else:
                            continue
                else:
                    continue
        return len(ans)
    
arr = [3,0,1,1,9,7]
a = 7
b = 2
c = 3
solution=Solution()
print(solution.countGoodTriplets(arr,a,b,c))