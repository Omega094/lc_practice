class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        stack = []
        minVal = -float('inf')
        for num in preorder:
            if num < minVal : return False
            while stack and num > stack[-1]:
                minVal = stack.pop()
            stack.append(num)
        return True

#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.verifyPreorder([8,3,1,6,4,7,10,14,13])
