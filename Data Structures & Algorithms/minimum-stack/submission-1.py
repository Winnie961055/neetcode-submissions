class MinStack:

    def __init__(self):
        
        self.numberStack = []

        self.smallestStack = []

    def push(self, val: int) -> None:
        
        self.numberStack.append(val)
        if self.smallestStack == [] or val <= self.smallestStack[-1]:
            self.smallestStack.append(val)


    def pop(self) -> None:
        
        removed = self.numberStack.pop()
        if removed == self.smallestStack[-1]:
            self.smallestStack.pop()

    def top(self) -> int:
        
        return self.numberStack[-1]

    def getMin(self) -> int:

        return self.smallestStack[-1]
        
