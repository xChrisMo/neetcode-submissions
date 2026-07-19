class FreqStack:
    def __init__(self):
        self.count_dict = defaultdict(int)
        self.stack_dict = defaultdict(list)
        self.max_count = 0

    def push(self, val: int) -> None:
        # update count of val
        self.count_dict[val] += 1
        # get its frequency
        freq = self.count_dict[val]

        # chekc if this is the max count
        self.max_count = max(self.max_count, freq)

        # add it to that frequency list !
        self.stack_dict[freq].append(val)
        # put the max count to be the higghest count list?

    def pop(self) -> int:
        val = self.stack_dict[self.max_count].pop()

        self.count_dict[val] -= 1

        if len(self.stack_dict[self.max_count]) == 0:
            self.max_count -= 1

        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()



[5,7,4]
[]