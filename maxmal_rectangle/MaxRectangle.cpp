#include <iostream>
#include <vector>
#include <iterator>
#include <algorithm>

class Solution {
public:
    int maximalRectangle(std::vector<std::vector<char>>& matrix)
    {
        if (matrix.empty() ) return 0;
        int width = matrix[0].size();
        int height = matrix.size();
        int maxArea = 0;
        std::vector<std::vector<int>> table(height, std::vector<int>(width, 0));
        for (int i = 0; i < width; ++i) {
            table[0][i] = int(matrix[0][i] == '1');
        }
        maxArea = std::max(maxArea, largestRectangleArea(table[0]));
        for (int y = 1; y < height; ++y)
        {
            for (int x = 0; x < width ; ++ x){
                std::cout<<matrix[y][x]<<std::endl;
                if (matrix[y][x] == '0') table[y][x] = 0;
                else
                {
                    table[y][x] = table[y-1][x] + 1;
                }
            }
            maxArea = std::max(maxArea, largestRectangleArea(table[y]));
        }
        return maxArea;
        
    }
    
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
    std::vector<std::vector<char>> board = {{'0','0','1'}};
    std::cout<< sol.maximalRectangle(board)<<std::endl;
    return 0;
}