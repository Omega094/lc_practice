class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) == 0:
            return 0
        position_dict = {}
        max_len = 0
        back_ptr = 0
        front_ptr = 0

        while front_ptr < len(s):
            position_dict[s[front_ptr]] = position_dict.get(s[front_ptr], 0) + 1
            while len(position_dict) > k:
                position_dict[s[back_ptr]] -= 1
                if position_dict[s[back_ptr]] == 0:
                    del position_dict[s[back_ptr]]
                back_ptr += 1
            max_len = max(max_len, front_ptr - back_ptr + 1)
            front_ptr += 1
        return max_len
