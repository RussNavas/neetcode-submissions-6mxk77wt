class Solution:
    def climbStairs(self, n: int) -> int:
        """
        n is the number of steps
        options:
            take 1 or 2 steps at once
        return: number of distinct ways to climb to the top of the staircase

        notes:
        there is 1 way to take 1 step 
        there are 2 ways to take 2 steps i.e. 1 + 1 or 2

        recurance relation = f(n - 1) + f(n - 2)
        """

        memo = {}
        def bfs(n):
            if n <= 2:
                return n
            
            if n in memo:
                return memo[n]
            
            memo[n] = bfs(n-1) + bfs(n-2)
            return memo[n]
        return bfs(n)