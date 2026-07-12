class MyHashSet:
    def __init__(self):
        # use it as a list
        self.num_set = [[] for i in range(1000001)]

    def add(self, key: int) -> None:
        # if key not in 'set', add key?
        self.num_set[key].append('#')

    def contains(self, key: int) -> bool:
        # T or F is key in 'set'
        return len(self.num_set[key]) > 0

    def remove(self, key: int) -> None:
        # if key in 'set', delete key + value in set 
        self.num_set[key] = []


# 


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)