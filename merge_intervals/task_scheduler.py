# time O(N), space O(1)
def least_time(tasks, n):
    frequencies = {} # initialize dictionary to store frequencies of tasks
    for task in tasks: # store frequency of each task 
        frequencies[task] = frequencies.get(task, 0) + 1
    frequencies = dict(sorted(frequencies.items(), key=lambda x:x[1])) # sort frequencies 
    max_freq = frequencies.popitem()[1] # store max frequency 
    idle_time = (max_freq - 1) * n # calculate max possible idle time 
    while frequencies and idle_time > 0: # iterate over frequencies array and update idle time 
        idle_time -= min(max_freq - 1, frequencies.popitem()[1]) 
    idle_time = max(0, idle_time)
    
    return len(tasks) + idle_time

def main():
    all_tasks = [['A', 'A', 'B', 'B'],
                  ['A', 'A', 'A', 'B', 'B', 'C', 'C'],
                  ['S', 'I', 'V', 'U', 'W', 'D', 'U', 'X'],
                  ['M', 'A', 'B', 'M', 'A', 'A', 'Y', 'B', 'M'],
                  ['A', 'K', 'X', 'M', 'W', 'D', 'X', 'B', 'D', 'C', 'O', 'Z', 'D', 'E', 'Q']]
    all_ns = [2, 1, 0, 3, 3]

    for i in range(len(all_tasks)):
        print(i+1, '.', '\tTasks: ', all_tasks[i], sep='')
        print('\tn: ', all_ns[i], sep='')
        min_time = least_time(all_tasks[i], all_ns[i])
        print('\tMinimum time required to execute the tasks: ', min_time)
        print('-' * 100)

if __name__ == '__main__':
    main()