# time O(n), space O(1)
def longest_repeating_character_replacement(s, k):
    string_length = len(s)
    length_max_substring = 0 # keep track of longest substring with same characters after replacements 
    start = 0 # initialize first pointer to 0 
    char_frequency = {} # used to keep track of frequency of characters in current window using hash map 
    most_frequent_char = 0 # keep track of frequency of most occurring character 
    
    # iterating over string using end pointer 
    for end in range(string_length):
        # check if new character present in hash map 
        if s[end] not in char_frequency:
            # add character in hash map and initialize frequency to 1 if not
            char_frequency[s[end]] = 1
        else:
            # increment frequency by 1 if found 
            char_frequency[s[end]] += 1
        
        # compare frequency of new character with most frequent character to update as needed 
        most_frequent_char = max(most_frequent_char, char_frequency[s[end]])
        
        # check if number of characters in window other than most occurring character is greater than k
        # if TRUE -> number of replacements required in current window has exceeded limit k 
        if end - start + 1 - most_frequent_char > k:
            # slide window 1 step forward 
            # decrement frequency of character to be dropped out of window 
            char_frequency[s[start]] -= 1
            # increment start pointer by 1 
            start += 1
        
        # update with current window size if window is greater than current length of max substring 
        length_max_substring = max(end - start + 1, length_max_substring)
    
    # after entire input stirng traversed 
    return length_max_substring
        
def main():
    input_strings = ["aabccbb", "abbcb", "abccde", "abbcab", "bbbbbbbbb"]
    values_of_k = [2, 1, 1, 2, 4]

    for i in range(len(input_strings)):
        print(i+1, ".\tInput String: ", input_strings[i], sep="")
        print("\tk: ", values_of_k[i], sep="")
        print("\tLength of longest substring with repeating characters: ", longest_repeating_character_replacement(input_strings[i], values_of_k[i]))
        print("-" * 100)

if __name__ == '__main__':
    main()