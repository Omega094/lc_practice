class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        arr = [0 for _ in xrange(length+1)]
        for start, end, delta in updates:
            arr[start] += delta
            arr[end+1] -= delta
        result = [0 for _ in xrange(length)]
        counter = 0
        for i, num in enumerate(arr[:-1]):
            counter += num
            result[i] += counter
        return result 
        
