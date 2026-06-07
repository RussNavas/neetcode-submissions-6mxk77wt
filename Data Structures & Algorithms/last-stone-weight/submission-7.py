class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            heap.append(-1 * s)
        heapq.heapify(heap)

        while len(heap) >= 2:
            s1 = heapq.heappop(heap) * -1
            s2 = heapq.heappop(heap) * -1
            if s1 > s2:
                s1 -= s2
                heapq.heappush(heap,( s1 * -1))
            elif s2 > s1:
                s2 -= s1
                heapq.heappush(heap, (s2 * -1))
            else:
                continue
        if heap:
            return heap.pop() * -1
        return 0
