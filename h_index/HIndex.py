class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        result = 0
        if not citations: return 0
        citations.sort()
        for i in xrange(0, len(citations)):
            if citations[i] >= len(citations) - i :
                return len(citations) - i
        return result


    def hIndex_explicit(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        result = 0
        if not citations: return 0
        citations.sort()
        citations.reverse()
        for i, num in enumerate(citations, 1):
            if num >= i:
                result += 1
            else:
                return result
        return result

    def hIndex_linear(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        length = len(citations)
        counter = [0]*(length+1)
        for num in citations:
            if num >= length:
                counter[length]+= 1
            else:
                counter[num] += 1
        result = 0
        for i in range(length, -1, -1):
            result += counter[i]
            if result >= i: return i
        return 0

#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.hIndex([3, 0, 6, 1, 5])
