class Solution(object):
    def readBinaryWatch(self, num):
        return ["%d:%02d" % (h, m) for h in range(12) for m in range(60) if (bin(h) + bin(m)).count("1") == num]

#test
sol = Solution()
print sol.readBinaryWatch(3)
print sol.readBinaryWatch(1)
