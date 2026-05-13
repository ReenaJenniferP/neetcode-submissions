class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.hash_map = [[] for _ in range(1000)]
    
    def hash_key(self, key):
        return key % self.size

    def find_index(self, key, h):
        for i, (k, v) in enumerate(self.hash_map[h]):
            if k == key:
                return i
        return -1 

    def put(self, key: int, value: int) -> None:
        h = self.hash_key(key)

        idx = self.find_index(key, h)

        if idx == -1:
            self.hash_map[h].append((key, value))
        else:
            self.hash_map[h][idx] = (key, value)

    def get(self, key: int) -> int:
        h = self.hash_key(key)
        idx = self.find_index(key, h)
        if idx == -1:
            return -1
        return self.hash_map[h][idx][1]
        

    def remove(self, key: int) -> None:
        h = self.hash_key(key)
        idx = self.find_index(key, h)

        if idx != -1:
            self.hash_map[h].pop(idx)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)