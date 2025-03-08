#include <iostream>

using namespace std;

int main() {
    int N, n, rev;
    do {
        cin >> N;
        if (!N) break;
        
        n = N;
        rev = 0;
        while (n) {
            rev = rev * 10 + n % 10;
            n /= 10;
        }
        cout << (N == rev ? "yes" : "no") << endl;
    } while (N > 0);
    return 0;
}
