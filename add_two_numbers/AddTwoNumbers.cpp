#include <iostream>
#include <vector>
#include <set>
#include <map>


class Solution
{
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        if (!l1) return l2;
        if (!l2) return l1;
        ListNode *head = new ListNode(0);
        auto pre = head;
        int carry = 0, sum = 0, val = 0;
        while (l1 && l2) {
            sum = l1->val + l2->val;
            val = sum % 10;
            carry = int(sum / 10);
            ListNode* node = new ListNode(val);
            pre->next = node;
            l1 = l1->next, l2 = l2->next, pre = pre->next;
        }
        if (l2) l1 = l2;
        pre->next = l1;
        while (pre->next) {
            sum = l1->val + carry;
            val = sum % 10;
            carry = int(sum/10);
            pre->next->val = val;
            pre = pre -> next;
        }
        if (carry = 1) pre->next = new ListNode(1);
        return *head->next;
    }
}
