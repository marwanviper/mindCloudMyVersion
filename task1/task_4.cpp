#include <iostream>
using namespace std;


int main(){
    int sum1 = 0,sum2 = 0, n , in;
    cin >> n;
    for (int i = 0; i<n; i++) {
        for(int j = 0; j<n; j++){
            cin >> in;
            if (i == j) {
                sum1 += in;
            }
            if (i + j == n - 1) {
                sum2 += in;
            }
        }
    }
    sum1 = sum1 - sum2;
    if(sum1 < 0) {
        sum1 = -1 * sum1;
    }
    cout << sum1 << endl;
    return 0;
}