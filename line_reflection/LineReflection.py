class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        points = list(set(map(tuple, points)))
        points.sort()
        length = len(points)
        if length == 0: return True
        mid = float(sum( [x[0] for x in points]))/float(length)
        from collections import defaultdict
        distDict = defaultdict(list)
        for point in points:
            distDict[point[0] - mid].append(point[1])
        for val in distDict:
            #Maximum compare n times, therefore it is still totally O(n)
            if distDict[val] != distDict[-val] : return False
        return True
        
#test
if __name__ == "__main__":
    sol = Solution()
    print sol.isReflected([[1,2],[2,2],[1,4],[2,4]])
    print sol.isReflected([[2,0],[2,1],[2,2],[2,3],[2,4],[-2,0],[-2,1],[-2,2],[-2,3],[-2,4]])
