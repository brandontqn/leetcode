import math

# Mergesort Algorithm
# Returns a fully sorted array
# Space Complexity: O(1)
# Time Complexity: O(nlogn)
# Inputs:
# `arr`: the unsorted array which we'll be sorting
def mergeSort(arr: [int]):
    if len(arr) < 2:
        return arr

    mid = math.floor(len(arr) / 2)
    left_subarr = mergeSort(arr[:mid])
    right_subarr = mergeSort(arr[mid:])

    return merge(left_subarr, right_subarr)

def merge(left_subarr: [int], right_subarr: [int]):
    if (not len(left_subarr) or not len(right_subarr)):
        return left_subarr or right_subarr

    result = []
    i, j = 0, 0

    while (len(result) < len(left_subarr) + len(right_subarr)):
        if (i == len(left_subarr) or j == len(right_subarr)):
            result.extend(left_subarr[i:] or right_subarr[j:])
            break
        elif (left_subarr[i] < right_subarr[j]):
            result.append(left_subarr[i])
            i += 1
        else:
            result.append(right_subarr[j])
            j += 1

    return result