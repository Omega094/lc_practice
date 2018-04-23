class Solution(object):
    def pairCheck(self, num1, num2):
        pairDict = {"1": "1", "8": "8", "6": "9", "9":"6", "0":"0"}
        return pairDict.get(num1, None) == num2

    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        #Base  Case:
        strNum = num
        if num == "1" or num == "8" or num == "69" or num == "96" or num == "0" or num == None:
            return True
        
        #recursive case:
        if not num[1:-1]: 
            newNum = None
        else:
            newNum = (num[1:-1])

        return self.pairCheck(num[0], num[-1]) and self.isStrobogrammatic(newNum)

    def isStrobogrammatic_iterative(self, num):
        left = 0
        right = len(num)-1
        while left <= right:
            if not self.pairCheck(num[left], num[right]):
                return False
            left += 1
            right -= 1
        return True 



#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.isStrobogrammatic("608809")
    print sol.isStrobogrammatic_iterative("608809")
