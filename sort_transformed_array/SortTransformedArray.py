class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        if a == 0:
            return map(lambda x: b*x+c, nums)
        axis = float(-b)/float(2*a)
        left = []
        right = []
        ptr = 0
        #Partition the array by their position relative to axis
        while ptr < len(nums):
            val = nums[ptr]
            if val < axis:
                left.append(a*val**2 + b*val + c )
            else:
                right.append(a*val**2 + b*val + c)
            ptr += 1
        #One more processing regarding to a's value 
        if a > 0:
            left.reverse()
        else:
            right.reverse()
        result = []
        leftPtr = 0
        rightPtr = 0
        #Merge the two partitioned array
        while leftPtr < len(left) and rightPtr < len(right):
            if left[leftPtr] < right[rightPtr]:
                result.append(left[leftPtr])
                leftPtr += 1
            else:
                result.append(right[rightPtr])
                rightPtr += 1
        if leftPtr == len(left):
            left = right[rightPtr:]
        else:
            left = left[leftPtr:]
        result = result + left
        return result 

#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.sortTransformedArray([-4, -2, 2, 4],1,3,5)
    print sol.sortTransformedArray([-4, -2, 2, 4],-1,3,5)
