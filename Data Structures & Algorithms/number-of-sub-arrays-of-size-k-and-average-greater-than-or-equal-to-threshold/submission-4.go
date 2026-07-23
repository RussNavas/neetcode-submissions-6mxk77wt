func numOfSubarrays(arr []int, k int, threshold int) int {
    total := 0
    count := 0

    for i := 0; i < k - 1; i++ {
        total += arr[i]
    }

    for l := 0; l < len(arr) - k + 1; l++  {
        r := l + k - 1
        total += arr[r]
        avg := total / k
        if avg >= threshold {
            count++
        }
        total -= arr[l]
    }
    return count
}
