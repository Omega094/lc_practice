class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        result = 0
        if not citations: return 0
        #citations = citations[::-1]
        length = len(citations)
        if citations[0] >= length: return length
        if citations[-1] <= 1: return citations[-1]
        start = 0
        end = len(citations) - 1
        mid = (start + end) / 2
        while start < end :
            if citations[mid] >= length - mid and citations[mid-1] < length - (mid-1):
                return length - mid
            if citations[mid] < length - mid :
                start = mid + 1
            else:
                end = mid
            mid = (start + end) / 2 
        return length - mid  

#test
if __name__ == "__main__":
    sol = Solution()
    print sol.hIndex([3, 0, 6, 1, 5])
