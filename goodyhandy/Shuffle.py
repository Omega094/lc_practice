class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type size: int
        """
        self.arr = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.arr
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        import random
        result = []
        arrCopy = self.arr[:]
        while arrCopy:
            idx = random.randint(0, len(arrCopy)-1)
            arrCopy[idx], arrCopy[-1] = arrCopy[-1], arrCopy[idx]
            result.append(arrCopy.pop())
        return result
        
            
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
