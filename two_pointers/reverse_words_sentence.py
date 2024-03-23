import re

def reverse_words_first(sentence):
    reversed_string = str(sentence[::-1])
    start, end = 0, 0
    while end <= len(reversed_string) - 1:
        if end == len(reversed_string) - 1:
            reversed_string = reversed_string[:start] + reversed_string[start: end][::-1]
        if reversed_string[end] == " ":
            reversed_string = reversed_string[:start] + reversed_string[start: end][::-1] + reversed_string[end:]
            start, end = end, end 
        end += 1
    return reversed_string

# time O(n), space O(n)
def reverse_words(sentence):
    # remove leading, trailing and multiple spaces using the Python regex module  
    sentence = re.sub(' +', '', sentence.strip())
    # convert updated string to list of characters as strings are immutable in Python 
    sentence = list(sentence)
    str_len = len(sentence)
    string_reverser(sentence, 0, str_len - 1) # words in desired location but in reverse order 
    
    start, end = 0, 0
    
    # iterate reversed string and reverse each word in place
    while start < str_len:
        # find end index of word
        while end < str_len and sentence[end] != ' ':
            end += 1
        # call helper function to reverse just word this time 
        string_reverser(sentence, start, end - 1)
        start = end + 1
        end += 1
    return ''.join(sentence)

def string_reverser(_str, start_rev, end_rev):
    # starting from 2 ends of list and moving inwards to center, swap characters 
    while start_rev < end_rev:
        temp = _str[start_rev] # temp store for swapping 
        _str[start_rev] = _str[end_rev]
        _str[end_rev] = temp
        
        start_rev += 1 # move forwards towards middle
        end_rev -= 1 # move backwards towards middle 

def main():
    string_to_reverse = ["Hello Friend", "    We love Python",
                         "The quick brown fox jumped over the lazy dog   ",
                         "Hey", "To be or not to be",
                         "AAAAA","Hello     World"]

    for i in range(len(string_to_reverse)):
        print(i+1, ".\t Actual string:\t\t" +
              "".join(string_to_reverse[i]), sep='')
        Result = reverse_words(string_to_reverse[i])
        print("\t Reversed string:\t" +
              "".join(Result), sep='')
        print("-"*100)


if __name__ == '__main__':
    main()