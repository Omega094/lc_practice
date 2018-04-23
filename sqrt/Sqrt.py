class Solution(object):

    def mySqrt(self, x):
        start = 1
        end = x
        mid = x / 2 + 1
        while start <= end:
            mid = (start + end) / 2
#            print "start ", start, "end ", end, "mid ", mid 
            if mid ** 2 == x : return mid  
            if mid  ** 2 > x: 
                end = mid - 1 
            else: 
                start = mid + 1 
        return end  
            



#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.mySqrt(10)
    print sol.mySqrt(2)

