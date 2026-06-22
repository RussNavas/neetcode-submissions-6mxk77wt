func shortestPathBinaryMatrix(grid [][]int) int {
    ROWS, COLS := len(grid), len(grid[0])
    dirs := [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}}
	if grid[0][0] == 1 || grid[ROWS-1][COLS-1] == 1 {
        return -1
    }

    bfs := func(r, c int) int {
        q := [][]int{{r, c}}
        grid[r][c] = 0

        path := 0

        for len(q) > 0 {
            q_len := len(q)
            for i := 0; i < q_len; i++ {
                coords := q[0]
                r, c = coords[0], coords[1]
                if r == ROWS - 1 && c == COLS - 1{
                    return path + 1
                }
                q = q[1:]

                for _, dir := range dirs{
                    nr, nc := r + dir[0], c + dir[1]
                    if nr < 0 || nc < 0 || nr == ROWS || nc == COLS || grid[nr][nc] == 1 {
                        continue
                    }

                    q = append(q, []int{nr, nc})
                    grid[nr][nc] = 1
                }
            }
            path++
        }

        return -1
    }

    res := bfs(0, 0)
    if res > 0{
        return res
    }
    return -1
}
