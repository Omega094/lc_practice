#The idea is just to keep two variable 
#c1 is the smallest element before num when you reach each num
#c2 is the second smallest element that comes after c1 before num when you reach each num. 
#Therefore it is trival

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        c1 = float('inf')
        c2 = float('inf')
        for num in nums:
            if num <= c1:
                c1 = num
            elif num <= c2:
                c2 = num
            else:
                return True
        return False
