class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    maxSubArray(nums: number[]): number {
        let maxSum = nums[0]
        let total = 0
        for (const num of nums){
            total = Math.max(total, 0)
            total += num
            maxSum = Math.max(maxSum, total)
        }
        return maxSum
    }
}
