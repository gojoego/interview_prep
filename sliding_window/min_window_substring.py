# time O(n + m), space O(1)
def min_window(s, t):
    # identify whether t is valid string or not, return empty string if not  
    if t == "":
        return ""
    
    req_count = {} # populate with characters in t and corresponding frequencies 
    window = {} # used to keep track of frequency of characters of t in current window 
    
    # traverse each character of t to add frequencies
    for c in t:
        req_count[c] = 1 + req_count.get(c, 0) # add 1 if it doesn't exist, increment if it does 
    
    # initialized to contain same characters present in t but with counts set to 0    
    for c in t:
        window[c] = 0
    
    # tell us whether we need to increase/decrease size of sliding window
    current, required = 0, len(req_count) # current increments by 1 when char whose freq in window matches req_count, required will hold size, when equal all char found  
    result, result_length = [-1, -1], float("infinity")
    
    # initialize 2 pointers 
    left = 0
    for right in range(len(s)):
        c = s[right]
        
        # if new character present in window, increment by 1 
        if c in t:
            window[c] = 1 + window.get(c, 0)
        
        # check if current character has appeared same number of times in current window as it appears in t, increment if so 
        if c in req_count and window[c] == req_count[c]:
            current += 1
        
        # substring found that meets requirements, adjusting sliding window 
        while current == required:
            # start reducing size of current window to find shorter substring that still meets requirements
            # update result 
            if (right - left + 1) < result_length:
                result = [left, right]
                result_length = (right - left  + 1)
                
            # pop from left of window 
            if s[left] in t:
                window[s[left]] -= 1
            
            # if popped character was among required characters and removing it has reduced its frequency below its frequency in t, decrement currt 
            if s[left] in req_count and window[s[left]] < req_count[s[left]]:
                current -= 1
            
            left += 1
    left, right = result

    # return minimum window substring 
    return s[left: right + 1] if result_length != float("infinity") else ""

def main():
    s = ["PATTERN", "LIFE", "ABRACADABRA", "STRIKER", "DFFDFDFVD"]
    t = ["TN", "I", "ABC", "RK", "VDD"]
    for i in range(len(s)):
        print(i + 1, ".\ts: ", s[i], "\n\tt: ", t[i], "\n\tThe minimum substring containing ", \
              t[i], " is: ", min_window(s[i], t[i]), sep="")
        print("-" * 100)

if __name__ == '__main__':
    main()