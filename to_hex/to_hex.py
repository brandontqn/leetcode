# https://leetcode.com/problems/convert-a-number-to-hexadecimal/

# 405. Convert a Number to Hexadecimal

# Given an integer, write an algorithm to convert it to hexadecimal.
# For negative integer, two’s complement method is used.
# Note:
# All letters in hexadecimal (a-f) must be in lowercase.
# The hexadecimal string must not contain extra leading 0s. If the number is zero,
# it is represented by a single zero character '0'; otherwise, the first character
# in the hexadecimal string will not be the zero character.
# The given number is guaranteed to fit within the range of a 32-bit signed integer.
# You must not use any method provided by the library which converts/formats
# the number to hex directly.

import math
class Solution:
    hexs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        
    def toHex(self, num: int) -> str:
        result = ''

        if (num == 0): return '0'
        elif (num == 1): return '1'
        elif (num < 0):
            highest_32_pos_num = 4294967295 # ffff_ffff
            return self.toHex(highest_32_pos_num - abs(num) + 1 )

        while (num > 0):
            result = self.hexs[num % 16] + result
            num //= 16

        return result