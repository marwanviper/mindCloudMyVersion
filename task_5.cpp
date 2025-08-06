#include <iostream>
using namespace std;

int main(){
    int s, t, a, b, m, n;
    int apples = 0, oranges = 0;
    cin >> s >> t >> a >> b >> m >> n;
    int apple, orange;
    for (int i = 0; i < m;i++){
        cin >> apple;
        if (a + apple >= s && a + apple <= t) {
            apples++;
        }
    }
    for (int i = 0; i < n;i++){
        cin >> orange;
        if (b + orange >= s && b + orange <= t) {
            oranges++;
        }
    }
    cout << apples << endl;
    cout << oranges << endl;
        return 0;
}