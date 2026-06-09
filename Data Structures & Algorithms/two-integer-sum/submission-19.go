func twoSum(nums []int, target int) []int {
    hashMap := make(map[int]int)

    for i, n := range nums{
        complement := target - n
        if ind, ok := hashMap[complement]; ok{
            res := []int{ind, i}
            return res
        }
        hashMap[n] = i
    }
    return nil
}
