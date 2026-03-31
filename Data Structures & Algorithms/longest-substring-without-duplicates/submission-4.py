class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        max_len = 1
        window = set(s[0])
        L = 0
        for R in range(1, len(s)):
            while s[R] in window:
                window.remove(s[L])
                L += 1
            window.add(s[R])
            max_len = max(max_len, len(window))
        return max_len