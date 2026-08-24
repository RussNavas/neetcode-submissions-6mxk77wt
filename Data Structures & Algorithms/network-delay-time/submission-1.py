class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = {}
        for i in range(1, n+1):
            adjList[i] = []

        for s, d, w in times:
            adjList[s].append([w, d])
        
        minHeap = [[0, k]]
        shortest = {}
        time = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue
            time = max(time, w1)
            shortest[n1] = w1
            for w2, n2 in adjList[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap,[w1 + w2, n2])
        
        return time if len(shortest) == n else -1