class StockSpanner:
    def __init__(self):
        self.stock = [] # store price, index

    def next(self, price: int) -> int:
        i = 1
        while self.stock and price >= self.stock[-1][0]:
            i += self.stock.pop()[1]

        self.stock.append([price, i])

        return i


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)