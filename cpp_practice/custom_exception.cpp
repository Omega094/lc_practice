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

class MyException: public exception{
    public :
    virtual const char* what() const throw(){
        return "Something bad happened!";
    }
};

class Test{
public:
    void goesWrong(){
        throw MyException();
    }
};

int main(){
    Test test;
    try {
        test.goesWrong();
    } catch (MyException &e) {
        cout << e.what()<<endl;
    }
    return 0;
};
