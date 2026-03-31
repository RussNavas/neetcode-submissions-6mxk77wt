class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        maxHeap = stones
        while len(maxHeap) > 1:
            x, y = heapq.heappop_max(maxHeap), heapq.heappop_max(maxHeap)

            if x != y:
                heapq.heappush_max(maxHeap, abs(x-y))
        stones.append(0)
        return stones[0]
        