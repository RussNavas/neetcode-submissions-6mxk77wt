func kClosest(points [][]int, k int) [][]int {

    sortedPoints := QuickSort(points, 0, len(points)-1)
    return sortedPoints[:k]

}


func CalcDist(point []int) int {

    dist := (point[0] * point [0]) + (point[1] * point[1])
    return dist
}

func QuickSort(arr [][]int, s, e int) [][]int {
    if ( e - s + 1 <= 1){
        return arr
    }

    left := s
    pivot := arr[e]

    for i := s; i < e; i++ {
        if CalcDist(arr[i]) < CalcDist(pivot){
            temp := arr[left]
            arr[left] = arr[i]
            arr[i] = temp
            left++
        }
    }

    arr[e] = arr[left]
    arr[left] = pivot

    QuickSort(arr, s, left-1)
    QuickSort(arr, left+1, e)
    return arr
}
