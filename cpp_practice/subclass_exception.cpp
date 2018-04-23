//
//  main.cpp
//  Leetcode_cpp
//
//  Created by Jin Zhao on 7/14/16.
//  Copyright © 2016 Jin Zhao. All rights reserved.
//

#include <iostream>
#include <exception>

using namespace std;

void goesWrong(){
    bool error1Detected = true;
    bool error2Detected = false;
    
    if (error1Detected){
        throw bad_alloc();
    }
    if(error2Detected){
        throw exception();
    }
    return ;
}

int main(){
    try {
        goesWrong();
    } catch (bad_alloc &e) {
        cout << "Catching bad_alloc: " << e.what() <<endl;
    }
    catch (exception &e){
        cout << "Catching exception: " << e.what() <<endl;
    }
    return 0;
}
