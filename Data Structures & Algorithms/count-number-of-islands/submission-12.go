func numIslands(grid [][]byte) int {

    ROWS, COLS := len(grid), len(grid[0])
    
    islands := 0

    for r := 0; r < ROWS; r++ {
        for c:= 0; c < COLS; c++ {
            if grid[r][c] == '1'{
                islands += bfs(r, c, grid)
            }
        }
    }
    return islands
}

func bfs(r, c int, grid [][]byte) int {
    ROWS, COLS := len(grid), len(grid[0])
    island := 0
    q := [][]int{{r, c}}
    dirs := [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
    for len(q)> 0{
        r, c := q[0][0], q[0][1]
        grid[r][c] ='0'
        q = q[1:]
        for _, coord := range dirs {
            dr, dc := coord[0], coord[1]
            nr, nc := r + dr, c + dc
            if nr < 0 || nc < 0 || nr == ROWS || nc == COLS || grid[nr][nc] == '0' {
                continue
            }

            q = append(q, []int{nr, nc})
            grid[nr][nc] = '0'

        }
    }
    island++
    return island
}
