func minSubArrayLen(target int, nums []int) int {
    minLen := len(nums) + 1
    l := 0
    total := 0

    for r := 0; r < len(nums); r++ {
        total += nums[r]
        for total >= target {
            minLen = min(minLen, r - l + 1)
            total -= nums[l]
            l++
        }

    }
    if minLen == len(nums) + 1 {
        return 0
    }
    return minLen
}
