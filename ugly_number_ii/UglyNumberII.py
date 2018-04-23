class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Three pointer approach
        #Three pointers, move the pointer that generates the smallest ugly num
        #Note, 
        #Two same pointer might generate same ugly number,
        #In such case we need to move all
        m1 = m2 = m3 = m4 = 0
        result = [1]
        while len(result) < n:
            a1 = result[m1]*2
            a2 = result[m2]*3
            a3 = result[m3]*5
            #a4 = result[m4]*5
            nextNum = min(a1,a2,a3)
            if nextNum == a1:
                m1 += 1
            if nextNum == a2:
                m2 += 1
            if nextNum == a3:
                m3 += 1
            result.append(nextNum)
        print result
        return result[-1]

#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.nthUglyNumber(10)
