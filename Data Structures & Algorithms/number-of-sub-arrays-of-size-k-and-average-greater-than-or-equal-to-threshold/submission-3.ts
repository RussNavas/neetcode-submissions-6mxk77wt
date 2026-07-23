class Solution {
    /**
     * @param {number[]} arr
     * @param {number} k
     * @param {number} threshold
     * @return {number}
     */
    numOfSubarrays(arr: number[], k: number, threshold: number): number {
        let total = 0;
        let count = 0;
        for (let i = 0; i < k-1; i++){
            total += arr[i];
        }

        for (let l = 0; l < arr.length - k + 1; l++) {
            let r = (l + k - 1)
            total += arr[r];
            let avg = total / k;
            if (avg >= threshold) {
                count++;
            }
            total -= arr[l];
        }
        return count
    }
}
