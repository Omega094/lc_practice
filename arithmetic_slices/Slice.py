class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3: return 0
        table = [[None, 1] for _ in xrange(len(A))]
        for i in xrange(1, len(A)):
            table[i][0] = A[i] - A[i-1]
        result = 0
        table[0] = [None, 0]
        table[1][1] = 1; 
        for i in xrange(2, len(A)):
            if table[i][0] == table[i-1][0]  :
                table[i][1] = table[i-1][1] + 1
                result += (table[i][1]-1)
        return result 
        
