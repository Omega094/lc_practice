class Solution(object):
    def merge(self, intervals):
        #use :
        #intervals.sort(key = lambda x: x.start )
        #when interval is an object 
        #also , under above case we need to add one more check in the loop.
        intervals.sort()
        result = []
        result.append(intervals[0])
        intervals.pop(0)
        for interval in intervals:
            print interval,result
            if interval[0] <= result[-1][1]:
                #Need to add this check if interval is object
                #if interval[1] > result[-1][1]:
                result[-1][1] = max(interval[1], result[-1][1])
            else:
                result.append(interval)
        return result

    def sortedArrayToBST(self, nums):
        if not nums: return None
        if len(nums) == 1: return TreeNode(nums[0])
        start = 0
        end = len(nums) - 1
        mid = (start + end) / 2
        head = TreeNode(nums[mid])
        head.left = self.sortedArrayToBST(nums[:mid])
        head.right = self.sortedArrayToBST(nums[mid+1:])
        return head
#test:
if __name__ == "__main__":
    sol = Solution()
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    intervals = [[1,4],[1,5]]
    print sol.merge(intervals)


