class Solution:
    def mySqrt(self, x):
        start = 0
        end = x
        ans = -1
        while(start<=end):
            mid = start + (end-start)//2
            sqr = mid*mid
            if(sqr == x):
                return mid
            elif(sqr > x):
                end = mid-1
            else:
                ans = mid
                start = mid+1
        return ans
