class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        def dist(coord):
            x = coord[0]
            y = coord[1]
            d_2 = x**2 + y**2
            return [d_2, coord]
        
        for point in points:
            tup = dist(point)
            heap.append(tup)
        
        heapq.heapify(heap)
        res = []
        for _ in range(k):
            tup = heapq.heappop(heap)
            res.append(tup[1].copy())
        return res
        
        