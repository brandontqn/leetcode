import math

# Binary Search Algorithm
# Returns the index of the given `target` number or -1 if not found.
# Space Complexity: O(1), we only store three variables [left, right, mid]
# Time Complexity: O(logn) where `n` is the length of the length of the array
# Inputs:
# `target`: the integer the function will look for
# `arr`: the array from which we will search for `target`, must be sorted
def binarySearch(arr: [int], target: int) -> int:
    # return iterativeBinarySearch(arr, target)
    return recursiveBinarySearch(arr, target, 0, len(arr) - 1)
                
def iterativeBinarySearch(arr: [int], target: int) -> int:
    n = len(arr)
    left, right = 0, n - 1
    while left <= right:
        if (left == right):
            if (arr[left] == target):
                return left
            else:
                return -1
        else:
            mid = left + math.floor((right - left) / 2)
            if (arr[mid] == target):
                return mid
            elif (arr[mid] < target):
                left = mid + 1
            else:
                right = mid - 1

def recursiveBinarySearch(arr: [int], target: int, left: int, right: int) -> int:
    if left > right:
        return -1

    mid = left + math.floor((right - left) / 2)
    if (arr[mid] == target):
        return mid
    elif (arr[mid] < target):
        return recursiveBinarySearch(arr, target, mid + 1, right)
    else:
        return recursiveBinarySearch(arr, target, left, mid - 1)