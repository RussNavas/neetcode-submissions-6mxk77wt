class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) < 2:
            return False

        closedToOpen = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        stack = []

        for c in s:
            if c not in closedToOpen:
                stack.append(c)
            else:
                if stack and stack[-1] == closedToOpen[c]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False