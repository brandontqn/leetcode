# https://leetcode.com/problems/two-city-scheduling/

# 1029. Two City Scheduling

# There are 2N people a company is planning to interview. 
# The cost of flying the i-th person to city A is costs[i][0], 
# and the cost of flying the i-th person to city B is costs[i][1].

# Return the minimum cost to fly every person to a city such that 
# exactly N people arrive in each city.

class Solution:
    def twoCitySchedCost(self, costs):
        n = len(costs)
        result = -1

        diff_arr = []
        for i in range(n):
            diff = costs[i][0] - costs[i][1]
            diff_arr += [(i, diff)]

        self.qsort(diff_arr, 0, n-1)
        city_a = [costs[x[0]][0] for x in diff_arr[:int(n/2)]]
        city_b = [costs[x[0]][1] for x in diff_arr[int(n/2):]]
        result = sum(city_a) + sum(city_b)

        return result

    def qsort(self, arr, left, right):
        if left >= right: return

        pivot = arr[right][1]
        pivot_position = left

        for i in range(left, right+1):
            if(arr[i][1] <= pivot):
                tmp = arr[i]
                arr[i] = arr[pivot_position]
                arr[pivot_position] = tmp
                pivot_position += 1

        self.qsort(arr, left, pivot_position-2)
        self.qsort(arr, pivot_position, right)