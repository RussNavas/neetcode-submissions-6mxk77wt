class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        l = 0
        r = 0
        for i in range(len(s)):
            # odd length
            oddL, oddR = self.helper(s, i, i)
            if (oddR - oddL + 1) > longest:
                longest = (oddR - oddL + 1)
                l = oddL
                r = oddR

            # even length
            evenL, evenR = self.helper(s, i, i + 1)
            if (evenR - evenL + 1) > longest:
                longest = (evenR - evenL + 1)
                l = evenL
                r = evenR
        return s[l:r+1]
    
    def helper(self, s, l, r):
        maxLength = 0
        maxl, maxr = 0, 0
        while l >=0 and r < len(s) and s[l] == s[r]:
            if maxLength < (r - l + 1):
                maxLength = (r - l + 1)
                maxl = l
                maxr = r
            l -= 1
            r += 1
        return maxl, maxr