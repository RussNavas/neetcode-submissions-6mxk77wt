class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (min(r, c) < 0 or r == ROWS or c == COLS or
            board[r][c] != word[i] or board[r][c] == "#"):
                return False
            
            board[r][c] = '#'
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if dfs(nr, nc , i + 1):
                    board[r][c] = word[i]
                    return True
                    
            board[r][c] = word[i]
            return False
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False