class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLen = 0
        table = [[] for _ in xrange(0,  len(nums))]
        for i, num in enumerate(nums):
            print i
            if i == 0:
                table[i].append(0) 
                continue
#            if num > nums[table[i-1][-1]]:
#               table[i] = table[i-1][:] + [i] 
#            else:
            for j in xrange(i-1, -1, -1):
                    if num > nums[table[j][-1]] :
                        if len(table[j]) + 1 > len(table[i]) :
                            print table[j]
                            table[i] = table[j] + [i]                     
            if not table[i]:
                    table[i] = [i]
            maxLen = max(maxLen, len(table[i]))
            print table
        return maxLen

    def lengthOfLIS_simple(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #A list of tuple, (num of increasing iterms, the index of last increasing iterm)
        maxLen = 0
        table = [(1,i) for i in xrange(0,  len(nums))]
        for i, num in enumerate(nums):
            for j in xrange(i-1, -1, -1):
                    if num > nums[table[j][1]] :
                        if table[j][0] + 1 > table[i][0] :
                            table[i] = (table[j][0] + 1, i)
            maxLen = max(maxLen, table[i][0])
        return maxLen 

    def lengthOfLIS_fast(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #A list of tuple, (num of increasing iterms, the index of last increasing iterm)
 
        tails = nums[:]
        size = 0
        for k,x in enumerate(nums):
            i, j= 0, size
            while i != j:
                m = (i + j) / 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
        return size
        
    def lengthOfLIS_binary(self, nums):
        size = len(nums)
        dp = []
        for x in range(size):
            low, high = 0, len(dp) - 1
            #When equals, it increments one, 
            #Therefore it finds the first element that is not smaller than nums[x]
            #Note, this does not really make dp the LIS, think about it. 
            while low <= high:
                mid = (low + high) / 2
                if dp[mid][-1] >= nums[x]:
                    high = mid - 1
                else:
                    low = mid + 1
            if low >= len(dp):
                dp.append([nums[x]])
            else:
                dp[low].append( nums[x])
        print dp
        return len(dp)

#test
if __name__ == "__main__":
    sol = Solution()
    print sol.lengthOfLIS_binary([1,3,6,7,9,4,10,5,6])
    
    print sol.lengthOfLIS_binary([10, 9, 2, 5, 3, 7, 101, 18])
