#include <string>
#include <vector>
#include <iostream>

using namespace std;

int n;

void print_vector(vector<int>& vec) {
    for (auto& e : vec) {
        cout << e << ' ';
    }
    cout << '\n';
}

vector<int> calc_lefts(vector<int>& progresses, vector<int>& speeds) {
    vector<int> lefts(n, 0);
    for (int i = 0; i < n; ++i) {
        lefts[i] = (100 - progresses[i]) / speeds[i] + (int)((100 - progresses[i]) % speeds[i] != 0);
    }
    return lefts;
}

vector<int> count_deploys(vector<int>& lefts) {
    vector<int> deploys;
    vector<int> stack;
    
    int cnt = 0;
    for (auto& left : lefts) {
        while (!stack.empty() && left > stack.back()) {
            stack.pop_back();
            ++cnt;
        }
        if (stack.empty() and cnt != 0) {
            deploys.push_back(cnt);
            cnt = 0;
        }
        stack.push_back(left);
    }
    while (!stack.empty()) {
        stack.pop_back();
        ++cnt;
    }
    if (cnt != 0) {
        deploys.push_back(cnt);
    }
    
    return deploys;
}

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    n = progresses.size();
    auto lefts = calc_lefts(progresses, speeds);
    print_vector(lefts);
    auto deploys = count_deploys(lefts);
    
    return deploys;
}

/*
풀이 시간: 21분
접근:
    개발은 동시에 이뤄지고, 배포 시에는 100% 이상이 되어야 한다.
    
    또한 순서대로 배포 가능 (뒤에 건 대기해야 한다.)
    
    O(n^2)으로 풀 수 있으나, 스택을 이용하여 O(n) 풀이를 해보자.
    
    먼저 남은 일수를 계산하자.
    
    남은 일수 = (100 - progress) // speed + int((100 - progress) % speed == 0)
후기:

    pop하는 조건을 잘못 생각하여 헤맸다. 풀이 과정을 정확하게 잘 생각해야 한다.

    또한 그냥 max_day를 유지하면서 풀었어도 됐다.

*/