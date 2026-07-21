'''
the trick is to create a minstack that records the min value at this index
so getMin will be constant time



'''
class MinStack:

    def __init__(self):

        self.stack = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        #check the min val of current val
        val = min(val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
        
