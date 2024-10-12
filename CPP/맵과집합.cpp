#include <map>
#include <set>

#include <unordered_map>
#include <unordered_set>

#include <string>

#include <algorithm>
#include <numeric>

#include <iostream>

#define endl '\n'

using namespace std;


int main() {
    map<string, int> str_cnt;

    set<string> str_set;

    string strs[] = {
        "apple", "banana", "carrot", "diamond", "effect", "apple", "banana"
    };

    for (auto& str : strs) {
        str_cnt[str]++;
        str_set.insert(str);
    }

    cout << "===== Map Result. =====" << endl;

    for (auto& [str, cnt] : str_cnt) {
        cout << "string: " << str << ", cnt: " << cnt << endl;
    }

    cout << "===== Set Result. =====" << endl;

    for (auto& str : str_set) {
        cout << "string: " << str << endl;
    }

    return 0;
}