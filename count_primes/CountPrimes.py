class Solution(object):
    def countPrimes(self, n):
        isPrime = [True] * max(n, 2)
        isPrime[0] = False
        isPrime[1] = False
        x = 2
        while x**2 < n:
            if isPrime[x]:
                #Start from x*x 
                #Don't need to start from x
                #Since x*(anythin value smaller than x) has been set to false
                #already 
                #This reduces the time complexity 
                p = x*x
                while p < n:
                    isPrime[p] = False
                    p += x
            x += 1
        return sum(isPrime)

