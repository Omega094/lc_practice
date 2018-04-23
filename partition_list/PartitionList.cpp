#include "../common.cpp"
#include <iostream>


class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        
        ListNode* smallerPreHead = new ListNode(0);
        ListNode* largerPreHead = new ListNode(0);
        ListNode* currentSmallerHead = smallerPreHead;
        ListNode* currentLargerHead = largerPreHead;
        ListNode* current = head;
        
        if (!head || !head->next ) return head;
        while (current)
        {
            if (current->val < x) {
                currentSmallerHead->next = current;
                currentSmallerHead = currentSmallerHead->next;
            }
            else{
                currentLargerHead->next = current;
                currentLargerHead = currentLargerHead->next;
            }
            current = current->next;
        }
        currentSmallerHead->next = largerPreHead->next;
        //Avoid circle
        currentLargerHead->next = nullptr;
        return smallerPreHead->next;
        
    }
};


int main()
{
    Solution sol;
    std::vector<std::pair<std::vector<int>, int>> tests = {
        { {}, 0 }
        , { {1,1,1,1,1,1,1}, 0 }
        , { {1,1,1,1,1,1,1}, 1 }
        , { {1,1,1,1,1,1,1}, 2 }
        , { {1,4,3,2,5,2}, 3 }
    };
    
    for (auto& test: tests){
        
        auto input = constructListNode(test.first);
        std::cout<<"data";
        printListNode(input);
        std::cout<<" partitioned by : "<< test.second <<std::endl;
        
        auto result = sol.partition(input, test.second);
        std::cout<<"result: ";
        printListNode(result);
        std::cout << std::endl;
    }
    return 0;
    
}