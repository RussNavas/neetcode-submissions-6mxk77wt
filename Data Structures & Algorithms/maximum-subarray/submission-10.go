func maxSubArray(nums []int) int {
    maxSum := nums[0]
    total := 0
    for _, num := range nums {
        total = max(total, 0)
        total += num
        maxSum = max(maxSum, total)
    }
    return maxSum
}
