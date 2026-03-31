class MinStack:

    def __init__(self):
        self._stack = []
        self._minStack = []
        

    def push(self, val: int) -> None:
        self._stack.append(val)
        val = min(val, self._minStack[-1] if self._minStack else val)
        self._minStack.append(val)
        

    def pop(self) -> None:
        self._stack.pop()
        self._minStack.pop()
        

    def top(self) -> int:
        return self._stack[-1]
        

    def getMin(self) -> int:
        return self._minStack[-1]

        
