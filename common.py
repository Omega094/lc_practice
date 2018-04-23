class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        config = str(self.val) + "->"
        nextNode = self.next
        while nextNode:
            config = config + str(nextNode.val) + "->"
            nextNode = nextNode.next
        config = config + "Null"
        return config

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import Queue
def build_tree_by_level(nums):
    if not nums:return None
    head = TreeNode(nums[0])
    queue = Queue.deque()
    queue.append(head)
    i = 1
    while i < len(nums):
        current_node = queue.popleft()
        current_node.left = TreeNode(nums[i])
        i = i + 1
        queue.append(current_node.left)
        if ( i < len(nums)) :
            current_node.right = TreeNode(nums[i])
            i = i + 1
            queue.append(current_node.right)
    return head


def print_tree(tree_root):
    if not tree_root: print "NULL"
    queue = Queue.deque()
    queue.append(tree_root)
    queue.append(None)
    while queue:
        current_node = queue.popleft()
        if current_node :
            print current_node.val , ',',
            if current_node.left : queue.append(current_node.left)
            if current_node.right: queue.append(current_node.right)
        else:
            #print " ", 
            if not queue: return 
            else: queue.append(None)

def pretty_print_tree(tree_root, queue = []):
    #need to deep copy in here. 
    import copy
    out =  "".join(queue)
    if queue : out = out + "__"
    if not tree_root: 
        out = out + "(#)"
        print out
        return
    out = out + "(" + str(tree_root.val) + ")"
    print out
    queue.append("  |");
    pretty_print_tree(tree_root.left, copy.deepcopy(queue))
    queue.pop()
    queue.append("   ");
    pretty_print_tree(tree_root.right, copy.deepcopy(queue))


def construct_node_from_list(nums):
    head = ListNode(nums[0])
    tempNode = head
    for num in nums[1:]:
        tempNode.next = ListNode(num)
        tempNode = tempNode.next
    return head


#head = build_tree_by_level([1,2,3,4,5,6,7,8,9,10])
#print_tree(head)
#pretty_print_tree(head)
