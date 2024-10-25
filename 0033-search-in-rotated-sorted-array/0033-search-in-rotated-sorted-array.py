def pivot(arr):
    start =0
    end = len(arr)-1

    while(start<end):
        mid = start + (end-start)//2
        if(arr[mid]>=arr[0]):
            start = mid+1
        else:
            end = mid
    return start

def binarySearch(arr,target,start,end):
    while(start<=end):
        mid = start + (end-start)//2
        if(arr[mid]==target):
            return mid
        elif(arr[mid]>target):
            end = mid-1
        else:
            start= mid+1
            
    return -1


class Solution:
    def search(self, nums, target) :
        value = pivot(nums)
        if(nums[value]<= target <= nums[len(nums)-1]):
            return binarySearch(nums,target,value,len(nums)-1)
        else:
            return binarySearch(nums,target,0,value-1)