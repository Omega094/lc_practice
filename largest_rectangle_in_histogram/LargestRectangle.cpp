#include <iostream>
#include <vector>
#include <iterator>
#include <algorithm>

class Solution{
public:
    int largestRectangleArea(std::vector<int>& heights){
        int maxArea = 0;
        heights.push_back(0);
        std::vector<int> stack = {};
        int currentIndex = 0;
        while (currentIndex < heights.size())
        {
            if (stack.empty() || heights[currentIndex] >= heights[stack.back()])
            {
                stack.push_back(currentIndex);
                currentIndex ++;
            }
            else
            {
                int leftHeightIndex = stack.back();
                stack.pop_back();
                int width = currentIndex;
                if (!stack.empty()) width = currentIndex - stack.back() - 1;
                maxArea = std::max(maxArea, heights[leftHeightIndex]*width);
            }
        }
        return maxArea;
    }
};


int main(){
    Solution sol;
    std::vector<int> heights = {1,2,3,4,5};
    std::cout<< sol.largestRectangleArea(heights)<<std::endl;
    return 0;
}
