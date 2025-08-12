#include <iostream>


using namespace std;
int main() {
    int a[4];
    int sum = 0;
    for (int i = 0; i < 4; i++) {
        cin >> a[i];
    }
    while(a[0] != 0 && a[2] != 0 && a[3] != 0){
        sum += 256;
        a[0]--;
        a[2]--;
        a[3]--;
    }
    while(a[0] != 0 && a[1] != 0){
        sum += 32;
        a[0]--;
        a[1]--;
    }
    cout << sum << endl; 

    return 0;
}