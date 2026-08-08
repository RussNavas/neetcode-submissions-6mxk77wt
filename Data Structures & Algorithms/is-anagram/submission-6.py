class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f1, f2 = {}, {}

        for c in s:
            if c not in f1:
                f1[c] = 1
                continue
            f1[c] += 1
        
        for c in t:
            if c not in f2:
                f2[c] = 1
                continue
            f2[c] += 1
        return f1 == f2