// Definition for a pair.
// type Pair struct {
//     Key   int
//     Value string
// }

func mergeSort(pairs []Pair) []Pair {
    return mergeSortHelper(pairs, 0, len(pairs)-1)
}

func mergeSortHelper(pairs []Pair, s, e int) []Pair {
    if e-s+1 <= 1 {
        return pairs
    }

    m := ( s + e) / 2
    mergeSortHelper(pairs, s, m)
    mergeSortHelper(pairs, m+1, e)
    merge(pairs, s, m, e)
    return pairs
}

func merge(pairs []Pair, s, m, e int){
    L := make([]Pair, m-s+1)
    R := make([]Pair, e-m)
    copy(L, pairs[s:m+1])
    copy(R, pairs[m+1:e+1])

    i := 0
    j := 0
    k := s

    for i < len(L) && j < len(R){
        if L[i].Key <= R[j].Key{
            pairs[k] = L[i]
            i++
        } else {
            pairs[k] = R[j]
            j++
        }
        k++
    }

    for i < len(L){
        pairs[k] = L[i]
        i++
        k++
    }
    for j < len(R){
        pairs[k] = R[j]
        j++
        k++
    }
}
