# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        mid = (start + end) / 2
        while start < end:
            mid = (start + end) / 2
            if not isBadVersion(mid) and isBadVersion(mid+1):
                return mid + 1
            if not isBadVersion(mid):
                start = mid
            else:
                end = mid
        return mid

