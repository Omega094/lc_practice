class Solution(object):
    def wiggleMaxLength(self, nums):
        from collections import deque
        if len(nums) <= 1: return len(nums)
        if all(x == nums[0]  for x in nums) : return 1
        diff = deque([nums[i] - nums[i-1] for i in xrange(1, len(nums))])
        total = 1
        current = diff.popleft()
        while diff:
            val = diff.popleft()
            if val * current < 0 :
                total += 1
                current = val
        return total +1

#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8])
