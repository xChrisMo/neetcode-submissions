# initialise, start on homepage
# can visit, clears forward..
# back: backtrack / go back a number of steps / urls..
# forward: move forward allowed number of steps ? 

# use a stack, tabs = [homepage], count = 1
# on visit, append from tabs[count], clearing all forwards?, 
#visit: tabs = [homepage, url, url2] -> None

# back: while steps < count: pop, count -= steps | else, stay on homepage

# forward: while steps < end - count, count += steps, else, move to last url 

class BrowserHistory:
    def __init__(self, homepage: str):
        self.tabs = [homepage]
        self.pointer = 0

    def visit(self, url: str) -> None:
        # removing all after pointer when we visit
        self.tabs = self.tabs[:self.pointer + 1]
        self.tabs.append(url)
        self.pointer = len(self.tabs) - 1

    def back(self, steps: int) -> str:
        self.pointer = max(0, self.pointer - steps)
        return self.tabs[self.pointer] 

    def forward(self, steps: int) -> str:
        self.pointer = min(len(self.tabs) - 1, self.pointer + steps)
        return self.tabs[self.pointer] 


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)