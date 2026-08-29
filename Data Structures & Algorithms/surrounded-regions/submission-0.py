class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        ROWS, COLS = len(board), len(board[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # capture unsurrounded regions
        def capture(r, c):

            if min(r, c) < 0 or r == ROWS or c == COLS or board[r][c] != "O":
                return
            
            board[r][c] = 'T'
            for dr, dc in DIRS:
                capture(r + dr, c + dc)

        # capture the surrounded regions
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "O" and
                   ( r in [0, ROWS - 1] or
                    c in [0, COLS - 1])):
                    capture(r, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = "O"