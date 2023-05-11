from timeit import repeat
from typing import Any


class MaxStack:
    def __init__(self) -> None:
        self.stack =[]
    
    def push(self, element:Any)-> None:
        self.stack.append(element)
        print(self.stack)
        return

    def pop(self,)->Any:
        deleted = self.stack.pop(len(self.stack)-1)
        print(self.stack)
        return deleted

    def top(self)->Any:
        top_value = self.stack[-1]
        print(top_value)
        return top_value
    
    def peekMax(self)->Any:
        maximum = max(self.stack) #.sort()[0]
        print(maximum)
        return maximum
    
    def popMax(self) -> Any:
        new = sorted(self.stack,reverse=True)
        for i in range(len(self.stack)-1,-1,-1):
            value = self.stack[i]
            if value == new[0]:
                self.stack.pop(i)
                break
        print(self.stack)
        return 
stk = MaxStack()
breakpoint()