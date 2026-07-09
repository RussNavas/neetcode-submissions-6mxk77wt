class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    maxSubarraySumCircular(nums: number[]): number {

        let minSum: number = nums[0]
        let maxSum: number = nums[0]
        let total: number = 0

        let curMin: number = 0
        let curMax: number = 0

        for (let num of nums) {
            total += num
            curMin = Math.min(curMin, 0)
            curMax = Math.max(curMax, 0)

            curMin += num
            curMax += num

            minSum = Math.min(curMin, minSum)
            maxSum = Math.max(curMax, maxSum)
        } 

        if (maxSum > 0) {
            return Math.max(maxSum, total - minSum)
        }

        return maxSum

    }
}
