# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals: return []
        intervals.sort(key = lambda x : x.start)
        result = []
        result.append(intervals[0])
        for i in xrange(1, len(intervals)):
            if intervals[i].start <= result[-1].end:
                result[-1].end = max(result[-1].end , intervals[i].end)
            else:
                result.append(intervals[i])
        return result
