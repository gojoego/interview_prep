def insert_interval(existing_intervals, new_interval):
    if not existing_intervals:
        return [new_interval] if new_interval else None
    
    if not new_interval:
        return existing_intervals
    
    # read start and end times of new interval into separate variables 
    new_start, new_end = new_interval[0], new_interval[1]

    # initialize iterating variables for while loops and output array 
    result = []
    i = 0
    n = len(existing_intervals)
    
    # append all intervals that start before new interval to output list 
    while i < n and existing_intervals[i][1] < new_start:
        result.append(existing_intervals[i])
        i += 1
    
    # if new interval starts after end of last added interval, append new interval to output
    if not result or result[-1][1] < new_start:
        result.append(new_interval)
    else: # otherwise merge intervals
        result[-1][1] = max(result[-1][1], new_end)
        
    while i < n:
        ei = existing_intervals[i]
        start, end = ei[0], ei[1]
        if result[-1][1] < start:
            result.append(ei)
        else:
            result[-1][1] = max(result[-1][1], end)
        i += 1
    return result
            
def main():
    new_interval = [[5, 7], [8, 9], [10, 12], [1, 3], [1, 10]]
    existing_intervals = [
        [[1, 2], [3, 5], [6, 8]],
        [[1, 3], [5, 7], [10, 12]],
        [[8, 10], [12, 15]],
        [[5, 7], [8, 9]],
        [[3, 5]]
    ]
    
    for i in range(len(new_interval)):
        print(i + 1, ".\tExiting intervals: ", existing_intervals[i], sep="")
        print("\tNew interval: ", new_interval[i], sep="")
        output = insert_interval(existing_intervals[i], new_interval[i])
        print("\tUpdated intervals: ", output, sep = "")
        print("-"*100)


if __name__ == "__main__":
    main()

# time O(n), space O(1)