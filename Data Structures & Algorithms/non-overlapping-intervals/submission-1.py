class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count = 0
        prevEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if prevEnd > start:
                count += 1
            else:
                prevEnd = end
        return count