#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>

class Solution {
public:
    bool isScramble(std::string s1, std::string s2) {
        if (s1 == s2) return true;
        int length1 = s1.size();
        int length2 = s2.size();
        if (length1 != length2) return false;
        std::string tempS1 = s1;
        std::string tempS2 = s2;
        std::sort(tempS1.begin(), tempS1.end());
        std::sort(tempS2.begin(), tempS2.end());
        if (tempS1 != tempS2) return false;
        for (int i= 1; i < s1.size(); ++i){
            if (this->isScramble(s1.substr(0,i), s2.substr(0,i)) &&
                this->isScramble(s1.substr(i,s1.size()-i), s2.substr(i,s2.size()-i)
                                 ) )return true;
            
            if (this->isScramble(s1.substr(0,i), s2.substr(s2.size()-i,i)) &&
                this->isScramble(s1.substr(i,s1.size()-i), s2.substr(0, s2.size()-i))
                ) return true;
        }
        return false;
        
    }
};



int main()
{
    Solution sol;
    std::string s1 = "great";
    std::string s2 = "rgtae";
    std::cout<< true<<std::endl;
    std::cout<< sol.isScramble(s1, s2)<<std::endl;
    return 0;
}