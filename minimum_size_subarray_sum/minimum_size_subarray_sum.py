# https://leetcode.com/problems/minimum-size-subarray-sum/

# 209. Minimum Size Subarray Sum

# Given an array of n positive integers and a positive integer s, 
# find the minimal length of a contiguous subarray of which the sum ≥ s. 
# If there isn't one, return 0 instead.

class Solution:
    def minSubArrayLen(self, s, nums):
        n = len(nums)
        start = 0
        curr_sum = 0
        ans = n + 1

        for i in range(n):
            curr_sum += nums[i]
            while(curr_sum >= s):
                ans = min(ans, i + 1 - start)
                curr_sum -= nums[start]
                start += 1

        return ans if ans != n + 1 else 0
