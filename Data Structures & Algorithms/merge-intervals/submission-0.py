class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        for b in intervals[1:]:
            a = merged[-1]
            if a[1] < b[0]:
                merged.append(b)
            else:
                merged[-1][1] = max(a[1], b[1])
        return merged 