class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        totalSet = set()
        for num in nums:
            totalSet.add(num)
        maxCounter = 0
        while totalSet:
            currentNum = totalSet.pop()
            counter = 1
            currentNumDecrement = currentNum
            while currentNum+1 in totalSet:
                counter += 1
                totalSet.remove(currentNum + 1)
                currentNum += 1
            while currentNumDecrement - 1 in totalSet:
                counter += 1
                totalSet.remove(currentNumDecrement - 1)
                currentNumDecrement -= 1
            maxCounter = max(maxCounter , counter)
        return maxCounter

#test
if __name__ == "__main__":
    lst = [100, 4, 200, 1, 3, 2]
    sol = Solution()
    print sol.longestConsecutive(lst)
