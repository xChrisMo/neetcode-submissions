class MyHashSet:
    def __init__(self):
        # use it as a list
        self.num_set = [False for i in range(1000001)]

    def add(self, key: int) -> None:
        # if key not in 'set', add key?
        self.num_set[key] = True

    def contains(self, key: int) -> bool:
        # T or F is key in 'set'
        return self.num_set[key]

    def remove(self, key: int) -> None:
        # if key in 'set', delete key + value in set 
        self.num_set[key] = False

# 


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)