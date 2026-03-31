class Solution:
    def isValid(self, s: str) -> bool:
        parens = {
            ")":"(",
            "]":"[",
            "}":"{"
            }
        stack = []
        for c in s:
            if c in parens:
                if stack and stack[-1] == parens[c]:
                    stack.pop()
                else:
                    return False # the stack is empty or the paren is invalid
            else:
                stack.append(c)
            
        if stack:
            return False
        return True