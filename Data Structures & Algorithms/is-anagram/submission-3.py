class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def getFreqmap(s):
            sMap = {}
            for c in s:
                if c not in sMap:
                    sMap[c] = 1
                else:
                    sMap[c] += 1
            return sMap

        sMap = getFreqmap(s)
        tMap = getFreqmap(t)
        return sMap == tMap

        