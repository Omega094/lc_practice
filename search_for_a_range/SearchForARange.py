class Solution(object):

    def searchRange(self, A, target):
        result = []
        if not A:
            return [-1, -1]
        start = 0
        end = len(A) - 1
        mid = 0
        found = False
        while start <= end:
            mid = (start+end)/2
            if A[mid] == target:
                found = True
                break
            if start == end: break
            if A[mid] > target:
                end = mid
            else:
                start = mid + 1
        if not found: return [-1, -1]
        left_bound, right_bound = mid, mid
        while left_bound>0 and  A[left_bound-1] == target:
            left_bound -= 1
        while right_bound<len(A)-1 and  A[right_bound+1] == target:
            right_bound+= 1
        return [left_bound, right_bound]


#test
if __name__ == "__main__":
    sol = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    print sol.searchRange(nums, 8)
    print sol.searchRange(nums, 100)
