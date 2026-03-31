class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        ref = {
            "]":"[",
            ")":"(",
            "}":"{"
        }
        
        for char in s:
            if char not in ref:
                stack.append(char)
                continue
            if not stack or stack[-1] != ref[char]:
                return False
            stack.pop()

        return not stack