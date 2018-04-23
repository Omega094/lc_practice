
//++ -std=c++11 common.cpp -o  common
#pragma once

#include <vector>
#include <iostream>
#include <queue>
#include <iomanip>
#include <stdlib.h> // for atoi

/*
 * Common helper functions
 */


std::string to_string(int val){
    if (val == 0){
        return "0";
    }
    bool is_positive = true;
    if (val < 0) {
        is_positive = false;
        val = -val;
    }
    std::string res;
    while (val > 0) {
        //The ASCII code of '0' plus val. 
        res = std::string(1, '0' + val % 10) + res;
        val /= 10 ;
    }
    return is_positive ? res: "-" + res;
}

/*
 * Linked list related code
 */


struct ListNode {
    int val;
    ListNode *next;
    ListNode (int x): val(x), next(nullptr){}
};

ListNode* constructListNode(const std::vector<int>& list){
    ListNode *res = nullptr;
    ListNode *cur = nullptr;
    for (const auto& item : list) {
        ListNode *temp = new ListNode(item);
        if(!res){
            res = temp;
        }
        else{
            cur->next = temp;
        }
        cur = temp;
    }
    return res;
}

void printListNode(const ListNode* input){
    for (auto item = input; item != nullptr; item = item->next) {
        std::cout << item->val << "->";
    }
    std::cout << "nullptr" <<std::endl;
}

/*
 * Tree related code
 */

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) { }
};

TreeNode* constructTreeByLevel(std::vector<int> level)
{
    if (level.empty()) { return nullptr; }
    
    TreeNode *res = new TreeNode(level[0]);
    std::queue<TreeNode*> queue;
    queue.push(res);
    
    int i = 1;
    while (i < level.size()) {
        auto cur = queue.front();
        queue.pop();
        cur->left = new TreeNode(level[i++]);
        queue.push(cur->left);
        
        if (i < level.size()) {
            cur->right = new TreeNode(level[i++]);
            queue.push(cur->right);
        }
    }
    
    return res;
}

TreeNode* constructTreeBySymbol(std::vector<std::string> const& tree) {
    if (tree.empty() || tree[0] == "#") { return nullptr; }
    
    TreeNode* root = new TreeNode(atoi(tree[0].c_str()));
    std::queue<TreeNode*> queue;
    queue.push(root);
    int i = 1;
    while (i < tree.size()) {
        auto cur = queue.front();
        queue.pop();
        if (tree[i] != "#") {
            cur->left = new TreeNode(atoi(tree[i].c_str()));
            queue.push(cur->left);
        }
        ++i;
        if (tree[i] != "#" && i < tree.size()) {
            cur->right = new TreeNode(atoi(tree[i].c_str()));
            queue.push(cur->right);
        }
        ++i;
    }
    return root;
}

// assumes this is a full tree!!!
void printFullTree(TreeNode* root)
{
    if (!root) { std::cout << "NULL" << std::endl; return; }
    std::queue<TreeNode*> queue;
    queue.push(root);
    queue.push(nullptr); // used to print the end of current level
    
    while (!queue.empty()) {
        auto cur = queue.front();
        queue.pop();
        if (cur) {
            std::cout << cur->val << ",";
            if (cur->left) queue.push(cur->left);
            if (cur->right) queue.push(cur->right);
        } else {
            std::cout << std::endl;
            if (queue.empty()) { return; }
            else { queue.push(nullptr); }
        }
    }
}

/*
 * pretty print a binary tree
 */
void prettyPrintTree(TreeNode* root, std::vector<std::string> s = {})
{
    for (auto const& val : s) {
        std::cout << val;
    }
    if (!s.empty()) { std::cout << "__"; }
    if (!root) { std::cout << "(#)" << std::endl;  return; }
    
    std::cout << "(" << root->val << ")" << std::endl;
    s.push_back("  |");
    prettyPrintTree(root->left, s);
    s.pop_back();
    s.push_back("   ");
    prettyPrintTree(root->right, s);
}


//This is a test for the function above.
//int main(){
//    int const a = -1234567;
//    std::cout<< to_string(a) <<std::endl;
//    int number = '0' + 5;
//    char charNumber = '0' + 5;
//    std::cout<<"number: "<<number<<" charNumber: " << charNumber<<std::endl;
//    std::vector<int> list = {1,2,3,4,5,6,7,8,9,10};
//    ListNode *head = constructListNode(list);
//    printListNode(head);
//    
//    TreeNode* node = constructTreeByLevel(list);
//    printFullTree(node);
//    prettyPrintTree(node);
//    
//}
