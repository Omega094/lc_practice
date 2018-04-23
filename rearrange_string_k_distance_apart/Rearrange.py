#The core idea is 
#1: The same idea as sort a k-nearly sorted list. 
#   That's why we seperate/group the chars by blocks.
#2: The greedy idea. 
#   The greedy idea is what makes seperating by block works. 
#   Since the char with the most freq needs to be seperated by k 
#   at least, therefore each one with less frea should be only packed into
#   the first max_freq-1 blocks. 

import heapq
class Solution(object):
 
    def rearrangeString(self, s, k):
        """
        :type str: str
        :type k: int
        :rtype: str
        """
        from collections import Counter
        counter = Counter(s)
        char_with_count = []
        for c, freq in counter.iteritems():
            char_with_count.append((freq, c))
        char_with_count.sort(reverse = True)
        max_freq = char_with_count[0][0]
        block = [[] for _ in xrange(max_freq)]
        blockNum = 0
        for char in char_with_count:
            for _ in xrange(char[0]):
                block[blockNum].append(char[1])
                blockNum = (blockNum + 1) % max(max_freq-1, char[0])
        #This part is very important to understand. 
        for i in xrange(max_freq-1):
            if len(block[i]) < k:
                return ""
        return "".join(map(lambda x: "".join(x), block))

    def rearrangeString_heap(self, str, k):
        """
        :type str: str
        :type k: int
        :rtype: str
        """
        if k == 0:
            return str
        from collections import Counter
        counter = Counter(str)
        heap = []
        for c, count in counter.iteritems():
            heap.append([-1*count, c])
        heapq.heapify(heap)
        result = []
        while heap:
            used = []
            for _ in xrange(min(k, len(str) - len(result))):
                if not heap: return ""
                curr = heapq.heappop(heap)
                result.append(curr[1])
                curr[0] += 1
                if curr[0] < 0:
                    used.append(curr)
            for pair in used:
                heapq.heappush(heap,pair)
        return "".join(result)



#test
if __name__ == "__main__":
    sol = Solution()
    print sol.rearrangeString("aabbcc", 3)
    print sol.rearrangeString_heap("aabbcc", 3)
