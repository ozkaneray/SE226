#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int main() {
    string x;
    cout << "What is your name? ";
    getline(cin, x);
    cout << x << endl;
    cout << "Hello " << x << endl;

    string y;
    cout << "What is your student id? ";
    getline(cin, y);
    cout << "Your id is " << y << endl;

    int toplamsaniye;
    cout << "Enter a large integer: ";
    cin >> toplamsaniye;

    int saat = toplamsaniye / 3600;
    int dakika = (toplamsaniye % 3600) / 60;
    int saniye = toplamsaniye % 60;

    cout << toplamsaniye << " second is " << saat << " hours " << dakika << " minutes, and " << saniye << " seconds." << endl;

    double x1, y1, x2, y2;
    cout << "Enter x1: ";
    cin >> x1;
    cout << "Enter y1: ";
    cin >> y1;
    cout << "Enter x2: ";
    cin >> x2;
    cout << "Enter y2: ";
    cin >> y2;

    double distance = sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1));
    cout << "Distance is = " << distance << endl;

    cout << "*******\n ***** \n  ***  \n   *" << endl;

    return 0;
}