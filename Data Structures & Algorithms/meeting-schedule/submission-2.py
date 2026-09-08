"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.end)
        if not intervals:
            return True
        prevEnd = intervals[0].end
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval.start < prevEnd:
                return False
            prevEnd = interval.end
            
        return True
