class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        currentSum = 0
        for i in  xrange(0, len(A)):
            currentSum += i*A[i]
        #Now we start rotating 
        print currentSum
        increment = sum(A)
        maxSum = currentSum
        reduceCount = len(A)
        for i in xrange(len(A)-1, 0, -1):
            currentSum += increment
            currentSum -= reduceCount*(A[i])
            maxSum = max(maxSum, currentSum)
        return maxSum
#test:
sol = Solution()
print sol.maxRotateFunction([4,3,2,6])
