func maxSubArray(nums []int) int {
    maxSum := nums[0]
    currentSum := 0

    for _, val := range nums{
        if currentSum < 0{
            currentSum = 0
        }
        currentSum += val
        if maxSum < currentSum{
            maxSum = currentSum
        }
    }
    return maxSum
}
