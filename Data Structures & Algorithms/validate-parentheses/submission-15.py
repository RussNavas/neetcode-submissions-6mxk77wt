class Solution:
    def isValid(self, s: str) -> bool:
        
        # map closed to open & use a stack to track pairs
        if len(s) < 2:
            return False
        closed_to_open = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        stack = []

        for char in s:
            if char not in closed_to_open:
                stack.append(char)
            else:
                if stack and stack[-1] == closed_to_open[char]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        return False