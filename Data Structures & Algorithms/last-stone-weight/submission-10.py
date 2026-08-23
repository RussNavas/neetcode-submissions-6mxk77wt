class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            heap.append(s * -1)
        heapq.heapify(heap)
        while len(heap) > 1:
            s1, s2 = heapq.heappop(heap) * -1, heapq.heappop(heap) * -1
            if s1 == s2:
                continue
            elif s1 < s2:
                s2 -= s1
                heapq.heappush(heap, s2 * -1)
            elif s1 > s2:
                s1 -= s2
                heapq.heappush(heap, s1 * -1)
        return heap[0] * -1 if heap else 0