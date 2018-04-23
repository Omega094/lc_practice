class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        #Total area of the two rectangles. 
        totalArea = (C-A)*(D-B) + (G-E)*(H-F)
        #Subtracted by common area
        # min_of_head - max_of_tail 
        return totalArea - max(min(C, G) - max(A, E), 0) * max(min(D, H) - max(B, F), 0)


#Test:
if __name__ == "__main__":
    sol = Solution()
    print sol.computeArea(-3,0,3,4,0,-1,9,2)