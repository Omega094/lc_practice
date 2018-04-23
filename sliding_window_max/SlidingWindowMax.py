class Solution(object):
    def maxSlidingWindow(self, nums, k):
        import collections
        window = collections.deque()
        result = []
        front = 0
        while front != len(nums):
            while len(window)>0 and (front - window[0][1] >= k):
                window.popleft()
            while len(window)>0 and (window[-1][0] <= nums[front]):
                window.pop()
            window.append((nums[front], front))
            if front >= k-1:
                result.append(window[0][0])
            front += 1
            print window
        return result

    def maxSlidingWindow_elegant(self, nums, k):
        dq = collections.deque()
        ans = []
        for i, num in enumerate(nums):
            while dq and nums[dq[-1]]<= num:
                dq.pop()
            dq.append(i)
            while dq and dq[0] <= i - k:
                dq.popleft()
            if i >= k -1 :
                ans.append(nums[dq[0]])
        return ans


#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)


