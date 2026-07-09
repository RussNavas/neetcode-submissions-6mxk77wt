func maxSubarraySumCircular(nums []int) int {
	
    minSum  := nums[0]
    maxSum  := nums[0]
    total   := 0

    curMinSum := 0
    curMaxSum := 0

    for _, num := range nums {
        total += num
        curMinSum = min(curMinSum, 0)
        curMaxSum = max(curMaxSum, 0)
        
        curMinSum += num
        curMaxSum += num

        minSum = min(curMinSum, minSum)
        maxSum = max(curMaxSum, maxSum)
    }

    if maxSum > 0 {
        return max(maxSum, total - minSum)
    }
    return maxSum
}
