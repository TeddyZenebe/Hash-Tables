import time
import bcrypt

input_string = b"apple"
n = 1000000
​   print(f"Hashing {n}x")
​
start_time = time.time()
for i in range(n):
    output_hash = hash(input_string)
end_time = time.time()
print (f"  Python hash runtime: {end_time - start_time} seconds")
​
def djb2(key):
    '''
    DJB2 hash
    '''
    # Start from an arbitrary large prime
    hash_value = 5381
    # Bit-shift and sum value for each character
    for char in key:
        hash_value = ((hash_value << 5) + hash_value) + char
    return hash_value
​
​
​
start_time = time.time()
for i in range(n):
    djb2(input_string)
end_time = time.time()
print(djb2(input_string))
print(f"  DJB2 hash runtime: {end_time - start_time} seconds")
​
​
​
start_time = time.time()
salt = bcrypt.gensalt()
for i in range(5):
    bcrypt.hashpw(input_string, salt)
end_time = time.time()
print(f"  bcrypt hash runtime: {end_time - start_time} seconds")

class DynamicArray:
    def __init__(self, capacity = 8):
        self.length = 0
        self.capacity = capacity
        self.storage = [None] * capacity
    
    def insert(self, index, value):
        if self.length >= self.capacity:
            self.resize()
​
        # shift everything to the right of index, to the right
        for i in range(self.length, index, -1):
            self.storage[i] = self.storage[i - 1]
        # insert the value, at the index
        self.storage[index] = value
        self.length += 1
    
    def append(self, value):
        if self.length >= self.capacity:
            self.resize()
        self.storage[self.length] = value
        self.length += 1
    
    def resize(self):
        # create a new array, bigger in size
        self.capacity *= 2 # double the array size
        new_storage = [None] * self.capacity
        # move all elements from old array, into new one
        for i in range(self.length):
            new_storage[i] = self.storage[i]
        # set the new array to storage
        self.storage = new_storage