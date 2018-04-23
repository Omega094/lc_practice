class Solution(object):

    #There is a timeout if you use pyhton.
    def permutationHelper(self, n, k, currentString, currentList):
        if len(currentList) == n:
            self.counter += 1
            if self.counter == k:
                print currentList
            return 
        for i in range (len(currentString)):
            self.permutationHelper(n, k, currentString[:i]+currentString[i+1:], currentList + [currentString[i]])


    def getPermutation(self, n, k):
        self.counter = 0
        currentList = []
        currentString = ""+"".join([str(i) for i in range(1, n+1)])
        self.permutationHelper(n, k, currentString, currentList)

    #mathematical solution. 
    def getPermutation_fast(self, n, k):
        nums = [1,2,3,4,5,6,7,8,9]
        factorial = 1 
        for i in range (1,n): factorial *= i
        result = ''
        for i in reversed(range(n)):
            currentDigit = str(nums[k / factorial])
            result += currentDigit
            nums.remove(nums[k / factorial])
            if i != 0:
                factorial /= i
                k %= factorial
        return result


#test: 
if __name__ == "__main__":
    sol = Solution()
    print sol.getPermutation(3,5)
    print sol.getPermutation_fast(3,5)
