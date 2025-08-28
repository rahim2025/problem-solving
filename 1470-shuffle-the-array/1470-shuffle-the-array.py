class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        new_array =[0]*len(nums)
        i = 0
        j=0
        while(i<n):
            new_array[j] = nums[i]
            new_array[j+1] = nums[i+n]
            j+=2
            i+=1
        return new_array
        