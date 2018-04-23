class Solution(object):
    def grayCode(self, n):
        if not n : return [0]
        res = [0,1]
        for i in xrange(2, n +1 ):
            for j in xrange(len(res) -1, -1, -1):
                res.append(res[j] | 1 <<(i-1))
        return res
#test
sol = Solution()
print sol.grayCode(2)
