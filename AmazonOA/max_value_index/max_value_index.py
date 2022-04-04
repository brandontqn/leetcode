# Write a function that gets an array and returns the index of the maximum element in that array.
#  more than one index contains the maximum value, just return one of those indices with an equal probability.

"""
maxValue = 8
maxValuesIdx = [6]

 0  1  2  3  4  5
[1, 4, 2, 6, 6, 3, 8]

getRandom(maxValues) => 3 || 4
"""

"""
def getRandom(5):
   => returns random # from 0-4 
"""

def getMaxValueIndex(nums):
    maxValue = float('-inf')
    maxValuesIdx = []
    
    n = len(nums)
    
    for i in range(n):
        if nums[i] == maxValue:
            maxValuesIdx.append(i)
        elif nums[i] > maxValue:
            maxValue = nums[i]
            maxValuesIdx = [i]
           
    idx = getRandom(len(maxValuesIdx)) 
    return maxValuesIdx[idx]
    
# O(1) space
# [5,5,5,5]

"""
maxValue = 5
maxValueIdx = 0
n = 4
1/3 * 3/4  = 1/4

"""

def getMaxValueIndexV2(nums):
    maxValue = float('-inf')
    maxValueIdx = None
    count = 0
    
    n = len(nums)
    
    for i in range(n):
        if nums[i] == maxValue:
            count += 1
            shouldKeepCurrentMaxVal = getRandom(count)
            if shouldKeepCurrentMaxVal == 0:
                maxValueIdx = i
            else:
                # keep existing value
                continue
        elif nums[i] > maxValue:
            maxValue = nums[i]
            maxValueIdx = i
            count = 1
           
    return maxValueIdx