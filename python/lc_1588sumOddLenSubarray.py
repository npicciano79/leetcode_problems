#1588 sum of all odd length subarray
"""
---given an array of positive integers arr, 
---return the sum of all possible odd-length subarrays of arr
---subarray is a contiguous subsequence of the array
"""


class Solution(object):
    def sumOddLengthSubarrays(self,arr):
        arrOddSum=0
        if len(arr)%2!=0 and len(arr)!=1:
            #sum of total array and each element
            arrOddSum=(sum(arr))*2
        else:
            #sum of each element
            arrOddSum=sum(arr)

        counter=2
        
        while counter<len(arr)-1 and len(arr)>1:
            print(counter)
            arrayEnd=counter
            start=0
            while arrayEnd<=len(arr)-1:
                arrOddSum+=sum(arr[start:arrayEnd+1])
                print(arrOddSum)
                start+=1
                arrayEnd+=1
            counter+=2
            print('counter incremented')

        return arrOddSum



arr=[1,4,2,5,3]
solution=Solution()
print(solution.sumOddLengthSubarrays(arr))