"""
Given 
- a list of buildings where buildings[i] is the number of people in that building,
- a list of router locations where routerLocations[i] is the index (1-indexed) location of a router corresponding to the building locations
- a list of router ranges where routerRanges[i] is the distance +/- from routerLocation[i]

Return the number of buildings which are fully covered by the routers. A building is fully covered if and only if there are X routers covering X people for that building
"""


def removeCoveredIntervals(buildings, routerLocations, routerRanges):
    intervals = []
    n = len(buildings)
    k = len(routerLocations)
    for i in range(k):
        begin = routerLocations[i] - 1 - routerRanges[i] if routerLocations[i] - 1 - routerRanges[i] >= 0 else 0
        end = routerLocations[i] - 1 + routerRanges[i] if routerLocations[i] - 1 + routerRanges[i] < n else n - 1
        intervals.append((begin, end))

    covered_buildings = n

    for building_location, num_people in enumerate(buildings):
        if num_people == 0:
            covered_buildings -= 1
            continue

        interval_idx = 0
        while num_people > 0 and interval_idx < k:
            curr_begin, curr_end = intervals[interval_idx]
            if building_location >= curr_begin and building_location <= curr_end:
                num_people -= 1
                if num_people == 0:
                    covered_buildings -= 1
            interval_idx += 1

    return covered_buildings

def main():
    buildings = [3, 1, 1]
    routerLocations = [2, 1]
    routerRanges = [1, 0]
    result = removeCoveredIntervals(buildings, routerLocations, routerRanges)
    print(result)

if __name__ == "__main__":
    main()