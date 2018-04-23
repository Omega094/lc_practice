class Solution(object):

    def topKFrequent(self, nums, k):
        from collections import Counter
        count = Counter(nums)
        print count.most_common(k)
        return sorted(count, key = count.get, reverse = True)[:k]
    
    #Below is linear solution
    #Just recreate a counter to num dict
    #then count from n to 1 and get the value
    def topKFrequent(self, nums, k):
        count = collections.Counter(nums)
        counterToNum = collections.defaultdict(list)
        for num, freq in count.iteritems():
            counterToNum[freq].append(num)
        length = len(nums)
        result = []
        for n in xrange(length, -1, -1):
            values = counterToNum[n]
            for val in values:
                result.append(val)
                if len(result) == k:
                    return result
        return 


#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.topKFrequent([1,1,1,2,2,3], 2)
