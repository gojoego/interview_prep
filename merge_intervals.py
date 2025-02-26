'''
merge intervals pattern
- deals with problems involving overlapping intervals
- each interval represented by start and end time 
- involves merging intersecting intervals, inserting new intervals into 
  existing sets or determining min number of intervals needed to cover range 
- common problems solved using pattern: event scheduling, resource allocation, time slot 
  consideration

examples: 
1. merge intervals 
2. meeting rooms
3. schedule 3 interviews for 1 interviewer in a day 
4. for football tournament, find durations more than 1 game being played 

does your problem match this pattern? yes, if...
- array of intervals 
- overlapping intervals 

real-world problems
- display busy schedule 
- schedule a new meeting
- task scheduling in operating systems 
'''

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end 
        self.closed = True # closed by default 
        
    def set_closed(self, closed):
        self.closed = closed
        
    def __str__(self):
        return "[" + str(self.start) + ", " + str(self.end) + "]" \
            if self.closed else \
                "(" + str(self.start) + ", " + str(self.end) + ")"
  
'''
Merge Intervals

statement: we are given an array of closed intervals, intervals, where each 
interval has a start time and an end time; input array is sorted with respect 
to the start times of each interval. 

for example, intervals = [ [1,4], [3,6], [7,9] ] is sorted in terms of start times 
1, 3, and 7

your task is to merge the overlapping intervals and return a new output array consisting 
of only the non-overlapping intervals

algorithm: merge intervals pattern w simple linear scan to merge overlapping intervals;
declare output list and add 1st interval; traverse remaining intervals and check for 
overlap; update interval in output list if overlap; otherwise add current interval to 
output; +1 intervals in output -> always use last interval to compare 

'''

def merge_intervals(intervals):
    # return None for empty lists 
    if not intervals:
        return None

    # copy 1st interval to output
    output = []
    output.append([intervals[0][0], intervals[0][1]])
    
    # loop to iterate over each interval, except 1st 
    for i in range(1, len(intervals)):
        last_added_interval = output[len(output) - 1]
  
        current_start = intervals[i][0]
        current_end = intervals[i][1]
  
        # end time of last interval present in output list 
        previous_end = last_added_interval[1]

        # overlapping condition 
        if current_start <= previous_end:
            output[-1][1] = max(current_end, previous_end)
        else:
            output.append([current_start, current_end])
        
    return output

''' 

naive solution to merge intervals: start from first interval and check if any other interval overlaps, 
merge other interval into first, remove other from list 

time O(n ^ 2), space O(1)

'''
def naive_merge_intervals(intervals):
    i = 0 
    while i < len(intervals):
        j = i + 1 
        while j < len(intervals):
            # check intervals for overlap
            if intervals[j][0] <= intervals[i][1]:
                # merging 
                intervals[i][1] = max(intervals[i][1], intervals[j][1])

                intervals.pop(j)
            else: 
                j += 1 # moving forward if there's no merge 

        i += 1 # moving on to next interval 

    return intervals

'''
Insert Interval

statement: given a sorted list of nonoverlapping intervals and a new interval, 
your task is to insert the new interval into the correct position while ensuring 
that the resulting list of intervals remains sorted and nonoverlapping; each 
interval is a pair of nonnegative numbers, the first being the start time and the 
second being the end time of the interval

algorithm:
- append intervals occurring before new interval to output list until hitting interval
  that starts after starting point of new interval
- overlap between last interval in output list and new interval -> merge by updating 
  end value of last interval, otherwise append new interval to output list 
- continue iterating through remaining intervals and merge overlapping intervals with 
  last interval in output list 
- return final output list containing merged intervals 

time O(n) where n = number of intervals in input list, space O(1)
'''
def insert_interval(existing_intervals, new_interval):
    output = []
    
    # read start/end time of new interval 
    new_start, new_end = new_interval
    
    # initialize variables for iteration
    i = 0
    n = len(existing_intervals)
    
    # iterate through existing intervals
    while i < n and existing_intervals[i][0] < new_start:
        # append intervals occurring before new interval to output
        output.append(existing_intervals[i])
        i += 1
        
    # merge new interval w last interval if overlap, else add separately
    if not output or output[-1][1] < new_start:
        output.append(new_interval)
    else:
        output[-1][1] = max(output[-1][1], new_end)

    # copy any remaining intervals to output list, merging overlapping intervals 
    while i < n:
        start, end = existing_intervals[i]
        if output[-1][1] < start:
            output.append(existing_intervals[i])
        else:
            output[-1][1] = max(output[-1][1], end)
        i += 1
        
    return output

'''
naive approach to insert interval: iterate and check for overlaps, merge new with existing if so,
append to new interval if no overlap, sort list based on start times of intervals to ensure 
correct order of intervals

time O(nlogn), space O(n)
'''

def naive_insert_interval(existing_intervals, new_interval):
    intervals = existing_intervals[:]
    intervals.append(new_interval)
    
    # 1: sort intervals based on time 
    intervals.sort(key=lambda x: x[0])
    
    # 2: merge overlapping intervals
    merged = [intervals[0]]
    
    for i in range(1, len(intervals)):
        previous_start, previous_end = merged[-1]
        current_start, current_end = intervals[i]
        
        if previous_end >= current_start:
            merged[-1] = [previous_start, max(previous_end, current_end)]
        else: 
            merged.append([current_start, current_end])
    
    return merged

'''
Interval List Intersections

statement: for two lists of closed intervals given as input, interval_list_a and interval_list_b, 
where each interval has its own start and end time, write a function that returns the intersection 
of the two interval lists

for example, the intersection of [3,8] and [5,10] is [5,8]

algorithm: 2 key advantages -> sorted intervals lists, result requires comparing intervals 
to check for overlap; iterate through both lists simultaneously to find intersections;
compare current intervalsw from both lists and examine endpoints to find intersections; 
add intersection to result list; adjust pointers based on positions of endpoints to cover all 
possible intersections

time O(n + m) where n = number meetings a, m = b, space O(1)
'''

def intervals_intersection(interval_list_a, interval_list_b):
    intersections = []
    
    # 2 pointers i/j at lists starts, i for a, j for b 
    i = j = 0 
    
    while i < len(interval_list_a) and j < len(interval_list_b):
        # find lastest start and earliest ending for a at i and b at j 
        start = max(interval_list_a[i][0], interval_list_b[j][0])
        end = min(interval_list_a[i][1], interval_list_b[j][1])
        
        # if latest starting time less than / equal to earliest end, store as intersection 
        if start <= end:
            intersections.append([start, end])
        
        
        # increment pointer i/j w smaller end time 
        if interval_list_a[i][1] < interval_list_b[j][1]:
            i += 1
        else:
            j += 1 
    
    # return list of intersections 
    return intersections

'''
naive approach for Interval List Intersections: use a nested loop for finding intersecting intervals, 
outer loop will iterate for every interval in interval_list_a and the inner loop will search for any 
intersecting interval in the interval_list_b; if such an interval exists, we add it to the 
intersections list

time O(n * m) where n = length of intervals A and m = length of intervals B, space O(1)
'''

def naive_intervals_intersection(interval_list_a, interval_list_b):
    intersections = []
    for a in interval_list_a:
        for b in interval_list_b:
            start = max(a[0], b[0])
            end = min(a[1], b[1])
            
            if start <= end:
                intersections.append([start, end])
    return intersections

'''
Employee Free Time

statement: you're given a list containing the schedules of multiple employees; each person's 
schedule is a list of non-overlapping intervals in sorted order; an interval is specified with 
the start and end time, both being positive integers; your task is to find the list of finite 
intervals representing the free time for all the employees

note: the common free intervals are calculated between the earliest start time and the latest 
end time of all meetings across all employees

algorithm: merging overlapping intervals of employees and identifying free time gaps between merged
intervals; use min heap to array intervals based on start and sort accordingly; min heap pops will
be earliest available interval; merge intervals as popped; if current start time more than merged
interval end -> gap / free period; after each gap, restart process 

time O(mlog(n)), space O(n) where m = total intervals and n = number of employees and m = number of
intervals 

'''
import heapq

def employee_free_time(schedule):  
    # initialize heap 
    min_heap = []
    # push first interval of each employ onto heap: start, index value and 0 
    for i in range(len(schedule)):
        min_heap.append((schedule[i][0].start, i, 0))
    
    # create heap from array elements 
    heapq.heapify(min_heap)
    
    result = []
    
    # set previous interval as start time of first interval 
    previous = schedule[min_heap[0][1]][min_heap[0][2]].start 
    
    # repeatedly pop smallest interval from heap and compare w previous interval 
    while min_heap:
        _, i, j = heapq.heappop(min_heap)
        
        # select interval 
        interval = schedule[i][j]
        
        # if selected start time greater than previous -> free interval, add to result 
        if interval.start > previous:
            result.append(Interval(previous, interval.start))
        
        # update previous as max of previous and current end times 
        previous = max(previous, interval.end)
        
        # push additional intervals of current employee onto heap if it exists 
        if j + 1 < len(schedule[i]):
            heapq.heappush(min_heap, (schedule[i][j + 1].start, i , j + 1))
        
    return result

'''
Task Scheduler

statement: given a character array tasks, where each character represents a unique task and a 
positive integer n that represents the cooling period between any two identical tasks, find the 
minimum number of time units the CPU will need to complete all the given tasks; each task requires 
one unit to perform, and the CPU must wait for at least n units of time before it can repeat the 
same task; during the cooling period, the CPU can perform other tasks or remain idle

algorithm: minimize idle time by strategically scheduling tasks based on frequency; 
start with most frequent tasks -> create structure that maximizes idle time; reduce 
idle time by incorporating less frequent tasks within cooling periods 

max possible idle time = (max freq - 1) * cooling period 
max freq = highest freq of task in sequence
cooling time = specified interval between identical tasks 

idle time -= min(max freq - 1, current task frequency)
current task frequency = frequency of task currently being processed

total time required = length of tasks + idle time 

time O(n) where n = total number of tasks, space O(1)
'''

def least_time(tasks, n):
    # initialize dictionary to store frequency of tasks 
    frequencies = {}
    
    # count and store frequencies of all tasks 
    for task in tasks:
        frequencies[task] = frequencies.get(task, 0) + 1
    
    # sort tasks based on frequencies
    frequencies = dict(sorted(frequencies.items(), key = lambda x:x[1]))
    
    # store max frequency
    max_frequency = frequencies.popitem()[1]
    
    # compute max possible idle time 
    idle_time = (max_frequency - 1) * n 
    
    # start scheduling tasks in desc order of their freqs / iterate over frequencies 
    while frequencies and idle_time > 0:
        # compute idle time 
        idle_time -= min(max_frequency - 1, frequencies.popitem()[1])
    
    idle_time = max(0, idle_time)
        
    # calculate total time by adding number of tasks and idle time 
    return len(tasks) + idle_time

'''
Meeting Rooms II

statement: we are given an input array of meeting time intervals, intervals, 
where each interval has a start time and an end time; your task is to find the 
minimum number of meeting rooms required to hold these meetings

an important thing to note here is that the specified end time for 
each meeting is exclusive

algorithm: first sort the meeting intervals by start time; use a min-heap to track 
meeting end times; iterate through the intervals, checking if the earliest ending 
meeting (top of the heap) has finished before the current meeting starts —> if so, 
remove that meeting from the heap; current meeting's end time is then added to the 
heap, and the heap's size at the end represents the minimum number of meeting rooms
required

time O(n*log(n)), space O(n)
'''
import heapq

def find_sets(intervals):
    if not intervals:
        return 0
    
    # sort given input intervals with respect to their start times 
    intervals.sort(key = lambda x : x[0])
    
    # initialize min heap and push end time of first interval onto it 
    min_heap = []
    heapq.heappush(min_heap, intervals[0][1])
    
    # loop over remaining intervals 
    for i in range(1, len(intervals)):
        # compare start time of current interval w all heap end times 
        start, end = intervals[i]
        
        # if earliest end time so far (root of heap) occurs before start time of current interval
        if min_heap[0] <= start:
            # remove earliest interval from heap 
            heapq.heappop(min_heap)
        
        # push current interval onto heap 
        heapq.heappush(min_heap, end)
    
    # after processing all intervals, heap size = count meeting rooms needed 
    return len(min_heap)