class RandomizedSet:
    def __init__(self):
        self.nums = {}
        self.index = []

    def insert(self, val: int) -> bool:
        if val in self.nums:
            return False

        self.nums[val] = len(self.index)
        self.index.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.nums:
            return False

        remove_idx = self.nums[val]
        last_val = self.index[-1]

        # move last value into removed spot
        self.index[remove_idx] = last_val
        self.nums[last_val] = remove_idx

        # remove last element
        self.index.pop()
        del self.nums[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.index)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()