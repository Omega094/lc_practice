class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stack = []
        preorder = preorder.split(',')
        #This is basically traversing the node
        #Each time we traversed a node , we pop "x,#,#," append an "#", which represents that this node has been traversed(deleted)
        for node in preorder:
            stack.append(node)
            while len(stack) >= 3 and stack[-1] == "#" and stack[-2] == "#" and stack[-3] != "#":
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append("#")
        #If the tree has been traversed, it should be a single None node 
        return stack == ["#"]

#test
if __name__ == "__main__":
    sol = Solution()
    print sol.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")
    print sol.isValidSerialization("1,#,#,#")
