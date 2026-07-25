class Solution {
public:
    int reverse(int x) {
        int num = x;
        int ans = 0;

        while(num){
            int rem = num % 10;
            num = num / 10;

            // Conditions to look for while facing stack overflow ;-;
            if (ans > INT_MAX / 10 || ans < INT_MIN / 10){
                return 0;
            }

            if ((ans == INT_MAX / 10 && rem > 7) || (ans == INT_MIN / 10 && rem < -8)){
                return 0;
            }

            ans = ans*10 + rem;
        }
        return ans;
    }
};