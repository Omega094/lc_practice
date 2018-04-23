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
class PhoneDirectory {
        set<int> numSet ;
        int maxNum ;
        queue<int> recycled ;
        int currentMax  ;
public:
    /** Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory. */
    PhoneDirectory(int maxNumbers) {
        maxNum = maxNumbers;
        currentMax = 0;
    }
    
    /** Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available. */
    int get() {
        if (numSet.size() == maxNum) return -1;
        int val = currentMax;
        if (recycled.size() != 0) { val = recycled.front(); recycled.pop();}
        else  ++currentMax;
        numSet.insert(val);
        return val;
    }
    
    /** Check if a number is available or not. */
    bool check(int number) {
        return (numSet.find(number) == numSet.end()) && number < maxNum;
    }
    
    /** Recycle or release a number. */
    void release(int number) {
        if (numSet.find(number) == numSet.end()) return;
        numSet.erase(number);
        recycled.emplace(number);
        return;
    }
};

/**
 * Your PhoneDirectory object will be instantiated and called as such:
 * PhoneDirectory obj = new PhoneDirectory(maxNumbers);
 * int param_1 = obj.get();
 * bool param_2 = obj.check(number);
 * obj.release(number);
 */

int main(){
    return 0;
}
