class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        max_area = 0
        
        # Loop through each cell in the grid
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # If a land cell (1) is found, perform DFS to calculate the area of the island
                if grid[r][c] == 1:
                    area = self.dfs(r, c, grid)
                    max_area = max(max_area, area)
        
        return max_area

    def dfs(self, r: int, c: int, grid: List[List[int]]) -> int:
        # Base case to terminate recursion
        if not self.is_within_bounds(r, c, grid) or grid[r][c] != 1:
            return 0
        
        # Mark the current land cell as visited
        grid[r][c] = -1
        
        # Define direction vectors for up, down, left, and right
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        area = 1  # Start with the current land cell contributing to the area
        # Recursively call DFS on each neighboring land cell and add their areas
        for d in dirs:
            area += self.dfs(r + d[0], c + d[1], grid)
        
        return area

    def is_within_bounds(self, r: int, c: int, grid: List[List[int]]) -> bool:
        return 0 <= r < len(grid) and 0 <= c < len(grid[0])
