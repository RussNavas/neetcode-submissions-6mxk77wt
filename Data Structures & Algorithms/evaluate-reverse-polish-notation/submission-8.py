class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i].lstrip("-").isdigit():
                stack.append(tokens[i])
            else:
                op = tokens[i]
                num1, num2 = int(stack.pop()), int(stack.pop())
                if op == "+":
                    stack.append(num1 + num2)
                elif op == "-":
                    stack.append(num2 - num1)
                elif op == "*":
                    stack.append(num1 * num2)
                elif op == "/":
                    stack.append(int(num2 / num1)) # truncate to zero
        return int(stack.pop())