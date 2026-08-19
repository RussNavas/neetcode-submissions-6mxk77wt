class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(s, open, close):
            if len(s) == n * 2:
                res.append(s)
                return
            
            if open < n:
                dfs(s + "(", open + 1, close)
            if close < open:
                dfs(s + ")", open, close + 1)
        dfs("", 0, 0)
        return res
