class MinStack:
    def __init__(self):
        # initialise 2 arrays
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        #[4,3,1]
        #[4,3,1]
        # 
        if not self.min_stack:
            self.min_stack.append(val)

        else:    
            if val <= self.min_stack[-1]:
                self.min_stack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        # pops normal stack, always would be pop on non empty array
        val = self.stack.pop()
        
        # check if it is also a min in minstack
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        # getting, not popping
        return self.stack[-1]

    def getMin(self) -> int:
        # top element of min_stack
        return self.min_stack[-1]
