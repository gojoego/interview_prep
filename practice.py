MOD = 1000000007

# Method to count the good subsequences
def count_good_subsequences(s):
    # Initializing factorials and inverses array of size N + 1
    N = len(s) + 1
    factorials = [1] * N
    inverses = [1] * N

    # Calculating the factorial and inverse of all numbers from 1 to N
    # instead of calculating factorial of a number again and again
    # we will store the factorial of a number i
    # and use to calculate the factorial of a number i+1, since
    # the factorial of a number i+1 is factorial of i-1 * i
    for i in range(1, N):
        factorials[i] = factorials[i - 1] * i % MOD
        inverses[i] = quick_modular_inverse(factorials[i], MOD - 2, MOD)

    # Initializing an array of size 26 to hold the frequency
    # of each character from 'a' to 'z'
    frequency_count = [0] * 26

    # Initializing a variable to keep record of maximum frequency
    max_count = 1

    # Calculating the frequency of each character and
    # keeping record of maximum frequency
    for char in s:
        max_count = max(max_count, frequency_count[ord(char) - ord('a')] + 1)
        frequency_count[ord(char) - ord('a')] += 1

    # Initializing a variable to store the count of good subsequences
    final_count = 0

    # Nested loop to calculate the combination
    # from 1 to the maximum frequency
    for i in range(1, max_count + 1):
        count = 1

        for j in range(26):
            # Counting only if count of frequency of a character is
            # greater or equal than the i
            if frequency_count[j] >= i:
                count = count * (combination(frequency_count[j], i, factorials, inverses) + 1) % MOD

        # Adding the count to the final count after subtracting 1
        # and taking the mod
        final_count = (final_count + count - 1) % MOD

    # Returning the final count after casting it to integer
    return int(final_count)

# Method to find the modular inverse of a number
def quick_modular_inverse(base, exponent, modulus):
    # Initialize result to 1, as 1 is the identity element for multiplication modulo modulus
    result = 1

    while exponent != 0:
        # If exponent is odd, multiply result by base and take modulo modulus
        if (exponent & 1) == 1:
            result = result * base % modulus
        # Right shift exponent by 1 (equivalent to dividing exponent by 2)
        exponent >>= 1
        # Square base and take modulo modulus to reduce base in terms of modulus
        base = base * base % modulus

    return result

# Calculating the combination (n choose k)
def combination(n, k, factorials, inverses):
    return (factorials[n] * inverses[k] % MOD) * inverses[n - k] % MOD

def climb_stairs(n):
    # If there are 0 or 1 steps, there's only one way to climb the stairs
    if n == 0 or n == 1:
        return 1
    
    # Initialize the lookup table with base cases
    lookup = [0] * (n + 1)
    lookup[0] = 1  # 1 way to stay at the ground (0th step)
    lookup[1] = 1  # 1 way to climb 1 step
    
    # Fill in the lookup table for steps 2 to n
    for i in range(2, n + 1):
        lookup[i] = lookup[i - 1] + lookup[i - 2]
    
    # The nth index in the lookup table gives the number of ways to climb n stairs
    return lookup[n]

# Example usage
print(climb_stairs(5))  # Output: 8




















def num_of_decodings(decode_str):
    str_len = len(decode_str)
    # initialize the dp array with all 0s
    dp = [0] * (str_len + 1)
    # there is only one way to decode an empty string
    dp[0] = 1
    # the first element of the dp array is 1 if the first character 
    # of the string is not '0', otherwise it's 0
    if decode_str[0] != '0':
        dp[1] = 1 
    else:
        return 0

    # iterate through the input string starting from the 2nd character
    for i in range(2, str_len + 1):
        # if the current character is not '0', add the number of ways 
        # to decode the substring without the current character
        if decode_str[i - 1] != '0':
            dp[i] += dp[i - 1]
        # if the substring of the current and previous characters is a valid 
        # two-digit number, add the number of ways to decode the substring 
        # without the current and previous characters
        if decode_str[i - 2] == '1' or \
          (decode_str[i - 2] == '2' and decode_str[i - 1] <= '6'):
            dp[i] += dp[i - 2]

    # return the number of ways to decode the input string
    return dp[str_len]

# Driver code
def main():
    decode_str = ["124", "123456", "11223344", "0", "0911241", "10203", "999901"]

    for i in range(len(decode_str)):
        print(i + 1, f".\t There are {num_of_decodings(decode_str[i])} ways in which we can decode the string: '", 
                        decode_str[i], "'", sep="")
        print("-" * 100)

if __name__ == '__main__':
    main()
    
    
MOD = 1000000007

# Method to count the good subsequences
def count_good_subsequences(s):
    # Initializing factorials and inverses array of size N + 1
    N = len(s) + 1
    factorials = [1] * N
    inverses = [1] * N

    # Calculating the factorial and inverse of all numbers from 1 to N
    # instead of calculating factorial of a number again and again
    # we will store the factorial of a number i
    # and use to calculate the factorial of a number i+1, since
    # the factorial of a number i+1 is factorial of i-1 * i
    for i in range(1, N):
        factorials[i] = factorials[i - 1] * i % MOD
        inverses[i] = quick_modular_inverse(factorials[i], MOD - 2, MOD)

    # Initializing an array of size 26 to hold the frequency
    # of each character from 'a' to 'z'
    frequency_count = [0] * 26

    # Initializing a variable to keep record of maximum frequency
    max_count = 1

    # Calculating the frequency of each character and
    # keeping record of maximum frequency
    for char in s:
        max_count = max(max_count, frequency_count[ord(char) - ord('a')] + 1)
        frequency_count[ord(char) - ord('a')] += 1

    # Initializing a variable to store the count of good subsequences
    final_count = 0

    # Nested loop to calculate the combination
    # from 1 to the maximum frequency
    for i in range(1, max_count + 1):
        count = 1

        for j in range(26):
            # Counting only if count of frequency of a character is
            # greater or equal than the i
            if frequency_count[j] >= i:
                count = count * (combination(frequency_count[j], i, factorials, inverses) + 1) % MOD

        # Adding the count to the final count after subtracting 1
        # and taking the mod
        final_count = (final_count + count - 1) % MOD

    # Returning the final count after casting it to integer
    return int(final_count)

# Method to find the modular inverse of a number
def quick_modular_inverse(base, exponent, modulus):
    # Initialize result to 1, as 1 is the identity element for multiplication modulo modulus
    result = 1

    while exponent != 0:
        # If exponent is odd, multiply result by base and take modulo modulus
        if (exponent & 1) == 1:
            result = result * base % modulus
        # Right shift exponent by 1 (equivalent to dividing exponent by 2)
        exponent >>= 1
        # Square base and take modulo modulus to reduce base in terms of modulus
        base = base * base % modulus

    return result

# Calculating the combination (n choose k)
def combination(n, k, factorials, inverses):
    return (factorials[n] * inverses[k] % MOD) * inverses[n - k] % MOD

# Driver code
input_list = ["aqw", "aabbcc", "aaa", "abbc", "abbb"]

for i, s in enumerate(input_list):
    print(f"{i + 1}.\tInput string: {s}")
    print(f"\tNumber of good subsequences: {count_good_subsequences(s)}")
    print('-' * 100)