class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums)+1)]
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for key, val in freq.items():
            buckets[val].append(key)

        res = []
        for i in range(len(buckets)-1, -1, -1):
            if len(res) == k:
                return res
            if len(buckets[i]) > 0:
                for j in range(len(buckets[i])):
                    if len(res) < k:
                        res.append(buckets[i][j])