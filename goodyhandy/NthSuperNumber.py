class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        index = [0 for _ in xrange(len(primes))]
        import heapq
        ugly = [1]
        heap = [(p, 0, p) for p in primes]
        heapq.heapify(heap)
        count = 1
        while count < n:
            nextUgly, idx, prime = heapq.heappop(heap)
            if nextUgly != ugly[-1]:
                ugly.append(nextUgly)
                count += 1
            newUgly, idx, prime = prime*ugly[idx+1], idx+1, prime
            heapq.heappush(heap, (newUgly, idx, prime))
        return ugly[-1]
