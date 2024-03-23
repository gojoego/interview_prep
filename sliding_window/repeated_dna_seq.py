# naive approach, time and space O((n - k) * k)
def find_repeated_sequences_naive(s, k):
    substrings = set()
    output = set()
    for i in range(len(s)):
        if s[i: i + k] in substrings:
            output.add(s[i: i + k])
        else: 
            substrings.add(s[i: i + k])
    return output

# optimized with sliding window, time O((n - k) * k), space O(n)
def find_repeated_sequences(s, k):
    n = len(s)
    # if length of string is less than window size k, return empty array 
    if n < k: 
        return []
    # hash map defining numeric mapping of nucleotides
    mapping = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    # base value used in polynomial hash function, base 4 -> 4 nucleotides in sequence
    a = 4
    # array storing integer form of string s based on mapping above 
    numbers = [0] * n 
    # hash set to store unique hash values of k-length substrings, output to store repeated substrings 
    hash_set, output = set(), set()
    
    for i in range(n):
        numbers[i] = mapping.get(s[i])
    # store hash value of current k-length sequence in window - initialize to 0
    hash_value = 0
    # slide window along string s using pointer i ranging from 0 to (n - k + 1)
    for i in range(n - k + 1):
        # when i == 0 window at starting position or first k-length substring 
        if i == 0:
            # calculate hash value from scratch using polynomial hash function 
            for j in range(k):
                hash_value += numbers[j] * (a ** (k - j - 1))
        # not at starting position 
        else:
            # calculate hash value of current k-length substring by utilizing hash value of previous k-length substring 
            previous_hash_value = hash_value
            hash_value = ((previous_hash_value - numbers[i - 1] * (a ** (k - 1))) * 4) + numbers[i + k - 1]
            # repeat by sliding window one character forward 
        # if k-length substring present in hash set
        if hash_value in hash_set:
            # substring repeated, add to output 
            output.add(s[i : i + k])
        # otherwise add hash value of substring to hash set 
        hash_set.add(hash_value)
    # when hash values of all k-length substrings evaluated or sliding window cannot move forward, return output 
    return output
    print("\tHash value of", s[i : i + k], ":", hash_value)
    
def main():
    inputs_string = ["ACGT", "AGACCTAGAC", "AAAAACCCCCAAAAACCCCCC", "GGGGGGGGGGGGGGGGGGGGGGGGG",
                     "TTTTTCCCCCCCTTTTTTCCCCCCCTTTTTTT", "TTTTTGGGTTTTCCA",
                     "AAAAAACCCCCCCAAAAAAAACCCCCCCTG", "ATATATATATATATAT"]
    inputs_k = [3, 3, 8, 12, 10, 14, 10, 6]

    for i in range(len(inputs_k)):
        print(i+1, ".\tInput Sequence: \'", inputs_string[i], "\'", sep="")
        print("\tk: ", inputs_k[i], sep="")
        print("\tRepeated Subsequence: ",
              find_repeated_sequences(inputs_string[i], inputs_k[i]))
        print("-"*100)


if __name__ == '__main__':
    main()