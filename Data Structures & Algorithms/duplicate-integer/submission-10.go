func hasDuplicate(nums []int) bool {
    hashmap := make(map[int]bool)
    for _,n := range nums{
        if hashmap[n] == true{
            return true
        }
        hashmap[n] = true
    }
    return false
}
