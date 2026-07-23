class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {boolean}
     */
    containsNearbyDuplicate(nums: number[], k: number): boolean {
        let window: Set<number> = new Set();
        let l = 0;
        for (let r = 0; r < nums.length; r++ ) {
            if (r - l > k) {
                window.delete(nums[l]);
                l++;
            }
            if (window.has(nums[r])){
                return true;
            }
            window.add(nums[r]);
        }
        return false;
    }
}
