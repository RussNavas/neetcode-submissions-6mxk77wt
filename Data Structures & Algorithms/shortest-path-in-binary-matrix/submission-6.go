func shortestPathBinaryMatrix(grid [][]int) int {
	ROWS, COLS := len(grid), len(grid[0])
    if grid[0][0] == 1 || grid[ROWS-1][COLS-1] == 1{
        return -1
    }

    q := [][]int{{0, 0}}
    dirs := [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}, {1, 1}, {-1, 1}, {1, -1}, {-1, -1}}

    time := 1
    for len(q) > 0{
        q_len := len(q)
        for i := 0; i < q_len; i++ {
            curr := q[0]
            q = q[1:]

            r, c := curr[0], curr[1]
            if r == ROWS - 1 && c == COLS - 1{
                return time
            }
            for _, dir := range dirs{
                dr, dc := dir[0], dir[1]
                nr, nc := r + dr, c + dc

                if nr < 0 || nc < 0 || nr == ROWS || nc == COLS || grid[nr][nc] == 1 {
                    continue
                }
                grid[nr][nc] = 1
                q = append(q, []int{nr, nc})
            }
        }
        time++
    }
    return -1
}
