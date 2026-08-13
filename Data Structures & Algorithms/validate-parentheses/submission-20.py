class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {")":"(", "}": "{", "]": "["}
        stack = []
        for c in s:
            print(stack)
            if c not in hash_map:
                stack.append(c)
            elif not stack or stack[-1] != hash_map[c]:
                return False

            else:
                stack.pop()
        return len(stack) == 0


        