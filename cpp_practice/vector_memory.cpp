//
//  main.cpp
//  Leetcode_cpp
//
//  Created by Jin Zhao on 7/14/16.
//  Copyright © 2016 Jin Zhao. All rights reserved.
//
#include <vector>
#include <iostream>
using namespace std;

int main(){
    vector<double> numbers(0);
    cout << "Size: " << numbers.size() << endl;
    
    int capacity = numbers.capacity();
    cout << "Capacity : " << capacity <<endl;
    
    for (int i = 0; i < 10000 ; i++){
        if (numbers.capacity() != capacity){
            capacity = numbers.capacity();
            cout << "Capacity : " << capacity <<endl;
        }
        numbers.push_back(i);
    }
    
    numbers.reserve(1000000);
    cout << numbers[2] << endl;
    cout << "Size: " << numbers.size() << endl;
    cout << "Capacity: " << numbers.capacity() << endl;
    return 0;
}
