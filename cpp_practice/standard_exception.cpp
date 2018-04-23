//
//  main.cpp
//  Leetcode_cpp
//
//  Created by Jin Zhao on 7/14/16.
//  Copyright © 2016 Jin Zhao. All rights reserved.
//

#include <iostream>
using namespace std;

class CanGoWrong{
public:
    CanGoWrong(){
        //There is no way to allocate this much memory. 
        char *pMemory = new char[-9];
        delete[] pMemory;
    }
};


int main(){
    try {
        CanGoWrong wrong;
    } catch (bad_alloc &e) {
        cout<< "Caught exception: " << e.what() <<endl;
    }
    cout << "Still running " <<endl;
    
    return 0;
}
