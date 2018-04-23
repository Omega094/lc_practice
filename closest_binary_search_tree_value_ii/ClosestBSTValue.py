class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        stack = []
        minDist = float('inf')
        closestVal = None
        from collections import deque
        result = deque()
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                result.append(root.val)
                diff = abs(root.val - target)
                if  diff < minDist:
                    minDist = diff
                    closestVal = root.val
                if abs(root.val - target) > minDist and len(result) > 2*k-1:
                    break
                if len(result) > 2*k-1:
                    result.popleft()
                root = root.right 
        result = list(result)
        result.sort(key = lambda x: abs(x-target))
        return result[:k]
