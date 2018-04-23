# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        #for each point 
        maxPtrOnLine = 0
        for point in points:
            slopeTable = {}
            extraCounter = 0
            for connectPoint in points:
                if connectPoint is not point:
                    if not (connectPoint.x == point.x and connectPoint.y == point.y) :
                        if connectPoint.x == point.x:
                            slope = float("inf")
                        else:
                            slope = float((connectPoint.y - point.y))/float((connectPoint.x - point.x))
                        slopeTable[slope] = slopeTable.get(slope, 1) + 1
                    else:
                        extraCounter += 1
            if slopeTable.values():
                maxPtrOnLine = max(max(slopeTable.values()) + extraCounter, maxPtrOnLine)
            maxPtrOnLine = max(maxPtrOnLine, extraCounter + 1)
            slopeTable = {}
        return maxPtrOnLine
