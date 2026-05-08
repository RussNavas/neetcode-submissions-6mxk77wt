class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            print(stack)
            if op == '+':
                num1, num2 = stack[-1], stack[-2]
                stack.append(num1 + num2)
            elif op == 'D':
                num = stack[-1]
                num *= 2
                stack.append(num)
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)