class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        minHeap = [[grid[0][0], (0, 0)]] # [weight, (r, c)]
        visit = set()
        while minHeap:
            for _ in range(len(minHeap)):
                w1, n1 = heapq.heappop(minHeap)
                if n1 in visit:
                    continue
                visit.add(n1)
                if n1[0] == ROWS - 1 and n1[1] == COLS - 1:
                    return w1

                for dr, dc in DIRS:
                    maxVal = w1
                    nr, nc = n1[0] + dr, n1[1] + dc
                    if (min(nr, nc) < 0 or nr == ROWS or nc == COLS or
                        grid[nr][nc] in visit):
                        continue
                    maxVal = max(maxVal, grid[nr][nc])
                    heapq.heappush(minHeap, [maxVal, (nr, nc)])