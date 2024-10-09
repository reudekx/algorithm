#include <string>
#include <vector>
#include <queue>

#include <utility>
#include <iostream>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int time = 1;
    int cur = 1;
    int sum_weight = truck_weights[0];
    queue<pair<int, int>> q;
    q.push(pair{0, 0});
    while (!q.empty()) {
        auto [truck_num, truck_time] = q.front();
        if (time - truck_time == bridge_length) {
            q.pop();
            sum_weight -= truck_weights[truck_num];
        }
        if (cur < truck_weights.size() && sum_weight + truck_weights[cur] <= weight) {
            q.push(pair{cur, time});
            sum_weight += truck_weights[cur];
            ++cur;
        }
        ++time;
    }
    return time;
}

/*
풀이 시간: 23분
접근:
    1초에 1칸 이동인 듯..

    현재 총 무게를 알아야 하고, 트럭이 다리 위에 몇 초 간 있었는지 알아야 한다.
    
    timer를 설정하여.. 무게와 올라간 시간을 큐에 넣고,
    timer를 확인하며 pop해주면 된다. 
후기:
    생각보다 각종 변수들의 초기값을 설정하는 게 까다로웠다.

*/