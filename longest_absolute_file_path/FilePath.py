class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        filePathArr = []
        longestFilePathLen = 0
        input = input.split("\n")
        filePathArr.append(0)
        for f in input:
            fName = f.lstrip("\t")
            level = len(f) - len(fName)
            if "." in fName:
                #print fName, len(fName),len(f), ">>>>>>>", level
                longestFilePathLen = max(longestFilePathLen, filePathArr[level]+len(fName))
            else:
                if len(filePathArr) <= level+1:
                    filePathArr.append(len(fName) + filePathArr[level]+1)
                else:
                    filePathArr[level+1] = len(fName) + filePathArr[level]+1
        print filePathArr
        return longestFilePathLen
 
#test
sol = Solution()
print sol.lenghtLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")
