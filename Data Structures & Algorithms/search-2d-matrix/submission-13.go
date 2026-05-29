func searchMatrix(matrix [][]int, target int) bool {

    for r := range matrix {
        if binarySearch(matrix[r], target){
            return true
        }
    }

    return false

}

func binarySearch(arr []int, target int) bool {
    l := 0
    r := len(arr) - 1

    for l <= r {
        m := (r + l) / 2
        if arr[m] == target{
            return true
        }
        if arr[m] < target{
            l = m + 1
        } else {
            r = m - 1
        }
    }
    return false
}
