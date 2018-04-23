# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

#Idea is just check how many interval overlapping in the same time
import heapq
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        ongoingMeetings = []
        heapq.heapify(ongoingMeetings)
        if not intervals: return 0
        intervals.sort(key = lambda x: x.start)
        maxOverlap = 0
        for interval in intervals:
            heapq.heappush(ongoingMeetings, interval.end)
            while ongoingMeetings[0] <= interval.start:
                heapq.heappop(ongoingMeetings)
            maxOverlap = max(maxOverlap, len(ongoingMeetings))
        return maxOverlap

