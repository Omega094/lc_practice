class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        from collections import defaultdict
        valueDict = defaultdict(list)
        for i in xrange(0, len(nums)):
            for j in xrange(i+1, len(nums)):
                valueDict[nums[i] + nums[j]].append((i, j))
        result = set()
        for i in xrange(0, len(nums)):
            for j in xrange(i+1, len(nums)):
                twoSum = nums[i] + nums[j]
                if target - twoSum in valueDict:
                    for pair in valueDict[target-twoSum]:
                        if j < pair[0]:
                            result.add(tuple(sorted([nums[i], nums[j], nums[pair[0]], nums[pair[1]]])))
        return map(list, result)
        
