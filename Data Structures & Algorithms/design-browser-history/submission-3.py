class BrowserHistory:
    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.pointer = 0

    def visit(self, url: str) -> None:
        self.stack = self.stack[:self.pointer + 1] #stop at this, discard all after this
        self.stack.append(url) # add url to the end now
        self.pointer = len(self.stack) - 1 #update pointer

    def back(self, steps: int) -> str:
        self.pointer = max(0, self.pointer - steps)
        return self.stack[self.pointer]

    def forward(self, steps: int) -> str:
        self.pointer = min(len(self.stack) - 1, self.pointer + steps)
        return self.stack[self.pointer]        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)