func floodFill(image [][]int, sr int, sc int, color int) [][]int {
    ROWS, COLS := len(image), len(image[0])
    startColor := image[sr][sc]
    if startColor == color{
        return image
    }

    var dfs func(r, c int)
    dfs = func(r, c int){
        if r < 0 || c < 0 || r == ROWS || c == COLS || image[r][c] != startColor{
            return
        }
        image[r][c] = color
        delta := [][]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}
        for _, coord := range delta{
            dr := coord[0]
            dc := coord[1]
            dfs(r + dr, c + dc)
        }
    }

    dfs(sr, sc)
    return image
}
