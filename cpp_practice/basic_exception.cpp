//
//  main.cpp
//  Leetcode_cpp
//
//  Created by Jin Zhao on 7/14/16.
//  Copyright © 2016 Jin Zhao. All rights reserved.
//

#include <iostream>
using namespace std;

void mightgoWrong(){
    bool error1 = true;
    bool error2 = true;
    if (error1){
        throw 4;
    }
    if (error2){
        throw string("Something else went wrong");
    }
}

void usesMightGoWrong(){
    mightgoWrong();
}

int main(){
    try {
        usesMightGoWrong();
    } catch (int e) {
        cout << "Error code: "<<e<<endl;
    }
    catch(char const * e){
        cout << "Error message : "<< e <<endl;
    }
    catch(string &e){
        cout << "String error message: " << e << endl;
    }
    
    cout<< "Still running " << endl;
    return 0;
}
