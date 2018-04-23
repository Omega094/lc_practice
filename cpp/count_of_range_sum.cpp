//
//  main.cpp
//  Leetcode_cpp
//
//  Created by Jin Zhao on 7/14/16.
//  Copyright © 2016 Jin Zhao. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int countRangeSum(vector<int>& nums, int lower, int upper){
        vector<long long> prefix(1,0);
        for (auto num : nums){
            prefix.push_back(prefix.back() + num);
        }
        return mergeHelper(0, prefix.size(), prefix, lower, upper);
    }
    
    int mergeHelper(size_t low, size_t high, vector<long long>& prefix, int lower, int upper){
        size_t mid = (low + high) / 2;
        if (mid == low) return 0;
        int count = mergeHelper(low, mid, prefix, lower, upper) + mergeHelper(mid, high, prefix, lower, upper);
        size_t i = mid; 
        size_t j = mid;
        for (size_t left  = low; left < mid; ++left ){
            while ( i < high && prefix[i] - prefix[left] < lower) ++i;
            while ( j < high && prefix[j] - prefix[left] <= upper) ++j;
            count += j - i;
        }
        sort(prefix.begin() + low, prefix.begin() + high);
        return count;
    }
    
    
};



int main(){
    vector<int> arr = {-2,5,-1};
    Solution sol ; 
    cout<< sol.countRangeSum(arr, -2, 2)<<endl;
    return 0;
}
