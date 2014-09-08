#include <iostream>
using namespace std;
class Solution {
public:
    int singleNumber(int A[], int n) {
        int ones = 0;
        int twos = 0;
        for (int i = 0; i < n; i++) {
            int zeros = ~(ones | twos);
            ones = (ones & ~A[i]) | (zeros & A[i]);
            twos = (twos & ~A[i]) | (ones & A[i]);
        }
        cout << ones << '\t' << twos << endl;
    }
};

int main() {
    Solution sol;
    int A[6] = {100, 101, 101, 102, 102, 102};
    sol.singleNumber(A, 6);
}
