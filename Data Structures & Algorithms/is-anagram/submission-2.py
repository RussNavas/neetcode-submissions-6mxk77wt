class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd = {}
        td = {}

        for c in s:
            if c not in sd:
                sd[c] = 1
            else:
                sd[c] += 1

        for c in t:
            if c not in td:
                td[c] = 1
            else:
                td[c] += 1

        if sd == td:
            return True
        return False
        