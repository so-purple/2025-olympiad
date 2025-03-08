#include <iostream>
using namespace std;

int main() {
    int N, K, res = 1;
    cin >> N >> K;
    int i;
    for (i = 0; i < K; i++) {
        res *= N--;
    }
    for (i = 1; i < K + 1; i++) {
        res /= i;
    }

    cout << res << endl;
    return 0;
}
