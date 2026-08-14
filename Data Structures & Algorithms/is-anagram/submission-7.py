class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f1, f2 = {}, {}
        for c in s:
            f1[c] = f1.get(c, 0) + 1
        
        for c in t:
            f2[c] = f2.get(c, 0) + 1
        
        return f1 == f2