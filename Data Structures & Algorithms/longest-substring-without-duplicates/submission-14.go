func lengthOfLongestSubstring(s string) int {
	hashSet := make(map[byte]bool)
    maxLen := 0
    l := 0
    for r := 0; r < len(s); r++ {
        if  _, exist := hashSet[s[r]]; exist {
            for hashSet[s[r]] {
                delete(hashSet, s[l])
                l++
            }
        }
        hashSet[s[r]] = true
        maxLen = max(maxLen, r - l + 1)
    }
    return maxLen
}
