class MyHashMap:
    def __init__(self):
        self.nums = [-1 for _ in range(1000001)]

    def put(self, key: int, value: int) -> None:
        # if key in dict, update value, else add value to key
        self.nums[key] = value

    def get(self, key: int) -> int:
        # if key not in hash, return -1, else return val
        return self.nums[key]

    def remove(self, key: int) -> None:
        # remove the key and value if exists!
        self.nums[key] = -1
        

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


# use a list of lists. 
# key = index, value = value