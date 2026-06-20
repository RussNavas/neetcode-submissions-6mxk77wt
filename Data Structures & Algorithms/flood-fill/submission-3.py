class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        q = deque()
        q.append((sr, sc))
        start_color = image[sr][sc]
        visited = set((sr, sc))
        image[sr][sc] = color

        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (min(nr, nc) < 0 or nr == ROWS or nc == COLS or (nr, nc) in visited or image[nr][nc] != start_color):
                        continue
                    image[nr][nc] = color
                    q.append((nr, nc))
                    visited.add((nr, nc))
        return image