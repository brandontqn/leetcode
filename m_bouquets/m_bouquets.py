 # https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

# Given an integer array bloomDay, an integer m and an integer k.
# We need to make m bouquets. To make a bouquet, you need to use k 
# adjacent flowers from the garden. The garden consists of n flowers, 
# the ith flower will bloom in the bloomDay[i] and then can be used 
# in exactly one bouquet. Return the minimum number of days you need 
# to wait to be able to make m bouquets from the garden. If it is 
# impossible to make m bouquets return -1.

class Solution:
    def minDays(self, bloomDay: [int], m: int, k: int) -> int:
        return -1