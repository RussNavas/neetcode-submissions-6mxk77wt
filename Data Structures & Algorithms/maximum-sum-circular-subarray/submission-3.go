func maxSubarraySumCircular(nums []int) int {
	// Edge case for empty array
    if len(nums) == 0{
        return 0
    }

    // Init global max/min with the 1st element
    globalMax, globalMin := nums[0], nums[0]
    curMax, curMin := 0, 0
    total := 0

    for _, n := range nums{
        // Kadane's logic for Max and Min
        curMax = max(curMax + n, n)
        curMin = min(curMin + n, n)

        total += n

        globalMax = max(globalMax, curMax)
        globalMin = min(globalMin, curMin)
    }

    // If all numbers are negative, globalMax will be max single element.
    // Otherwise, we compare the standard max vs. the circular max (total - globalMin)
    if globalMax > 0 {
        return max(globalMax, total - globalMin)
    }
    return globalMax
}
