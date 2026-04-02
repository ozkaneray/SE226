#include <iostream>
using namespace std;

double calculate(int n, int current = 1) {
    if (current > n)
        return 0;
    
    int sign = (current % 2 == 0) ? -1 : 1;
    return sign * (1.0 / current) + calculate(n, current + 1);
}

int main() {
    int n;
    cout << "Enter n: ";
    cin >> n;
    
    cout << "S" << n << " = " << calculate(n) << endl;
    return 0;
}
