class StockSpanner:

    def __init__(self):
        self.stack = [] #price, 1

    def next(self, price: int) -> int:
        curr = 1
        while self.stack and price >= self.stack[-1][0]:
            curr += self.stack.pop()[1]

        self.stack.append([price, curr])
        return curr



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)