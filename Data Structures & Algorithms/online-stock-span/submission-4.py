class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        index = 1
        while self.stack and price >= self.stack[-1][0]:
            index += self.stack.pop()[1]
        self.stack.append([price, index])

        return index


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)