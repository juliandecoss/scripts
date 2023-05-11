class MinStack:

    def __init__(self):
        self.stack = []
        self.last_index = len(self.stack)-1

    def push(self, val: int) -> None:
        self.stack.append(val)
        return

    def pop(self) -> None:
        self.stack.pop(self.last_index)
        return

    def top(self) -> int:
        return self.stack[self.last_index]

    def getMin(self) -> int:
        return min(self.stack)