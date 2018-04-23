#include <iostream>
#include <unordered_map>
#include <queue>
#include <functional>
#include <string>
#include <list>
using namespace std;
class Solution {
    
    unordered_map<string, list<string> > graph;
    void buildGraph(const list<pair<string ,string>> tickets){
        for (auto e : tickets){
            graph[e.first].push_back(e.second);
        }
        for (auto e : graph){
            graph[e.first].sort();
        }
        return;
    };
    
    bool dfs(vector<string>& path, string source, int targetLen){
        path.emplace_back(source);
        if (path.size() == targetLen) return true;
        int length = graph[source].size();
        for (int i = 0; i < length; ++i){
            string t = graph[source].front();
            graph[source].pop_front();
            if (dfs(path, t, targetLen)) return true;
            graph[source].push_back(t);
        }
        path.pop_back();
        return false;
    }
    
public:
    vector<string> findItinerary(vector<pair<string, string>> tickets) {
        list<pair<string, string>> ticketList { begin(tickets), end(tickets) };
        buildGraph(ticketList);
        vector<string> path{};
        string source = "JFK";
        int targetLen = ticketList.size() + 1;
        dfs(path, source, targetLen);
        return path;
    }
};
int main(){
    vector<pair<string, string>> tickets{ { "JFK", "SFO" }, { "JFK", "ATL" }, { "SFO", "ATL" }, { "ATL", "JFK" }, { "ATL", "SFO" } };
    Solution sol;
    vector<string> path = sol.findItinerary(tickets);
    for (auto& city : path){
        cout << city << endl;
    }
    return 0;
}

