import collections
class Solution(object):

    def groupStrings(self, strings):
        groups = collections.defaultdict(list)
        for s in strings:
            groups[tuple((ord(c) - ord(s[0])) % 26 for c in s)].append(s)
            print groups
        return map(sorted, groups.values())
#test
if __name__ == "__main__":
    sol = Solution()
    print sol.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"])
