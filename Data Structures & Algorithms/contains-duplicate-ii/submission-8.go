func containsNearbyDuplicate(nums []int, k int) bool {
    hashmap := make(map[int]bool)
    l := 0
    for r, val := range nums {
        if r - l > k {
            delete(hashmap, nums[l])
            l++
        }
        if exist := hashmap[val]; exist{
            return true
        }
        hashmap[val] = true
    }

    return false


}
