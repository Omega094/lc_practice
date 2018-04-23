from collections import Counter

class Solution(object):
    def rearrangeString(self, str, k):
        """
        :type str: str
        :type k: int
        :rtype: str
        """
        count = Counter(str)
        charAndCount = []
        for c, cnt in count.iteritems():
            charAndCount.append((cnt, c))
        charAndCount.sort(reverse = True)
        print charAndCount
        maxCount = charAndCount[0][0]
        blocks = [[] for _ in xrange(maxCount)]
        i = 0
        for freq, char in charAndCount:
            for _ in xrange(freq):
                blocks[i].append(char)
                i = (i+1) % max(freq, maxCount - 1)
        for i in xrange(len(blocks) - 1):
            if len(blocks[i]) < k:
                return ""
                
        return "".join(map(lambda x : "".join(x), blocks))
