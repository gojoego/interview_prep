from heapq import heappush, heappop
import heapq

# time O(nlogn), space O(n)
def maximum_capital(c, k, capitals, profits):
    current_capital = c 
    capitals_min_heap = []
    profits_max_heap = []
    
    # 1 - push all capitals values in min-heap 
    for x in range(0, len(capitals)): # insert all capitals values to min-heap 
        heappush(capitals_min_heap, (capitals[x], x)) # populate min-heap w/ (capital required, index) tuples 
    
    for _ in range(k): # iterate k times to choose up to k projects 
        # 2 - select projects that can be invested in range of current capital and push profits in max-heap 
        # move all projects that can be started w/ current capital to max-heap 
        while capitals_min_heap and capitals_min_heap[0][0] <= current_capital:
            c, i = heappop(capitals_min_heap)
            heappush(profits_max_heap, (-profits[i]))
            
        if not profits_max_heap: # if no projects can be started, break loop 
            break
    
        # 3 - select project from max-heap that yields max profit 
        j = -heappop(profits_max_heap) # select project w/ max profit 
        # 4 - add profit from seleected project to current capital 
        current_capital = current_capital + j # update current capital by adding profit from selected project
    
    return current_capital # return max capital after selecting up to k projects 

class MedianOfStream:
    def __init__(self):
        self.min_heap_largenum = [] # store half of numbers larger than x in min heap 
        self.max_heap_smallnum = [] # store half of numbers smaller than x in max heap 
    
    def insert_num(self, num):
        if not self.max_heap_smallnum or -self.max_heap_smallnum[0] >= num:
            heappush(self.max_heap_smallnum, -num)
        else:
            heappush(self.min_heap_largenum, num)
            
        if len(self.max_heap_smallnum) > len(self.min_heap_largenum) + 1: 
            heappush(self.min_heap_largenum, -heappop(self.max_heap_smallnum))
        elif len(self.max_heap_smallnum) < len(self.min_heap_largenum): 
            heappush(self.max_heap_smallnum, -heappop(self.min_heap_largenum))
    
    def find_median(self): # calculate median of current list of numbers using top element of 2 heaps 
        if len(self.max_heap_smallnum) == len(self.min_heap_largenum):
            return -self.max_heap_smallnum[0] / 2.0 + self.min_heap_largenum[0] / 2.0
        return -self.max_heap_smallnum[0] / 1.0

class max_heap:
    def __init__(self):
        self.max_heap_list = []
    
    def insert(self, x):
        heappush(self.max_heap_list, -x)
        
    def get_max(self):
        return -self.max_heap_list[0]
        
    def __str__(self):
        out = "["
        for i in self.max_heap_list:
            out += str(i) + ", "
        out = out[:-2] + "]"
        return out

class min_heap:
    def __init__(self) -> None:
        self.min_heap_list = []
    
    def insert(self, x):
        heappush(self.min_heap_list, x)
    
    def get_min(self):
        return self.min_heap_list[0]
    
    def __str__(self):
        out = "["
        for i in self.min_heap_list:
            out += str(i) + ", "
        out = out[:-2] + "]"
        return out
    
def median_sliding_window(nums, k):
    medians = [] # store medians
    outgoing_num = {} # keep track of numbers that need to be removed from heaps 
    small_list = [] # max heap, keep n/2th element here  
    large_list = [] # min heap 
    
    # add k elements to small_list - multipy by -1 b/c max heap 
    for i in range(0, k): # initialize max heap by multiplying each element by -1 
        heappush(small_list, -1 * nums[i])
        
    for i in range(0, k // 2): # transfer top 50% of numbers from max to min heap 
        element = heappop(small_list) 
        heappush(large_list, -1 * element) # multiply by -1 to restore sign of each number 
        
    balance = 0 # variable to keep heaps balanced 
    
    i = k
    while True: 
        if (k & 1) == 1: # if odd size window 
            medians.append(float(small_list[0] * -1))
        else: 
            medians.append((float(small_list[0] * -1) + float(large_list[0])) * 0.5)
            
        if i >= len(nums): # break loop if all elements processed 
            break
        
        out_num = nums[i - k] # outgoing number
        in_num = nums[i] # incoming number
        i += 1
        
        if out_num <= (small_list[0] * -1): # if outgoing number is from max heap 
            balance -= 1
        else: 
            balance += 1 
            
        if out_num in outgoing_num: # add/update outgoing number in hash map 
            outgoing_num[out_num] = outgoing_num[out_num] + 1 
        else: 
            outgoing_num[out_num] = 1
            
        if small_list and in_num <= (small_list[0] * -1): # if incoming number less than top of max heap
            balance += 1
            heappush(small_list, in_num * -1) # add into max heap 
        else: # otherwise add to min heap 
            balance -= 1
            heappush(large_list, in_num)
            
        if balance < 0: # rebalance heaps 
            heappush(small_list, (-1 * large_list[0]))
            heappop(large_list)
        elif balance > 0:
            heappush(large_list, -1 * small_list[0])
            heappop(small_list)
            
        balance = 0 # reset balance variable to 0 since heaps balanced to ensure 2 heaps 
        # contain correct elements for calculations to be performed on elements in next window 
        
        # remove invalid numbers present in hash map from top of max heap 
        while (small_list[0] * -1) in outgoing_num and (outgoing_num[(small_list[0] * -1)] > 0):
            outgoing_num[small_list[0] * -1] = outgoing_num[small_list[0] * -1] - 1
            heappop(small_list)   
        
        # remove invalid numbers present in hash map from top of min heap
        while large_list and large_list[0] in outgoing_num and (outgoing_num[large_list[0]] > 0):
            outgoing_num[large_list[0]] = outgoing_num[large_list[0]] - 1
            heappop(large_list)
            
    return medians

def tasks(tasks_list):
    optimal_machines = 0 # count total # machines for optimal machines task 
    machines_available = [] # empty list to store tasks finish time 
    heapq.heapify(tasks_list) # convert task list to heap 
    
    while tasks_list: # loop through tasks list 
        task = heapq.heappop(tasks_list) # remove task with earliest start time
        # if there are machines available and top task if later than or at the same time as the task as the first available machine 
        if machines_available and task[0] >= machines_available[0][0]:
            machine_in_use = heapq.heappop(machines_available) # top element deleted from available machines 
            machine_in_use = (task[1], machine_in_use[1]) # schedule task on current machine 
        else: # if conflicting task, increment counter for machines and store task end time on machines heap 
            optimal_machines += 1 
            machine_in_use = (task[1], optimal_machines)
        heapq.heappush(machines_available, machine_in_use) # push updated machine or new machine back into heap 
        
    return optimal_machines # return total number of machines used by tasks in tasks list 

def main():

    # Input: A set "tasks_list" of "n" tasks, such that
    # each task has a start time and a finish time
    input_tasks_list = [[(1, 1), (5, 5), (8, 8), (4, 4),
                        (6, 6), (10, 10), (7, 7)],
                        [(1, 7), (1, 7), (1, 7),
                        (1, 7), (1, 7), (1, 7)],
                        [(1, 7), (8, 13), (5, 6), (10, 14), (6, 7)],
                        [(1, 3), (3, 5), (5, 9), (9, 12),
                        (12, 13), (13, 16), (16, 17)],
                        [(12, 13), (13, 15), (17, 20),
                        (13, 14), (19, 21), (18, 20)]]

    # loop to execute till the length of tasks
    for i in range(len(input_tasks_list)):
        print(i + 1, ".\t Tasks = ", input_tasks_list[i], sep="")

        # Output: A non-conflicting schedule of tasks in
        # "tasks_list" using the minimum number of machines
        print("\t Optimal number of machines = ",
              tasks(input_tasks_list[i]), sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()