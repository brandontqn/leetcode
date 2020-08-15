import math

# Insertionsort Algorithm
# Returns a fully sorted array
# Space Complexity: O(1)
# Time Complexity: O(n^2)
# Inputs:
# `arr`: the unsorted array which we'll be sorting
def insertionSort(arr: [int]):
    # return iterativeInsertionSort(arr)
    return binaryInsertionSort(arr)

def iterativeInsertionSort(arr: [int]):
    for i in range(1, len(arr)):
        target_element = arr[i]
        j = i - 1
        while (j >= 0 and target_element < arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = target_element
    return arr

def binaryInsertionSort(arr: [int]):
    for i in range(1, len(arr)):
        target_value = arr[i]
        target_idx = binarySearch(target_value, arr[:i])
        arr = arr[:target_idx] + [target_value] + arr[target_idx:i] + arr[i+1:]
    return arr

def binarySearch(target: int, arr: [int]) -> int:
    n = len(arr)
    left, right = 0, n - 1
    while left <= right:
        if (left == right):
            if (arr[left] <= target):
                return left + 1
            else:
                return left
        else:
            mid = left + math.floor((right - left) / 2)
            if (arr[mid] == target):
                return mid
            elif (arr[mid] < target):
                left = mid + 1
            else:
                right = mid - 1
    return left