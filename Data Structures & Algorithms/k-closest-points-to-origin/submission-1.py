class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def getDistFromOrigin(coord):
            x, y = coord
            return math.sqrt((x)**2 + (y)**2)

        heap = [] # [ [ dist, [x, y] ] ]
        for pt in points:
            heap.append([-getDistFromOrigin(pt), pt])

        heapq.heapify(heap)

        while len(heap) > k:
            heapq.heappop(heap)
        res = []
        for i in heap:
            res.append(i[1])
        return res