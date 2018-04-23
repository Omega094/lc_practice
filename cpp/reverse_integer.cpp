class Solution {
public:
    int reverse(int x) {
        bool isNegative = ( x < 0);
        x = abs(x);
        int result = 0;
        while (x > 0){
            if (result > ((INT_MAX - (x%10)) / 10)) return 0;
            result *= 10;
            result += x%10;
            x = x / 10;
        };
        return (isNegative ? (-1)*result : result );
    }
};

