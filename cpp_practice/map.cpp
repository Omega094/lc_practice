//
//  main.cpp
//  Leetcode_cpp
//
//  Created by Jin Zhao on 7/14/16.
//  Copyright © 2016 Jin Zhao. All rights reserved.
//
#include <iostream>
#include <map>
using namespace std;

int main(){
    map<string, int> ages;
    
    ages["Mike"] = 40;
    ages["Raj"] = 20;
    ages["Vicky"] = 30;
    ages["Mike"] = 70;
    
    
    ages.insert(make_pair("Peter", 100));
    cout << ages["Raj"] << endl;
    if (ages.find("Vicky") != ages.end()){
        cout << "found Vicky " <<endl;
    }else{
        cout << "Key not found " <<endl;
    }
    
    for (map<string, int>::iterator it = ages.begin(); it != ages.end(); it ++){
 
        cout << it->first << ": " <<it->second <<endl;
    }
    return 0;
}
