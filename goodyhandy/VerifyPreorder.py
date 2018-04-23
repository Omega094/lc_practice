class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        stack = []
        currentMax = float('-inf')
        for num in preorder:
            if stack and num <= currentMax : return False
            while stack and stack[-1] < num:
                currentMax = max(currentMax, stack.pop())
            stack.append(num)
        return True
