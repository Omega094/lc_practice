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
#include <memory>
using namespace std;

class Memcache {
	map<int, pair<int, int>> data;
public:
	Memcache() {
		// initialize your data structure here.
	}

	int get(int curtTime, int key) {
		// Write your code here
		if (data.find(key) == data.end() || data[key].second < curtTime) {
			return INT_MAX;
		}
		return data[key].first;

	}

	void set(int curtTime, int key, int value, int ttl) {
		// Write your code here
		if (ttl == 0){
			data[key] = make_pair(value, INT_MAX);
		}
		else{
			data[key] = make_pair(value, curtTime + ttl - 1);
		}
		return;
	}

	void del(int curtTime, int key) {
		// Write your code here
		data.erase(key);
		return;
	}

	int incr(int curtTime, int key, int delta) {
		// Write your code here
		if (data.find(key) == data.end() || data[key].second < curtTime) {
			return INT_MAX;
		}
		int newVal = data[key].first + delta;
		data[key] = make_pair(newVal, data[key].second);
		return newVal;

	}

	int decr(int curtTime, int key, int delta) {
		// Write your code here
		if (data.find(key) == data.end() || data[key].second < curtTime) {
			return INT_MAX;
		}
		int newVal = data[key].first - delta;
		data[key] = make_pair(newVal, data[key].second);
		return newVal;
	}
};

int main(){
	shared_ptr<Memcache> memcache = make_shared<Memcache>();
	memcache->set(1, 2, 1, 1);
	cout << memcache->get(2, 2);
	getchar();
	return 0;
}
