# https://leetcode.com/problems/power-of-three/submissions/

# Given an integer, write a function to determine if it is a power of three.
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        power = 0
        CONST_THREE = 3

        while(CONST_THREE**power < n):
            power += 1

        if CONST_THREE**power == n:
            return True
        else:
            return False