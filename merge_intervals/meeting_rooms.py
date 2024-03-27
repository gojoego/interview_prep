import heapq

def find_sets(intervals):
    if not intervals:
        return 0
    
    # sort intervals based on their start times 
    intervals.sort(key=lambda x: x[0])
    
    # use min-heap to store end times of ongoing meetings 
    rooms = []
    
    # add end time of first meeting to min-heap
    heapq.heappush(rooms, intervals[0][1])
    
    # iterate through remaining intervals 
    for interval in intervals[1:]:
        # if start time of current meeting later than end time of any ongoing meeting, remove from min-heap b/c no longer ongoing 
        if interval[0] >= rooms[0]:
            heapq.heappop(rooms)
        
        # add end time of current meeting to min-heap 
        heapq.heappush(rooms, interval[1])
    
    return len(rooms) # size of min-heap reps min number of meeting rooms required 