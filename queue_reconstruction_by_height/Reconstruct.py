class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import defaultdict
        heightDict = defaultdict(list)
        for h, front in people:
            heightDict[h].append(front)
        for l in heightDict.values():
            l.sort()
        print heightDict 
        result =  [] 
        for  h in sorted(heightDict.keys(), reverse = True):
            for front in heightDict[h]:
                result.insert(front, [h, front])
        return result
   

#test:
sol = Solution()
print sol.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
print sol.reconstructQueue([[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]])
