class MinStack:

    def __init__(self):
        self.s = []
        self.min_s = []
        

    def push(self, value: int) -> None:
        self.s.append(value)
        if not self.min_s or value <= self.min_s[-1]:
            self.min_s.append(value)
        

    def pop(self) -> None:
        if self.s[-1]==self.min_s[-1]:
            self.min_s.pop()
        self.s.pop()

        

    def top(self) -> int:
        return self.s[-1]
        

    def getMin(self) -> int:
                return self.min_s[-1]

        
        


