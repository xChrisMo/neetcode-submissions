class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.pointer = 0

    def visit(self, url: str) -> None:
        # slice at pointer, remember slicing is exclusive...
        self.history = self.history[:self.pointer + 1] # this is exclusive also
        self.history.append(url)
        self.pointer += 1
        

    def back(self, steps: int) -> str:
        # we want to find the minimum between (curr - steps) and 0
        self.pointer = max(0, self.pointer - steps)
        return self.history[self.pointer]

    def forward(self, steps: int) -> str:
        # we want to find the maximum between (curr + steps) and pointer 
        self.pointer = min(len(self.history) - 1, self.pointer + steps)
        return self.history[self.pointer]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)