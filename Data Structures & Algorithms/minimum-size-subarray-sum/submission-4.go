func minSubArrayLen(target int, nums []int) int {
    length := len(nums) + 1
    total := 0
    l := 0
    for r := 0; r < len(nums); r++ {
        total += nums[r]
        for total >= target {
            length = min(length, r - l + 1)
            total -= nums[l]
            l++
        }
    }

    if length == len(nums) + 1{
        return 0
    }
    return length
}
