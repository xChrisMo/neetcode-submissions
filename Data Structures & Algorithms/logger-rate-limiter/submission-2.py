#messages and timestamp
from collections import deque
class Logger:
    def __init__(self):
        self.rate_store = dict()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.rate_store:
            self.rate_store[message] = timestamp
            return True

        if timestamp - self.rate_store[message] >= 10:
            self.rate_store[message] = timestamp
            return True

        else:
            return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
