# https://leetcode.com/problems/contiguous-array/

# Given a binary array, find the maximum length 
# of a contiguous subarray with equal number of 0 and 1.

class Solution:
    def findMaxLength(self, nums: [int]) -> int:
        hashmap = {}
        result = 0
        count = 0        

        hashmap[0] = -1
        for idx, val in enumerate(nums):
            if val == 0:
                count -= 1
            else:
                count += 1

            if count in hashmap:
                subarr_length = idx - hashmap[count]
                if subarr_length >= result:
                    result = subarr_length
            else:
                hashmap[count] = idx

        return result