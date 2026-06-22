func orangesRotting(grid [][]int) int {
    ROWS, COLS := len(grid), len(grid[0])
    fresh := 0
    q := [][]int{}
    for r := 0; r < ROWS; r++{
        for c := 0; c < COLS; c++{
            if grid[r][c] == 1{
                fresh++
            }else if grid[r][c] == 2{
                q = append(q, []int{r, c})
            }
        }
    }

    if fresh == 0 {
        return 0
    }

    dirs := [][]int{ {1, 0}, {0, 1}, {-1, 0}, {0, -1}}
    time := 0
    for fresh > 0 && len(q) > 0{
        q_len := len(q)
        for i := 0; i < q_len; i++ {
            r, c := q[0][0], q[0][1]
            q = q[1:]

            for _, dir := range dirs{
                dr, dc := dir[0], dir[1]
                nr, nc := r + dr, c + dc
                if nr < 0 || nc < 0 || nr == ROWS || nc == COLS || grid[nr][nc] != 1 {
                    continue
                }

                q = append(q, []int{nr, nc})
                grid[nr][nc] = 2
                fresh--

            }
        }
        time++

    }

    if fresh == 0{
        return time
    }
    return -1
}
