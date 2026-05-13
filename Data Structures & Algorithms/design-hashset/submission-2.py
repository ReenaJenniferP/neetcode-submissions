class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.hash_set = [[] for _ in range(self.size)]

    def hash_key(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        h = self.hash_key(key)

        if key not in self.hash_set[h]:
            self.hash_set[h].append(key)

    def remove(self, key: int) -> None:
        h = self.hash_key(key)

        if key in self.hash_set[h]:
            self.hash_set[h].remove(key)

    def contains(self, key: int) -> bool:
        h = self.hash_key(key)

        return key in self.hash_set[h]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)