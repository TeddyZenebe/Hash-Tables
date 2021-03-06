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
        #if self.storage[index] is not None:
            #print('WARN: Collision detected for key ' + key)
            #current = self.storage[index] #(key1, value)
            #prev = current
            #while current is not None:
                #prev = current
                #current = current.next #at the end of the chain the last node will have self.next == None so current become None and while loop get break so the prev.next will be the new node
            #prev.next = LinkedPair(key, value)
        #else:
            #self.storage[index] = LinkedPair(key, value)
        current = self.storage[index] # Pair at current index
        prev = None # Pair to insert
        #Check if current location is empty
        # Handle collisions by adding new LinkedPair
        while current and current.key != key:
            prev = current
            current = prev.next
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
        current = self.storage[index]
        while current is not None and current.key != key:
            current = current.next
        if current is None:
            return None
        else:
            self.storage[index] = None 
        
            
    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        current = self.storage[index]
        if current is None:
            return None
        while current is not None and current.key != key:
            current = current.next
        if current is None: # when while break with current = None 
            return None
        else:# when while break with current.key == key
            return current.value

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        
        Fill this in.
               '''
        self.capacity *=2 # double the Array size
        new_storage = [None] * self.capacity 
        # move all elements from old Array, into new one
        for i in range(len(self.storage)):
            new_storage[i] = self.storage[i]
        # set the mew array to storage
        self.storage = new_storage
        #old_storage = self.storage
        #self.capacity *= 2
        # create an new array size *2
        #self.storage = [None] * self.capacity
        # move all values over
        #for pair in old_storage:
            #reinsert all key
            #if pair is not None:
                #self.insert(pair.key, pair.value)      

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
