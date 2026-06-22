func numIslands(grid [][]byte) int {
    islands := 0
    ROWS, COLS := len(grid), len(grid[0])


    bfs := func(r, c int) int {

        q := [][]int{{r, c}}
        for len(q) > 0 {
            q_len := len(q)
            for i := 0; i < q_len; i++ {
                coords := q[0]
                q = q[1:]

                r, c := coords[0], coords[1]

                dirs := [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}

                for _, dir := range dirs{
                    dr, dc := dir[0], dir[1]

                    nr, nc := r + dr, c + dc
                    if nr < 0 || nc < 0 || nr == ROWS || nc == COLS || grid[nr][nc] == '0'{
                        continue
                    }

                    q = append(q, []int{nr, nc})
                    grid[nr][nc] = '0'
                }
            } 
        }
        return 1
    }

    for r := 0; r < ROWS; r++{
        for c:= 0; c < COLS; c++{
            if grid[r][c] == '1'{
                islands += bfs(r, c)
            }
        }
    }
    return islands
}
