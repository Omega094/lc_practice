import operator
class Solution(object):
    def calculate(self, a, b, op):
        operatorDict = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.div}
        return operatorDict[op](a,b)
    
    def dfsHelper(self, nums, ops):
        if not ops:
            return [nums[0]]
        ans = []
        for x in xrange(len(ops)):
            left = self.dfsHelper(nums[:x+1],ops[:x])
            right = self.dfsHelper(nums[x+1:], ops[x+1:])
            for l in left:
                for r in right:
                    ans.append(self.calculate(l, r, ops[x]))
        return ans

    def diffWaysToCompute(self,input):
        import re
        input = re.split('(\D)', input)
        nums = []
        ops = []
        for x in input:
            if x.isdigit():
                nums.append(int(x))
            else:
                ops.append(x)
        return self.dfsHelper(nums, ops)

#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.diffWaysToCompute("2*3-4*5")
