class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sortedNum = sorted(nums)
        rank = {}
        for i, n in enumerate(sortedNum):
            rank[n] = i
        bit = [0]*(len(nums) + 1)
        result = []
        for n in reversed(nums):
            r = rank[n]
            r1 = r ; smallerLeft = 0
            while r1 > 0:
                smallerLeft += bit[r1]
                r1 -= (r1 & -r1)
            r2 = r + 1
            while r2 < len(bit):
                bit[r2] += 1
                r2 += (r2 & -r2)
            result.append(smallerLeft)
        result.reverse()
        return result
