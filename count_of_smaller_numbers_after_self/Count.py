class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rank = { k : i+1 for i, k in enumerate(sorted(nums))}
        bit = [0]*(len(nums)+1)
        def update(i):
            while i < len(bit):
                bit[i] += 1
                i += (i & -i)
            return
        
        def getSum(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= (i&-i)
            return s
        solution = []
        for num in reversed(nums):
            solution.append(getSum(rank[num] - 1))
            update(rank[num])
        return solution[::-1]

#test
if __name__ == "__main__":
    sol = Solution()
    print sol.countSmaller([5,2,6,1])
