#The approach is to 
#1: Check if all rectangles make up the area that is made by four corners
#2: Check if four corners only appears once.
#3: Check if other corners appears twice or forth. 
 
class Solution(object):
 
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict
        cornerDict = defaultdict(int)
        areaSum = 0
        for rec in rectangles:
            x1, y1 , x2, y2 = rec
            areaSum += (x2-x1)*(y2-y1)
            for x, y in [(x1, y1), (x2, y2),(x1, y2), (x2, y1)]:
                cornerDict[(x, y)] += 1

        leftX = min([x[0] for x in rectangles])
        rightX = max([x[2] for x in rectangles])
        upY = min([y[1] for y in rectangles])
        downY = max([y[3] for y in rectangles])
        #Check the area

        if areaSum != (rightX - leftX)*(downY - upY): return False

        corners = [(leftX, upY), (rightX, upY), (leftX, downY), (rightX, downY)]
        for c in [(leftX, upY), (rightX, upY), (leftX, downY), (rightX, downY)]:
            if c not in cornerDict or cornerDict[c] != 1:
                return False
      
        for c , count in cornerDict.iteritems():
            if c not in corners and count % 2 != 0:
                return False
        return True

