def merge_intervals(intervals):
    if not intervals:
        return None
    result = []
    # copy first interval from input list to output list 
    result.append([intervals[0][0], intervals[0][1]])
    # loop to traverse remaining intervals 
    for i in range(1, len(intervals)):
        last_added_interval = result[len(result) - 1]
        current_start = intervals[i][0] # start time of current input interval 
        current_end = intervals[i][1] # end time of current input interval 
        previous_end = last_added_interval[1] # track end time of last interval in output list 
        
        # check each interval of input list against last interval of output list 
        if current_start <= previous_end: # if current input interval overlaps with last interval 
            # merge 2 intervals and replace last interval of output with newly merged interval 
            result[-1][1] = max(current_end, previous_end)
        else: 
            # otherwise add input interval to output 
            result.append([current_start, current_end])
    return result

def main():
    
    all_intervals = [
    [[1, 5], [3, 7], [4, 6]],
    [[1, 5], [4, 6], [6, 8], [11, 15]],
    [[3, 7], [6, 8], [10, 12], [11, 15]],
    [[1, 5]],
    [[1, 9], [3, 8], [4, 4]],
    [[1, 2], [3, 4], [8, 8]],
    [[1, 5], [1, 3]],
    [[1, 5], [6, 9]],
    [[0, 0], [1, 18], [1, 3]]
    ]

    for i in range(len(all_intervals)):
        print(i + 1, ". Intervals to merge: ", all_intervals[i], sep="")
        result = merge_intervals(all_intervals[i])
        print("   Merged intervals:\t", result)
        print("-"*100)

if __name__ == '__main__':
    main()