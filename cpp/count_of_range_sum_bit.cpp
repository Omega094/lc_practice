//
//  main.cpp
//  Leetcode_cpp
//
//  Created by Jin Zhao on 7/14/16.
//  Copyright © 2016 Jin Zhao. All rights reserved.
//
#include <vector>
#include <unordered_map>
using namespace std;

typedef long long LL;

class BIT{
    vector<int> arr;
    int n;
    inline int lowbit(int x){
        return x& -x;
    }
    
public:
    BIT(int n) : n(n), arr(n+1, 0){}
    
    void add(int x){
        while (x <= n){
            arr[x] += 1;
            x += lowbit(x);
        }
    }
    
    int sum(int x){
        int res = 0;
        while (x > 0){
            res += arr[x];
            x -= lowbit(x);
        }
        return res;
    }
    
};

class Solution{
public:
    int countRangeSum(vector<int>& nums, int lower, int upper){
        if (nums.size() == 0) return 0;
        vector<LL> sum_array(nums.size()*3, 0);
        LL sum = 0;
        for (int i = 0 ; i < nums.size(); i ++ ){
            sum += nums[i];
            sum_array[i*3] = sum;
            sum_array[i*3+1] = sum + lower -1;
            sum_array[i * 3 + 2] = sum + upper;
        }
        sum_array.push_back(upper);
        sum_array.push_back(lower-1);
        unordered_map<LL, int> index;
        sort(sum_array.begin(), sum_array.end());
        auto end = unique(sum_array.begin(), sum_array.end());
        auto it = sum_array.begin();
        for (int i = 1; it != end; i ++ , it ++){
            index[*it] = i;
        }
        BIT tree(index.size());
        int ans = 0;
        for (int i = nums.size()-1; i >= 0; i --){
            tree.add(index[sum]);
            sum -= nums[i];
            ans += tree.sum(index[upper + sum]) - tree.sum(index[lower + sum - 1]);
        }
        return ans;
        
    }
};
