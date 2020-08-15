import sys
sys.path.append('../')
import binary_search

# Insertionsort Algorithm
# Returns a fully sorted array
# Space Complexity: O(1)
# Time Complexity: O(n^2)
# Inputs:
# `arr`: the unsorted array which we'll be sorting
def insertionSort(arr: [int]):
    regularInsertionSort(arr)

def iterativeInsertionSort(arr: [int]):
    for i in range(1, len(arr)):
        target_element = arr[i]
        j = i - 1
        while (j >= 0 and target_element < arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = target_element

def binaryInsertionSort():
    return