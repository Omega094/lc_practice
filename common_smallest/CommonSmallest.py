class Solution(object):
    def commonSmallest(self, lsts):
        return min(list((reduce( lambda  x , y : set(x) & set(y) , lsts))))

#test
if __name__ == "__main__":
    sol = Solution()
    print sol.commonSmallest( [[1,2,3],[2,3,4],[2,3,5,5]] )
