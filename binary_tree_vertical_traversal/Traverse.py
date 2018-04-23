class Solution(object):
    def traverseHelper(self, root, position, listDict, level):
        if root:
            listDict[position].append((level,root.val))
            self.traverseHelper(root.left,position-1, listDict, level + 1)
            self.traverseHelper(root.right,position+1, listDict, level +1 )
            
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        cols = collections.defaultdict(list)
        queue = [(root, 0)]
        for node, i in queue:
            if node:
                cols[i].append(node.val)
                queue += (node.left, i - 1), (node.right, i + 1)
        return [cols[i] for i in xrange(min(cols.keys()), max(cols.keys()) + 1)] \
                   if cols else []

