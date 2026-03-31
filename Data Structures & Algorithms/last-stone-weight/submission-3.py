class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        maxHeap = stones
        while len(maxHeap) > 1:
            x, y = heapq.heappop_max(maxHeap), heapq.heappop_max(maxHeap)

            if y < x :
                heapq.heappush_max(maxHeap, (x-y))
        stones.append(0)
        return stones[0]
        