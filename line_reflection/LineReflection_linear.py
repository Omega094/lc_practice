class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        from collections import Counter
        points = list(set(map(tuple, points)))
        length = len(points)
        if length == 0: return True
        mid = float(sum( [x[0] for x in points]))/float(length)
        from collections import defaultdict
        distDict = defaultdict(Counter)
        for point in points:
            distDict[point[0] - mid][point[1]] += 1
        for val in distDict:
            #Maximum compare n times, therefore it is still totally O(n)
            if distDict[val] != distDict[-val] : return False
        return True
