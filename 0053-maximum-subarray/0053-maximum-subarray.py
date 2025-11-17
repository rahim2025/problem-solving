class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        current_sum =0

        for i in nums:
            current_sum+=i

            if current_sum>max_so_far:
                max_so_far = current_sum
            if current_sum <0:
                current_sum = 0
        return max_so_far