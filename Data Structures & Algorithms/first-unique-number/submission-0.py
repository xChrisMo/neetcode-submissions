# queue of integers
# find uniqye integer inside queue

# make a queue to add all, 
# make a dict to store index

# [2:1, 3:1, 5:2]
# [2, 3, 5, 5]

#sf: 2
#add: 5

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.freq = {}
        self.q = deque()
        
        for num in nums:
            self.freq[num] = self.freq.get(num, 0) + 1
            self.q.append(num)
        
    def showFirstUnique(self) -> int:
        for char in self.q:
            if self.freq[char] == 1:
                return char
            
            continue

        return -1

    def add(self, value: int) -> None:
        self.freq[value] = self.freq.get(value, 0) + 1
        self.q.append(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
