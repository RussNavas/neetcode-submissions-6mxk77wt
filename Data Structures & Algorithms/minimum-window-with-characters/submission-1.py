class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        window, ft = {}, {}
        for c in t:
            ft[c] = ft.get(c, 0) + 1
        
        have, need = 0, len(ft)
        res, resLen = [-1, -1], float("inf")

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in ft and window[c] == ft[c]:
                have += 1
            
            while have == need:
                window_size = r - l + 1
                if window_size < resLen:
                    res = [l, r]
                    resLen = window_size
                
                window[ s[l] ] -= 1
                if s[l] in ft and window[ s[l] ] < ft[ s[l] ]:
                    have -= 1
                l += 1
        l, r = res
        return s[ l: r+1 ] if resLen != float("inf") else ""
            