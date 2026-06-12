class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        visited = set()
        start_color = image[sr][sc]
        def dfs(image, r, c, visited):
            if ( min(r, c) < 0 or
                r == ROWS or c == COLS or
                (r, c) in visited or 
                image[r][c] != start_color):
                return

            visited.add((r, c))
            image[r][c] = color
            delta = [[0, 1],[0, -1], [1, 0], [-1, 0]]
            for coord in delta:
                dr, dc = coord
                newr, newc = r + dr, c + dc
                dfs(image, newr, newc, visited)
            return image
        return dfs(image, sr, sc, visited)