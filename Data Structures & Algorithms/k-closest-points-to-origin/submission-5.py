class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            heap.append(self.dist_from_origin(p))
        heapq.heapify(heap)
        res = []
        for i in range(k):
            point = heapq.heappop(heap)[1]
            res.append(point)
        return res
    
    def dist_from_origin(self, point: List[int]):
        x, y = point
        d_2 = x**2 + y**2
        return (d_2, point)