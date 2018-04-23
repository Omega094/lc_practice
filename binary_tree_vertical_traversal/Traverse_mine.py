class Solution(object):
    def traverseHelper(self, root, position, listDict):
        if root:
            if root.left:
                listDict[position-1].append(root.left.val)
            if root.right:
                listDict[position+1].append(root.right.val)
            self.traverseHelper(root.left,position-1, listDict)
            self.traverseHelper(root.right,position+1, listDict)
            
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import defaultdict
        listDict = defaultdict(list)
        if root:
            listDict[0].append(root.val)
        self.traverseHelper(root, 0, listDict)
        result = []
        positionKeys = listDict.keys()
        positionKeys.sort()
        for key in positionKeys:
            result.append(listDict[key])
        return result
