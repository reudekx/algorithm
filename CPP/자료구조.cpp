/*
c++ 자료구조 정리

*/

#include <vector>
#include <algorithm>

using namespace std;

void vector_test() {
    int n = 10;
    vector<int> v(n);
    iota(v.begin(), v.end(), 0);

    // 10과 일치하는 첫 번째 요소의 반복자 반환
    auto iter = find(v.begin(), v.end(), 3);

    auto idx = find(v.begin(), v.end(), 3) - v.begin();

}
