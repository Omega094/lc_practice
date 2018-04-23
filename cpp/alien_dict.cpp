#include <iostream>
#include <unordered_map>
#include <queue>
#include <functional>
#include <string>
#include <tuple>
#include <functional>
#include <map>
#include <unordered_map>
#include <set>
using namespace std;

class Solution {
public:
    string alienOrder(vector<string>& words) {
        unordered_map<char, set<char>> predecessor, successor;
        set<char> chars;
        string pre;
        for (string current : words){
            chars.insert(current.begin(), current.end());
            for (int i = 0; i < min(current.size(), pre.size()); ++i){
                char a = current[i]; char b = pre[i];
                if (a != b){
                    predecessor[a].insert(b);
                    successor[b].insert(a);
                    break;
                }
            }
            pre = current;
        }
        int totalSize = chars.size();
        for (auto p : predecessor){
            chars.erase(p.first);
        }
        string result;
        while (chars.size()){
            char current = *(chars.begin());
            chars.erase(current);
            result += current;
            for (char s : successor[current]){
                predecessor[s].erase(current);
                if (predecessor[s].empty()){
                    chars.insert(s);
                }
            }
        }
        return result.size() == totalSize ? result : "";
    }
};

int main(){
    vector<string> words{ "wrt", "wrf", "er", "ett", "rftt" };
    Solution sol;
    cout << sol.alienOrder(words) << endl;
    getchar();
    return 0;
}