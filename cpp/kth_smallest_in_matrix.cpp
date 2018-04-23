#include <iostream>
#include <unordered_map>
#include <queue>
#include <functional>
#include <string>
#include <tuple>
#include <functional>
using namespace std;

class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        priority_queue < tuple<int, int, int>, vector<tuple<int, int, int >>, greater<tuple<int, int, int >>> queue;
        for (int i = 0; i < matrix.size(); ++i){
            queue.push(make_tuple(matrix[i][0], i, 0));
        }
        for (int i = 0; i < k - 1; ++i){
            int val, rowNum, colNum;
            tie(val, rowNum, colNum) = queue.top();
            queue.pop();
            if (colNum + 1 < matrix[0].size())
                queue.push(make_tuple(matrix[rowNum][colNum + 1], rowNum, colNum + 1));
        }
        int val, rowNum, colNum;
        tie(val, rowNum, colNum) = queue.top();
        return val;
    }
};

int main(){
    vector<vector<int>> matrix{ {1,5,9}, {10,11,13}, {12,13,15} };
    Solution sol;
    cout << sol.kthSmallest(matrix, 8);
    getchar();
    return 0;
}
