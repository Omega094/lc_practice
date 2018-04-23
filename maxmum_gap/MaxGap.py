class Solution(object):

 

    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MIN = 0
        MAX = 1
        if len(nums) < 2 or max(nums)-min(nums) == 0:   # in case bsize == 0
            return 0
        maxNum,minNum,bucketLength = max(nums),min(nums),len(nums)
        #Now we need to compute the bucket depth
        bucketDepth = ((maxNum - minNum + 1.0) / bucketLength)
        buckets = [[float("inf"), -float("inf")] for i in xrange(bucketLength+1)]
        #print buckets
        for num in nums:
            bucketLocation = int((num - minNum)/bucketDepth)
            #print bucketLocation
            buckets[bucketLocation][MIN] = min(buckets[bucketLocation][MIN], num)
            buckets[bucketLocation][MAX] = max(buckets[bucketLocation][MAX], num)
        prev = buckets[0][MAX]
        maxDiff = 0
        for bucket in buckets[1:]:
            if bucket != [float("inf"), -float("inf")]:
                maxDiff = max(maxDiff, bucket[MIN] - prev)
                prev = bucket[MAX]
        return maxDiff
#test:
if __name__ == "__main__":
    sol = Solution()
    arr = [3,6,9,1]
    print  "This is the max gap", sol.maximumGap(arr)
