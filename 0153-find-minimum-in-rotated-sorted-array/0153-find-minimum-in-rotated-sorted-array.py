def pivot(arr):
    start =0
    end = len(arr)-1

    while(start<end):
        mid = start + (end-start)//2
        if(arr[mid]>=arr[0]):
            start = mid+1
        else:
            end = mid
    if(arr[start]>arr[0]):
        return arr[0]
    else:
        return arr[start]


class Solution:
    def findMin(self, nums):
        return pivot(nums)


        