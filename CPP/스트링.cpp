#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    string str1 = "Hello, world!";

    vector<char> vec(str1.begin(), str1.end());

    string str2(vec.begin(), vec.end());

    cout << str2 << endl;

    auto idx1 = str2.find("o");
    auto idx2 = str2.rfind("o");
    auto idx3 = str2.find("a");

    cout << idx1 << " " << idx2 << " " << idx3 << " "  << string::npos << endl;

    return 0;
}