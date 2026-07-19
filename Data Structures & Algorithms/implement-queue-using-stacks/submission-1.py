class MyQueue:
    def __init__(self):
        self.stack = []
        self.stack_2 = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if not self.stack_2:
            while self.stack:
                self.stack_2.append(self.stack.pop())

        return self.stack_2.pop()

    def peek(self) -> int:
        if not self.stack_2:
            while self.stack:
                self.stack_2.append(self.stack.pop())

        return self.stack_2[-1]

    def empty(self) -> bool:
        return not self.stack_2 and not self.stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


# implement queue using stacks

# [1, 2]