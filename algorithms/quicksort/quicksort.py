# Quicksort Algorithm
# Returns a fully sorted array
# Space Complexity: O(1)
# Time Complexity: O(nlogn)
# Inputs:
# `arr`: the unsorted array which we'll be sorting
def quickSort(arr: [int]):
    low, high = 0, len(arr) - 1
    quickSort_helper(arr, low, high)

def quickSort_helper(arr: [int], low: int, high: int):
    if (low < high):
        pivot_idx = partition(arr, low, high)
        quickSort_helper(arr, low, pivot_idx - 1)
        quickSort_helper(arr, pivot_idx + 1, high)

def partition(arr: [int], low: int, high: int) -> int:
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if (arr[j] <= pivot):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1