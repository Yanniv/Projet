class HashTable:

    def __init__(self):
        self.size = 10
        self.hashmap = [[] for _ in range(0, self.size)]
        print(self.hashmap)

    
    def my_hashing(self, key):
        hashed_key = hash(key) % self.size
        return hashed_key


    def set(self, key, value):
        hash_key = self.my_hashing(key)
        key_exists = False
        slot = self.hashmap[hash_key]
        for i, kv in enumerate(slot):
            k, v = kv
            if key == k:
                key_exists == True
                break

        if key_exists:
                slot[i] = ((key, value))
        else:
                slot.append((key, value))

    def get(self, key):
        hash_key = self.my_hashing(key)
        slot = self.hashmap[hash_key]
        for kv in slot:
            k, v = kv
            if key == k:
                return v
            else:
                raise KeyError('the value does not exist')
    
    
    def __setitem__(self, key, value):
        return self.set(key, value)

    def __getitem__(self, key):
        return self.get(key)


H = HashTable()

H['5'] = 'green'
H['2'] = 'yellow'
H['10'] = 'blue'
H['7'] = 'red'
H['1'] = 'purple'
H['4'] = 'white'

print (H['5'])