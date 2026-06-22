func maxAreaOfIsland(grid [][]int) int {
    ROWS, COLS := len(grid), len(grid[0])
    maxArea := 0
    dirs := [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}

    bfs := func(r, c int) int {
        q := [][]int{{r, c}}
        grid[r][c] = 0
        area := 1
        for len(q) > 0{
            coord := q[0]
            q = q[1:]
            r, c = coord[0], coord[1]
            for _, dir := range dirs {
                dr, dc := dir[0], dir[1]
                nr, nc := r + dr, c + dc
                if nr < 0 || nc < 0 || nr == ROWS || nc == COLS || grid[nr][nc] == 0{
                    continue
                }
                q = append(q, []int{nr, nc})
                grid[nr][nc] = 0
                area++
            }
        }
        return area
    }

    for r := 0; r < ROWS; r++{
        for c := 0; c < COLS; c++{
            if grid[r][c] == 1 {
                maxArea = max(maxArea, bfs(r, c))
            }
        }
    }


    return maxArea
}
