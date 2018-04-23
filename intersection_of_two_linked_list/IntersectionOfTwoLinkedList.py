# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode_hashTable(self, headA, headB):
        if headA == None or headB == None: return
        dict = {}
        tempHead = headA
        while tempHead != None:
            dict[tempHead] = 1
            tempHead = tempHead.next
        while headB != None:
            if dict.has_key(headB):
                return headB
            headB = headB.next
        return None 
        
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB: return None
        counterA = 0
        counterB = 0
        tempA = headA
        tempB = headB
        while tempA:
            counterA += 1
            tempA = tempA.next
        while tempB:
            counterB += 1
            tempB = tempB.next
        #Make sure B is longer
        if counterA > counterB:
            headA, headB = headB, headA
            counterA, counterB = counterB, counterA
        extraStep = counterB - counterA
        while extraStep != 0:
            headB = headB.next
            extraStep -= 1
        while headA != None or headB != None:
            if headA == headB: return headA
            headA = headA.next
            headB = headB.next
        return None
