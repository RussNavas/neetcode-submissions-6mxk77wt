class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
    
        def getW(xi, yi, xj, yj):
            return abs(xi - xj) + abs(yi - yj)
        
        adj = {}
        for x, y in points:
            if (x, y) not in adj:
                adj[(x, y)] = []
        
        for xi, yi in adj.keys():
            for xj, yj in points:
                if (xi, yi) == (xj, yj):
                    continue
                w = getW(xi, yi, xj, yj)
                adj[(xi, yi)].append([w, (xj, yj)])
                adj[(xj, yj)].append([w, (xi, yi)])
        res = 0
        visit = set()
        minHeap = [[0, tuple(points[0])]]
        while len(visit) < len(points):
            cost, i = heapq.heappop(minHeap)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minHeap, [neiCost, nei])
        return res