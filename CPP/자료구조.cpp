/*
c++ 자료구조 정리

*/

#include <iostream>
#include <algorithm>
#include <numeric>

#include <vector>

using namespace std;

void print(const auto& iter) {
    cout << "Value: " << *iter << '\n';
}

void vector_test() {
    int n = 10;
    vector<int> v(n);
    iota(v.begin(), v.end(), 0);

    // 10과 일치하는 첫 번째 요소의 반복자 반환
    auto iter1 = find(v.begin(), v.end(), 3);

    auto iter2 = find_if(v.begin(), v.end(), [](int n) { return n >= 5; });

    print(iter1);
    print(iter2);
}


int main() {
    vector_test();


    return 0;
}
