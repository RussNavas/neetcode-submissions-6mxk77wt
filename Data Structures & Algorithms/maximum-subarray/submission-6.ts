class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    maxSubArray(nums: number[]): number {
        let maxSum: number = nums[0];
        let curSum: number = 0;
        for (const num of nums){
            curSum = Math.max(curSum, 0)
            curSum += num
            maxSum = Math.max(maxSum, curSum)
        }
        return maxSum
    }
}
