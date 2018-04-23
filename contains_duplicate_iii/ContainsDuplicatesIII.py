#The core idea here is to use bucket !!
#Since k can be very large therefore we can't check by counting the diff from -k to k
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        import collections
        if k < 1 or t < 0 : return False
        
        valueDict = collections.OrderedDict()
        for i, num in enumerate(nums):
            #Key is the bucket. 
            key = num//t if t != 0 else num
            for val in (key-1, key, key+1):
                if val in valueDict and abs(valueDict[val] - num) <=  t:
                    return True
            #Use a ordered dict to save space, good !!
            if len(valueDict) >= k:
                valueDict.popitem(last = False)
            valueDict[key] = num
            #print valueDict
        return False
