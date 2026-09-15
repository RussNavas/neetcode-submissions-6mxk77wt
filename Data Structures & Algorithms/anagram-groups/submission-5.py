class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for s in strs:
            cannonical = str(sorted(s))
            if cannonical not in hash_map:
                hash_map[cannonical] = [s]
            else:
                hash_map[cannonical].append(s)
        res = []
        for key, val in hash_map.items():
            res.append(val)
        return res