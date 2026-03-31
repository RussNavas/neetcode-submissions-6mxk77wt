class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        visited = set()

        def dfs(r, c, i):

            if i == len(word):
                return True

            if(
                not (0 <= r < rows and 0 <= c < cols) or 
                ((r,c) in visited) or
                (word[i] != board[r][c])):
                return False

            visited.add((r,c))

            for dr, dc in dirs:
                if dfs(r + dr, c + dc, i+1):
                    return True

            visited.remove((r,c))

            return False

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False

        