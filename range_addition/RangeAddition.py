class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        result = [0]*(length+1)
        if not updates: return result[1:]
        for start, end, val in updates:
            result[start] += val
            #Whatever flows in will finally flow out !!!
            result[end+1] -= val
        summ = 0
        answer = []
        for i in xrange(length):
            summ += result[i]
            answer.append(summ)
        return answer

#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.getModifiedArray(5, [[1,3,2],[2,4,3],[0,2,-2]])
