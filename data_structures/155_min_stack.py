## https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.stack = []
        self.min = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if self.min and val <= self.min[0]:
            self.min.appendleft(val)
            return
        self.min.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        
        if self.min[0]==val:
            self.min.popleft()
            return
        self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.min[0], self.min[-1])


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
