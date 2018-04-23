import sys
sys.path.append("/Users/jinzhao/leetcode/")
from leetcode.common import *
class Solution(object):
    def sortedArrayToBST(self, nums):
        if not nums: return None
        if len(nums) == 1: return TreeNode(nums[0])
        start = 0
        end = len(nums) - 1
        mid = (start + end) / 2
        head = TreeNode(nums[mid])
        head.left = self.sortedArrayToBST(nums[:mid])
        head.right = self.sortedArrayToBST(nums[mid+1:])
        return head

#test
if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,4,5,6,7,8,9,10]
    root = sol.sortedArrayToBST(nums)
    pretty_print_tree(root,[])

