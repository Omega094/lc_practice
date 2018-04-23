class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        result = [a*n**2 + b*n + c for n in nums]
        from collections import deque
        result = deque(result)
        answer = []
        while result:
            if a > 0:
                if result[0] > result[-1]:
                    answer.append(result.popleft())
                else:
                    answer.append(result.pop())
            else:
                if result[0] < result[-1]:
                    answer.append(result.popleft())
                else:
                    answer.append(result.pop())
        if a > 0:
            answer = answer[::-1]
        return answer
