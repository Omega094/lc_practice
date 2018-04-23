#include <iostream>
#include <string>
#include <algorithm>
#include <list>
#include <unordered_map>
using namespace std;
#include <list>

class LRUCache {
public:
    LRUCache(int capacity): capa_(capacity){};
    
    int get(int key) {
        if (map_.find(key) != map_.end()){
            const auto value = map_[key]->second;
            update(key, value);
            return value;
        }
        return -1;
         
    }
    
    void set(int key, int value) {
        if (map_.find(key) == map_.end() && list_.size() == capa_)
        {
            auto del = list_.back();
            list_.pop_back();
            map_.erase(del.first);
        }
        update(key, value);
    }
    
private:
    int capa_;
    list<pair<int, int>> list_;
    unordered_map<int, list<pair<int, int>>::iterator> map_;
    
    void update(int key, int val){
        auto it = map_.find(key);
        if (it != map_.end()){
            list_.erase(it->second);
        }
        list_.emplace_front(key, val);
        map_[key] = list_.begin();
    }
};


int main(int argc, const char * argv[]) {
    // insert code here...
    LRUCache cache(2);
    cache.set(5, 4);
    cache.set(9,9);
    cout<<cache.get(5)<<endl;
    
    return 0;
}

