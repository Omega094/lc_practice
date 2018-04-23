#Most efficient solution
#Time is O(n**2)
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #put every pair (The index !!!) and their sum into a hash table
        if len(nums) < 4: return []
        from collections import defaultdict
        sumToPair = defaultdict(list)
        nums.sort()
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[i+1:], i+1):
                    #Hash the pair sum with the index. 
                    sumToPair[num1+ num2].append((i, j))

        solution = set()
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[i+1:], i+1):
                T = target - (num1 + num2)
                if T in sumToPair:
                    for pair in sumToPair[T]:
                        #Make sure they are in differnent index. 
                        if pair[0] > j:
                            quadruplet = [nums[i], nums[j], nums[pair[0]], nums[pair[1]]]
                            solution.add(tuple(sorted(quadruplet)))
        return map(list , solution)
        
        
        
