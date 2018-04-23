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
int main(){
    vector<string> strings;
    
    strings.push_back("one");
    strings.push_back("Two");
    
    for (int i = 0 ; i < strings.size(); i ++ ){
        cout << strings[i] <<endl;
    }
    
    for (auto str : strings){
        cout << str <<endl;
    }
    
    for (vector<string>::iterator it = strings.begin(); it  != strings.end(); it++){
        cout << *it << endl;
    }

    vector<string>::iterator it = strings.begin();
    it += 1;
    cout <<*it << endl;
    return 0;
}
