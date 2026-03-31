class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stack = []
        res = []

        def backtrack(openN, closedN): # where these are ints
            if openN == closedN == n: # the same amount of each paren
                res.append("".join(stack)) # stich it together & append
                return

            if openN < n: # build up the open parenth
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN: # build up the closed parenth
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res
        