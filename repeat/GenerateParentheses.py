class Solution(object):
    
    def helpler(self, l, r, current, res):
        if l > r: return
        if l == r  and l == 0:
            res.append(current)
        print current
        if l > 0 and r >= 0 :
            self.helpler(l-1,r, current+"(", res)
        if r > 0 and l >= 0:
            self.helpler(l, r-1, current+")", res)

    def generateParenthesis(self, n):
        if n == 0:
            return []
        res = []
        self.helpler(n, n, '', res)
        return res


#test
if __name__ == "__main__":
    sol = Solution()
    print sol.generateParenthesis(3)
