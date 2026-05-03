class MinStack:

    stack:list
    localMins: list

    def __init__(self):
        self.stack = []
        self.localMins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.localMins) == 0:
            self.localMins.append(val)
        elif val < self.localMins[-1]:
            self.localMins.append(val)
        else:
            self.localMins.append(self.localMins[-1])
        

    def pop(self) -> None:
        self.stack.pop()
        self.localMins.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.localMins[-1]

        
