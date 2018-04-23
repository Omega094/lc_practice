class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        front_ptr = 0
        back_ptr = 0
        position_dict = {}
        max_len = 0
        STARTINDEX = 0
        ENDINDEX = 1
        while front_ptr < len(s):
            print position_dict
            if s[front_ptr] not in position_dict and len(position_dict) == 2:
                char_keys = position_dict.keys()
                char_front = char_keys[0]
                char_back = char_keys[1]
                if position_dict[char_front][ENDINDEX] < position_dict[char_back][ENDINDEX]:
                    char_back, char_front = char_front, char_back
                max_len = max( max_len, front_ptr - position_dict[char_back][ENDINDEX])
                if position_dict[char_back][ENDINDEX] > position_dict[char_front][STARTINDEX]:
                    position_dict[char_front] = (position_dict[char_back][ENDINDEX]+1, position_dict[char_front][ENDINDEX]) 
                del position_dict[char_back]
                position_dict[s[front_ptr]] = (front_ptr, front_ptr)
            else:
                if s[front_ptr] not in position_dict:
                    if len(position_dict) == 1:
                        char_back = position_dict.keys()[0]
                        max_len = max(max_len, front_ptr - position_dict[char_back][STARTINDEX] + 1)
                    else:
                        max_len = max(max_len, 1)
                    position_dict[s[front_ptr]] = (front_ptr, front_ptr)
                else:
                    position_dict[s[front_ptr]] = (position_dict[s[front_ptr]][STARTINDEX], front_ptr)
                    if len(position_dict) == 2:
                        char_keys = position_dict.keys()
                        char_one = char_keys[0]
                        char_two = char_keys[1] 
                        max_len = max(max_len, front_ptr - min(position_dict[char_one][STARTINDEX], position_dict[char_two][STARTINDEX]) +1)
                    else:
                        max_len = max(max_len, front_ptr - position_dict[s[front_ptr]][STARTINDEX] + 1)
            front_ptr += 1
        return max_len


    def lengthOfLongestSubstringTwoDistinct_slidingWindow(self, s):
        if len(s) == 0:
            return 0
        position_dict = {}
        max_len = 0
        back_ptr = 0
        front_ptr = 0

        while front_ptr < len(s):
            position_dict[s[front_ptr]] = position_dict.get(s[front_ptr], 0) + 1
            while len(position_dict) > 2:
                position_dict[s[back_ptr]] -= 1
                if position_dict[s[back_ptr]] == 0:
                    del position_dict[s[back_ptr]]
                back_ptr += 1
            max_len = max(max_len, front_ptr - back_ptr + 1)
            front_ptr += 1
        return max_len


#test:
if __name__ == "__main__":
    sol = Solution()
    s1 = "abaccc"
    print sol.lengthOfLongestSubstringTwoDistinct(s1)
    print sol.lengthOfLongestSubstringTwoDistinct_slidingWindow(s1)





