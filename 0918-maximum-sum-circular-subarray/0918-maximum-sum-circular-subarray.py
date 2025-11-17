class Solution:
    def maxSubArray(self,nums):
        max_so_far = nums[0]
        current_sum =0

        for i in nums:
            current_sum+=i

            if current_sum>max_so_far:
                max_so_far = current_sum
            if current_sum <0:
                current_sum = 0
        return max_so_far
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_normal_array = self.maxSubArray(nums)
        neg_nums = [n * -1 for n in nums]
        minimun_sum = self.maxSubArray(neg_nums)
        total_sum = sum(nums)
        max_circular_array = (total_sum)-(minimun_sum*(-1)) 
        
        if(max_circular_array ==0):
            return max_normal_array
        
        max_sum = max(max_normal_array,max_circular_array)
        return max_sum



        