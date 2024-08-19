import heapq

def jump_game(nums):
    # set last element in array as initial target 
    target = len(nums) - 1 
    # traverse array from end to first element in array 
    for i in range(len(nums) - 2, -1, -1):
    # if current index reachable from any preceding index
    # based on value at that index, make index new target 
        if target <= i + nums[i]: 
            target = i 

    # if able to move each current target backward all the 
    # way to first index of array, path found from start to end - return True
    if target == 0:
        return True
    # if you reach first index of array without finding any index 
    # from which current target reachable, return FALSE 
    return False

def rescue_boats(people, limit):
    boats = 0
    # sort people array so that lightest person @ start & heaviest @ end
    people.sort()
    # initialize 2 pointers - left and right @ start and end
    left = 0
    right = len(people) - 1  
    # iterate over people array
    while left <= right: 
        # check if lightest + heaviest < limit  
        if people[left] + people[right] <= limit:   
            # if it is, increment left pointer and decrement right pointer 
            left += 1
        # otherwise, rescue heaviest person alone and decrement right pointer
        right -= 1
            # increment # boats 
        boats += 1
    # return number of boats 
    return boats

def gas_station_journey(gas, cost):
    # calc total gas and total cost from arrays 
    # if total gas less than total cost, return - 1 (cannot complete loop from any station)
    if sum(cost) > sum(gas):
        return -1 
    # otherwise, initialize starting index and current gas to 0
    current_gas, starting_index = 0, 0
    # iterate over each gas station
    for i in range(len(gas)):
        # subtract current element of gas station array from element in cost array with 
        # corresponding index add result to current gas 
        current_gas = current_gas + gas[i] - cost[i]

        # if at any point, current gas becomes less than 0, loop cannot be completed from this index 
        if current_gas < 0:
            current_gas = 0
            starting_index = i + 1 # increment starting index by 1
    return starting_index # return starting index at end of traversal 

def two_city_scheduling(costs):
    # initialize total cost variable to 0
    total_cost = 0
    # sort costs array in ascending order based on difference between cost of traveling 
    # to City A and City B 
    costs.sort(key = lambda x : x[0] - x[1])
    cost_length = len(costs)
    # iterate over costs array 
    for i in range(cost_length // 2):
        # add cost of first half of array to invite to City A 
        # add cost of second half to invite to City B in total cost variable 
        total_cost = total_cost + costs[i][0] + costs[cost_length - i - 1][1]
    # return total cost
    return total_cost

def min_refuel_stops(target, start_fuel, stations): 
    # if start fuel greater than or equal to target, car doesn't need refuel, return 0
    if start_fuel >= target:
        return 0
    # create max heap to store fuel capacities of stations in way that max at top 
    max_fuel_capacities = []
    # initialize variables for loop
    i = 0
    n = len(stations)
    stops = 0
    max_distance = start_fuel
    # iterate over refueling stations until max distance less than target or car not out of fuel 
    while max_distance < target:
        # if car can reach next station from current position, add fuel capacity to max-heap 
        if i < n and stations[i][0] <= max_distance:
            heapq.heappush(max_fuel_capacities, -stations[i][1])
            i += 1
        # if car cannot reach destination after stopping at all fuel stations, return -1 
        elif not max_fuel_capacities:
            return -1 
        # if car cannot reach next fuel station, pop station with highest fuel value from max heap
        # add its fuel to car's tank and increment stops
        else:
            max_distance += -heapq.heappop(max_fuel_capacities)
            stops += 1
    # return number of stops 
    return stops

def jump_game_two(nums):
    # initialize 3 variables
    farthest_jump = 0 # farthest jump
    current_jump = 0 # current jump 
    jumps = 0 # jumps 
    # traverse entire nums array
    for i in range(len(nums) - 1):
        # on each ith iteration, update farthest jump to max of current value 
        # of farthest jump and i + nums[i]
        farthest_jump = max(farthest_jump, i + nums[i])
        # if i equal to current jump, current jump completed, prepare next jump if needed 
        if i == current_jump: 
            # increment jumps
            jumps += 1
            # set current jump to farthest jump
            current_jump = farthest_jump
            if current_jump >= len(nums) - 1:
                break
    return jumps 
        
    
    

def main():
    input = (
              (3, 3, []),
              (59, 14, [[9, 12], [11, 7], [13, 16], [21, 18], [47, 6]]),
              (15, 3, [[2, 5], [3, 1], [6, 3], [12, 6]]),
              (570, 140, [[140, 200], [160, 130], [310, 200], [330, 250]]),
              (1360, 380, [[310, 160], [380, 620], [700, 89], [850, 190],
               [990, 360]])
    )
    num = 1
    for i in input:
        print(num, ".\tStations : ", i[2], sep="")
        print("\tTarget : ", i[0])
        print("\tStarting fuel : ", i[1])
        print("\n\tMinimum number of refueling stops :",
              min_refuel_stops(i[0], i[1], i[2]))
        num += 1
        print("-" * 100, "\n")


if __name__ == "__main__":
    main()
