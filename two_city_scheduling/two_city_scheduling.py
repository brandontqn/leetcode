# https://leetcode.com/problems/two-city-scheduling/

# 1029. Two City Scheduling

# There are 2N people a company is planning to interview. 
# The cost of flying the i-th person to city A is costs[i][0], 
# and the cost of flying the i-th person to city B is costs[i][1].

# Return the minimum cost to fly every person to a city such that 
# exactly N people arrive in each city.

class Solution:
    def twoCitySchedCost(self, costs):
        return 110