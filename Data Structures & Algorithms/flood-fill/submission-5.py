class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        ROWS, COLS = len(image), len(image[0])
        start_color = image[sr][sc]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()

        def dfs(r, c):

            if (min(r, c) < 0 or r == ROWS or c == COLS or
                (r, c) in visited or image[r][c] != start_color):
                return
            
            visited.add((r, c))
            image[r][c] = color
            for dr, dc in dirs:
                dfs(r + dr, c + dc)
        
        dfs(sr, sc)
        return image
            
