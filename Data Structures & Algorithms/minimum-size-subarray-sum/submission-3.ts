class Solution {
    /**
     * @param {number} target
     * @param {number[]} nums
     * @return {number}
     */
    minSubArrayLen(target: number, nums: number[]): number {
        let len = nums.length + 1;
        let l = 0;
        let total = 0;
        for (let r = 0; r < nums.length; r++) {
            total += nums[r];
            while (total >= target) {
                len = Math.min(len, r - l + 1);
                total -= nums[l];
                l++;
            }
        }

        if (len === nums.length + 1) {
            return 0;
        }
        return len;

    }
}
