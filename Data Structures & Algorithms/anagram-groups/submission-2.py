class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}

        for s in strs:
            s_sorted = "".join(sorted(s))
            if s_sorted not in hashMap:
                hashMap[s_sorted] = [s]
            else:
                hashMap[s_sorted].append(s)

        return list(hashMap.values())