class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for s in strs:
            cannonical = str(sorted(s))
            if cannonical in hash_map:
                hash_map[cannonical].append(s)
                continue
            hash_map[cannonical] = [s]
        res = []
        for k, v in hash_map.items():
            res.append(v)
        return res