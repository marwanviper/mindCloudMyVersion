#include <iostream>


using namespace std;
int main() {
    int n, m;
    float avg = 0;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> m;
        avg += m;
    }
    avg /= n;
    cout << avg << endl;
    return 0;
}


