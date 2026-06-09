func hasDuplicate(nums []int) bool {
    hashmap := map[int]int{}
    for _, num := range nums{
        if _, ok := hashmap[num]; ok{
            return true
        } else{
            hashmap[num]++
        }
    }
    return false
}
