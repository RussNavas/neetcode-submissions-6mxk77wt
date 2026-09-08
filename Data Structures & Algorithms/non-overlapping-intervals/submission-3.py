class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevEnd = intervals[0][1]
        count = 0
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start >= prevEnd:
                prevEnd = end
            else:
                count += 1
                prevEnd = min(end, prevEnd)
        return count