class Solution(object):
    def hIndex_slow(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        citations.reverse()
        count = 0
        for i, num in enumerate(citations, 1):
            if num >= i :
                count += 1 
        return count

    #O(N) solution, 
    # Need to understand it from inside out.
    def hIndex_linear(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        table = [0]*(len(citations) + 1)
        for num in citations:
            if num > len(citations) :
                table[-1] += 1
                continue
            table[num] += 1
        result = 0
        for i in range(len(citations), -1, -1):
            result += table[i]
            if result >= i :
                return i
        return 0
