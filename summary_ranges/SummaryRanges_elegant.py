class Solution(object):
 
    def summaryRanges(self, nums):
        ranges = []
        for n in nums:
            if not ranges or n > ranges[-1][-1] + 1:
                ranges.append([])
            if not ranges[-1]:
                ranges[-1].append(n)
            else:
                if ranges[-1][-1] == n: continue
                if len(ranges[-1]) == 1: ranges[-1].append(n)
                else:
                    ranges[-1][-1] = n
        return ['->'.join(map(str, r)) for r in ranges]
