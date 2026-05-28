// Definition for a pair.
// type Pair struct {
//     Key   int
//     Value string
// }

type Solution struct {

}



func QuickSort(pairs []Pair) []Pair {

    if len(pairs) == 0 {
        return pairs
    }

    return Helper(pairs, 0, len(pairs)-1)

}

func Helper(arr []Pair, s, e int) []Pair{
    if (e - s + 1 <= 1){
        return arr
    }

    left := s
    pivot := arr[e]

    for i := s; i < e; i++{
        if (arr[i].Key < pivot.Key){
            temp := arr[left]
            arr[left] = arr[i]
            arr[i] = temp
            left++
        }
    }

    arr[e] = arr[left]
    arr[left] = pivot 

    Helper(arr, s, left-1)
    Helper(arr, left+1, e)
    return arr

}
