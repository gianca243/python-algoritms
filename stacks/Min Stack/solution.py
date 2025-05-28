class MinStack:

    def __init__(self):
        self.stk = []
        self.low_stk = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if len(self.low_stk) == 0:
            self.low_stk.append(val)
        else:
            self.low_stk.append(min(self.low_stk[-1], val))

    def pop(self) -> None:
        self.low_stk.pop()
        self.stk.pop()

    def top(self) -> int:
        if len(self.stk) > 0:
            return self.stk[-1]
        return None

    def getMin(self) -> int:
        if len(self.low_stk) > 0:
            return self.low_stk[-1]
        return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
