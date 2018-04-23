# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key = lambda x : x.start)
        maxSameMeeting = 0
        curMeeting = []
        import heapq
        for i in intervals:
            while curMeeting and curMeeting[0] <= i.start:
                heapq.heappop(curMeeting)
            heapq.heappush(curMeeting, i.end)
            maxSameMeeting = max(maxSameMeeting, len(curMeeting))
        return maxSameMeeting
