class Solution(object):

    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        lst = path.split('/')
        while '.' in lst:
            lst.remove('.')
        pathSequence = []
        for i, folder in enumerate(lst):
            if folder != '' and folder != '..':
                pathSequence.append(folder)
            elif folder == '..':
                if pathSequence:
                    pathSequence.pop()
        return '/'+'/'.join(pathSequence)

#test:

if __name__ == "__main__":
    sol = Solution()
    print sol.simplifyPath("/a/./b/../../c/")