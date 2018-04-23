class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1: return True
        end = num/2
        start = 1
        mid = (end + start) / 2
        while start <= end :
            val = mid**2 
            if val == num:
                return True
            if val > num : 
                end = mid-1
            else:
                start = mid+ 1
            mid = (end + start) / 2
        return False

#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.isPerfectSquare(94)
    print sol.isPerfectSquare(94**2)
