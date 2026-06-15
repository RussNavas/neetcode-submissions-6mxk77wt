func orangesRotting(grid [][]int) int {
    ROWS, COLS := len(grid), len(grid[0])
    fresh := 0
    time := 0
    q := [][]int{}

    for r := 0; r < ROWS; r++ {
        for c := 0; c < COLS; c++ {
            if grid[r][c] == 1 {
                fresh++
            }else if grid[r][c] == 2{
                q = append(q, []int{r, c})
            }
        }

    }

    dirs := [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}

    for fresh > 0 && len(q) > 0{
        qLen := len(q)
        for i := 0; i < qLen; i++ {
            curr := q[0]
            q = q[1:]
            r, c := curr[0], curr[1]

            for _, dir := range dirs{
                dr, dc := dir[0], dir[1]
                nr, nc := r + dr, c + dc

                if nr < 0 || nc < 0 || nr == ROWS || nc == COLS || grid[nr][nc] != 1{
                    continue
                }
                grid[nr][nc] = 2
                q = append(q, []int{nr, nc})
                fresh--
            }
        }
        time++
    }
    if fresh > 0 {
        return -1
    } else{
        return time
    }
}
