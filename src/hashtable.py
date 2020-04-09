# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.length = 0
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        index = self._hash_mod(key)
        current = self.storage[index] # Pair at current index
        last = None # Pair to insert
        # Check if current location is empty
        # Handle collisions by adding new LinkedPair
        while current and current.key != key:
            last = current
            current = last.next
        # If a current is found with same key
        if current:
            current.value = value
        # If a current is not found
        else:
            new = LinkedPair(key, value)
            new.next = self.storage[index]
            self.storage[index] = new
      
        '''
        Store the value with the given key.
 
        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        current = self.storage[index] # Pair at current index
        last = None # Pair to insert
        while current is not None and current.key != key:
		    last = current
		    current = last.next
        if current is None:
		    return None
	    else:
            self.size -= 1
		    result = current.value
            if last is None:
			    current = None
		    else:
                last.next = last.next.next
            return result
            
    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] is None:
            print(f"error")
        else:
            for i in self.storage[index]:
                if i[0] == key:
                    return i[1]
                print(f"error")

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        
        Fill this in.
               '''
        ht2 = HashTable(length=len(self.storage)*2)
        for i in range(len(self.storage)):
            if self.storage[i] is None:
                continue
            for j in self.storage[i]:
                ht2.add(j[0], j[1])
        self.storage = ht2.storage

if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
