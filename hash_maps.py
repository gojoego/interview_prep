'''
hash map/hash table
-data structure that stores key-value pairs
-provides way to efficiently map keys to values for quick retrieval of value w/ given key 
-use hash function behind scenes to compute index or hash code for each key 
-index determines where corresponding value will be stored in underlying array 
-hash functions and collision resolution strategies aid in determining time complexities 

methods
-insert(key, value): key/value pair inserted into hash map -> hash function computes index 
based on key, index used to determine location in hash map where value stored, collision 
resolution strategy in case different keys hash to same index (chaining or open addressing),
worst case time O(n)
-search(key): hash function applied to key to compute index and retrieve value from hash map,  
then value stored at index returned, worst case time O(n)
-remove(key): removing key/value pair typically involves finding index based on key's hash and 
then removing value stored at that index, worst case time O(n)

examples
1. two sum 
2. word count 
3. find 4 elements a,b,c,d such that a+b=c+d
4. divide array into pairs whose sum divisible by 2

does your problem match this pattern? yes, if...
-data access: repeated fast access during algo
-pair-wise relation: store relationship between 2 sets of data to compute result, key/value pair 

real-world problems
-telecommunications 
-e-commerce
-file system 

'''

# design HashMap data structure with constructor(), put(key,value), get(key) and remove(key)
# time O(N), N = total number of possible keys, space O(K + M), K = key space size, M = number of unique keys inserted
class Bucket:
    def __init__(self): 
        # initialize empty list to store key/value pairs 
        self.bucket = []
    
    def get(self, key):
        # iterate through each key/value pair in bucket 
        for (k, v) in self.bucket:
            # if key matches provided key, return corresponding value 
            if k == key:
                return v
        
        # if key not found, return -1
        return -1 
    
    def update(self, key, value):
        # flag to indicate whether key found in bucket 
        found = False
        
        # iterate through each key/value pair in bucket 
        for i, kv in enumerate(self.bucket):
            # if key matches key of current key/value pair
            if key == kv[0]:
                # update value of key/value pair 
                self.bucket[i] = (key, value)
                
                # set flag to True, indicating that key found
                found = True
                break
        
        # if key not found in bucket, add it along with its value
        if not found:
            self.bucket.append((key, value))
    
    def remove(self, key):
        # iterate through each key/value pair in bucket 
        for i, kv in enumerate(self.bucket):
            # if key matches key of current key/value pair 
            if key == kv[0]:
                # delete key/value pair from bucket 
                del self.bucket[i]
                # exit loop as key has been removed 
                break

class DesignHashMap():
    # use the constructor below to initialize hash map based on the keyspace
    def __init__(self):
        # choose prime number for key space size (preferably large one)
        self.key_space = 2069 
        # create array and initialize it with empty buckets equal to key space size 
        self.bucket = [Bucket()] * self.key_space
        
    # implement supporting functions     
    # function to add key/value pair to hash map 
    def put(self, key, value):
        # generate hash key by taking modulus of input key with key space size 
        hash_key = key % self.key_space
        self.bucket[hash_key].update(key, value)
    
    # function to retrieve value associated with given key from hash map
    def get(self, key):
        hash_key = key % self.key_space
        return self.bucket[hash_key].get(key)

    # function to remove key/value pair from hash map given key 
    def remove(self, key):
        hash_key = key % self.key_space
        self.bucket[hash_key].remove(key)
        
def main():
    input_hash_map = DesignHashMap()
    keys = [5, 2069, 2070, 2073, 4138, 2068]
    keys_list = [5, 2069, 2070, 2073, 4138, 2068]
    values = [100, 200, 400, 500, 1000, 5000]
    funcs = ["Get", "Get", "Put", "Get",
             "Put", "Get", "Get", "Remove",
             "Get", "Get", "Remove", "Get"]
    func_keys = [[5], [2073], [2073, 250], [2073], 
                 [121, 110], [121], [2068], [2069], [2069],
                 [2071], [2071], [2071]]

    for i in range(len(keys)):
        input_hash_map.put(keys[i], values[i])

    for i in range(len(funcs)):
        if funcs[i] == "Put":
            print(
                i + 1,  ".\t put(", func_keys[i][0],  ", ", func_keys[i][1],  ")", sep="")
            if not func_keys[i][0] in keys_list:
                keys_list.append(func_keys[i][0])
            input_hash_map.put(func_keys[i][0], func_keys[i][1])
        elif funcs[i] == "Get":
            print(i + 1, ".\t get(", func_keys[i][0], ")", sep="")
            print("\t Value returned: ", input_hash_map.get(
                func_keys[i][0]), sep="")
        elif funcs[i] == "Remove":
            print(i + 1,  ". \t remove(", func_keys[i][0], ")", sep="")
            input_hash_map.remove(func_keys[i][0])

        print("-"*100)


if __name__ == '__main__':
    main()