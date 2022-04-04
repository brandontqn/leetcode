"""
Given
- a maximum distance that a plane can travel
- a list of forward routes where forwardRoutes[i] = (route_id, distance)
- a list of return routes where returnRoutes[i] = (route_id, distance)

Return a list of (forwardRouteId, returnRouteId) tuples where the total route distance is optimal.
"""

def optimalAircraftRoutes(maxDistance, forwardRoutes, returnRoutes):
    n = len(forwardRoutes)

    if n == 0:
        return [[]]

    sorted_forward_routes = sorted(forwardRoutes, key=lambda route:route[1])
    sorted_return_routes = sorted(returnRoutes, key=lambda route:route[1])
    optimal_distance = float("-inf")
    optimal_distance_routes = []

    for forward_id, forward_distance in sorted_forward_routes:
        return_min_idx, return_max_idx = 0, n - 1
        while return_min_idx <= return_max_idx:
            return_idx = (return_min_idx + return_max_idx) // 2
            return_id = sorted_return_routes[return_idx][0]
            return_distance = sorted_return_routes[return_idx][1]
            
            curr_distance = forward_distance + return_distance
            if curr_distance > optimal_distance and curr_distance <= maxDistance:
                optimal_distance = curr_distance
                optimal_distance_routes = [(forward_id, return_id)]
                return_min_idx = return_idx + 1
            elif curr_distance > maxDistance:
                return_max_idx = return_idx - 1
            elif curr_distance == optimal_distance:
                optimal_distance_routes.append((forward_id, return_id))
                return_min_idx = return_idx + 1
            else: # curr_distance < optimal_distance
                return_min_idx = return_idx + 1

    return optimal_distance_routes if optimal_distance_routes else [[]]


def main():
    maxDistance = 9000
    forwardRoutes = [(1, 2000), (2, 4000), (3, 5000)]
    returnRoutes = [(1, 4000), (2, 1000), (3, 4000), (4, 4950)]
    result = optimalAircraftRoutes(maxDistance, forwardRoutes, returnRoutes)
    print(result)

if __name__ == "__main__":
    main()