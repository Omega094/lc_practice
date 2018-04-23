class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split(".")
        v2 = version2.split(".")
        len1 = len(v1)
        len2 = len(v2)
        iter = max(len(v1), len(v2))
        for i in range(0, iter):
            if i < len1 and i < len2:
                if int(v1[i]) < int(v2[i]):
                    return -1
                elif int(v1[i]) > int(v2[i]):
                    return 1
                else:
                    continue
            else:
                if i < len1:
                    if int(v1[i]) > 0 : return 1
                if i < len2:
                    if int(v2[i]) > 0: return -1
        return 0


#test
if __name__ == "__main__":
   sol = Solution()
   print sol.compareVersion("0.1", "1.1")
