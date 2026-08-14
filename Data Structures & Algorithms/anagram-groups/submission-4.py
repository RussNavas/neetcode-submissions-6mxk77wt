class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for s in strs:
            cannonical = str(sorted(s))
            if cannonical in hash_map:
                hash_map[cannonical].append(s)
                continue
            hash_map[cannonical] = [s]
        return list(hash_map.values())