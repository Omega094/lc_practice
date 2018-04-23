    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type size: int
        """
        self.data = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.data
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        import random
        randomList = []
        listCopy = self.data[:]
        for i in range(len(listCopy)):
            idx = random.randint(0, len(listCopy)-1)
            listCopy[idx], listCopy[-1] = listCopy[-1], listCopy[idx]
            randomList.append(listCopy.pop())
        return randomList
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
