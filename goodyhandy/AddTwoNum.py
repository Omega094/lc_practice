class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        head = previous = None
        while l1 or l2 or carry:
            s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry, val = s/10, s%10
            node = ListNode(val)
            if previous:
                previous.next = node
            else:
                head = node
            previous = node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head

