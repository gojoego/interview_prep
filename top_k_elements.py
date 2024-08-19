from heapq import *

class KthLargest:
    # Constructor to initialize heap and add values in it
    def __init__(self, k, nums):
        self.top_k_heap = []
        self.k = k
        for element in nums:
            self.add(element)

    # Adds element in the heap and return the Kth largest
    def add(self, val):
        if len(self.top_k_heap) < self.k:
            heappush(self.top_k_heap, val)
        elif val > self.top_k_heap[0]:
            heappop(self.top_k_heap)
            heappush(self.top_k_heap, val)
        return self.top_k_heap[0]
 
from collections import Counter

def reorganize_string(str):
    result = ""
    # store each character and freq in hash map 
    freq = [] # initialize heap 
    char_counter = Counter(str) # calculate freq of char in string and store counts in + char itself in hash map
    # iterate through hash map and store negative count of each char + char itself in heap 
    for char, count in char_counter.items():
        freq.append([-count, char]) # store negative count of each char so when popped will return char w max freq 

    # max heap using character freq data so that most freq at root 
    heapify(freq) # construct heap from array 
    
    previous = None # stores previous char used so we don't use again 
    # iterate over heap, pop most freq char and append to result string 
    while len(freq) > 0 or previous:
        if previous and len(freq) == 0:
            return ""
        
        # highest freq char always at root of heap - keep popping from top to add to result 
        count, char = heappop(freq)
        result = result + char
        # decrement freq of popped char since we've used 1 occurrence of it
        count = count + 1 # since we stored negative count, adding 1 actually decrements it
        
        # push popped char back onto heap in next iteration if updated freq > 0 
        if previous:
            heappush(freq, previous)
            previous = None
        
        # setting previous to most recent used char 
        if count != 0:
            previous = [count, char]
    
    # return result string when heap empty
    return result

def k_closest(points, k):
    points_max_heap = []
    
    # push first k points to heap 
    for i in range(k):
        heappush(points_max_heap, points[i])
    
    # go through remaining points of input array
    for i in range(k, len(points)): # calc distance btw origin and each point
        # compare distance of point w distance of top of heap 
        if points[i].distance_from_origin() < points_max_heap[0].distance_from_origin():
            # push and pop point from heap
            heappop(points_max_heap)
            heappush(points_max_heap, points[i])
    
    # return points from heap 
    return list(points_max_heap)

def top_k_frequent(arr, k):
    frequencies = {}
    for num in arr:
        frequencies[num] = frequencies.get(num, 0) + 1
        
    top_k_elements = []
    
    for num, frequency in frequencies.items():
        heappush(top_k_elements, (frequency, num))
        if len(top_k_elements) > k:
            heappop(top_k_elements)
            
    top_numbers = []
    while top_k_elements:
        top_numbers.append(heappop(top_k_elements)[1])
        
    return top_numbers

def find_kth_largest(nums, k):
    k_numbers = []

    for i in range(k): # insert first k elements into min heap 
        k_numbers.append(nums[i])
        
    heapify(k_numbers)
    
    for i in range(k, len(nums)): # iterate over array and compare to min heap root
        if nums[i] > k_numbers[0]: # if greater, pop root and push greater element 
            heappop(k_numbers)
            heappush(k_numbers, nums[i])
    
    return k_numbers[0] # return root element as k greatness 

def top_k_frequent(words, k):
    result = []
    # count and store frequency of words in list 
    frequencies = {}
    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1
        
    # create max heap w priority based on frequency of words
    word_heap = []
    # push words with frequency to heap 
    for word, frequency in frequencies.items():
        heappush(word_heap, (-frequency, word))
        
    # pop k elements from heap being top k frequent words 
    for _ in range(k):
        freq, word = heappop(word_heap)
        result.append(word)
        
    return result

# Function used to convert list to string
def lst_to_str(lst):
    out = "["
    for i in range(len(lst)-1):
        out += str(lst[i]) + ", "
    out += str(lst[len(lst)-1]) + "]"
    return out
    
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __lt__(self, other): # __lt__ is used for max-heap
        return self.distance_from_origin() > other.distance_from_origin()
    
    def __str__(self): # __str__ is used to print the x and y values
        return '[{self.x}, {self.y}]'.format(self=self)
    
    def distance_from_origin(self): # distance_from_origin calculates the distance using x, y coordinates
        return (self.x * self.x) + (self.y * self.y)
    
    __repr__ = __str__
    
def main():
    input_array = [
                    [1, 5, 12, 2, 11, 9, 7, 30, 20],
                    [5, 2, 9, -3, 7],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 4, 6, 0, 2],
                    [3, 5, 2, 3, 8, 5, 3]
                ]

    k = [3, 1, 9, 1, 4]

    for i in range(len(input_array)):
        print(i + 1, ".\tInput array: ", input_array[i], sep="")
        print("\tValue of k: ", k[i], sep="")
        print("\tkth largest number: ", find_kth_largest(input_array[i], k[i]), sep="")
        print("-" * 100)


if __name__ == '__main__':
    main()
