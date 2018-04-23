class Solution(object):
    def strToBitMap(self, s):
        bitMap = [0 for _ in xrange(26)]
        from collections import Counter
        count = Counter(s)
        for c in count.keys():
            bitMap[ord(c) - ord("a")] =count[c]
        return tuple(bitMap)
        
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = []
        from collections import defaultdict
        aDict = defaultdict(list)
        for s in strs:
            bitMap = self.strToBitMap(s)
            aDict[bitMap].append(s)
        return aDict.values()
