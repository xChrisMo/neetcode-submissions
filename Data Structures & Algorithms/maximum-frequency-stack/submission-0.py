class FreqStack:
    def __init__(self):
        # max_freq: int
        # freq: Dict[str] elemenet -> stack
        # group: Dict[str] freq -> stack
        self.max_freq = 0
        self.freq = {} #element: count
        self.group = {} #count: [element]

    def push(self, val: int) -> None:
        # add to freq, 
        self.freq[val] = self.freq.get(val, 0) + 1
        
        # get max_freq,
        self.max_freq = max(self.max_freq, self.freq[val]) 
        
        # add key where value == max_freq
        if self.freq[val] in self.group:
            self.group[self.freq[val]].append(val)

        else:
            self.group[self.freq[val]] = [val]

    def pop(self) -> int:
        # no need to check if stack, that would always be valid!
        # val = group[max_freq].pop()

        # if group[max_freq] == 0:
        # max_freq -= 1
        # return val
        val = self.group[self.max_freq].pop()

        self.freq[val] -= 1

        if len(self.group[self.max_freq]) == 0:
            self.max_freq -= 1

        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()


# stack = []
# push(x: int) -> None:
# pop() -> int:


# [5, 7, 5, 7, 4, 5]

# max_freq = 3

# {5: 3, 7:2, 4:1}
# {1:[5, 7, 4], 2:[5, 7], 3:[5], 4:[], 5:[], 6:[], 7:[]}


# pops

# 5
# 7
# 5
# 4