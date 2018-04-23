class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        common = set(nums1)&set(nums2)
        result = []
        for num in common:
            result += [num]*min(c1[num], c2[num])
        return result
        
#test
if __name__ == "__main__":
    sol = Solution()
    print sol.intersect([1, 2, 2, 1],[2,2])
