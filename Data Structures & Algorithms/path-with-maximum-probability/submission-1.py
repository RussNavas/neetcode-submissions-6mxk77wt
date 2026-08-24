import collections
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adjList = collections.defaultdict(list)
        for i in range(len(edges)):
            src, dst = edges[i]
            prob = succProb[i]
            adjList[src].append([prob, dst])
            adjList[dst].append([prob, src])
        
        pq = [(-1, start_node)]
        visited = set()

        while pq:
            prob, cur = heapq.heappop(pq)
            if cur in visited:
                continue
            visited.add(cur)
            if cur == end_node:
                return prob * -1
            
            for nei in adjList[cur]:
                prob_nei, node = nei
                if node in visited:
                    continue
                heapq.heappush(pq, [prob_nei * prob, node])
        return 0