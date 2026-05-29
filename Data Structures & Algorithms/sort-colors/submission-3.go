func sortColors(nums []int) {
    buckets := []int{0, 0, 0}
    l := 0

    for i := 0; i < len(nums); i++ {
        buckets[nums[i]]++
    }

    for i := 0; i < len(buckets); i++{
        for j := 0; j < buckets[i]; j++{
            nums[l] = i
            l++
        }
    }
}
